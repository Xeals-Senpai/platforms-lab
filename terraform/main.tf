resource "docker_image" "web" {
  name = "platforms-lab"

  build {
    context    = "${path.module}/../app"
    dockerfile = "Dockerfile"
  }

  triggers = {
    app_py           = filesha256("${path.module}/../app/app.py")
    dockerfile       = filesha256("${path.module}/../app/dockerfile")
    requirements_txt = filesha256("${path.module}/../app/requirements.txt")
  }
}

resource "docker_network" "platforms_lab" {
  name = "platforms-lab-network"
}

resource "docker_image" "prometheus" {
  name = "prom/prometheus:latest"
}

resource "docker_image" "grafana" {
  name = "grafana/grafana:latest"
}

resource "docker_container" "web" {
  name  = "web-container"
  image = docker_image.web.image_id

  networks_advanced {
    name = docker_network.platforms_lab.name
  }

  ports {
    internal = 5050
    external = 5050
  }
}

resource "docker_container" "prometheus" {
  name  = "prometheus"
  image = docker_image.prometheus.image_id

  networks_advanced {
    name = docker_network.platforms_lab.name
  }

  ports {
    internal = 9090
    external = 9090
  }

  volumes {
    host_path      = "${var.platforms_lab_root}/prometheus/prometheus.yml"
    container_path = "/etc/prometheus/prometheus.yml"
  }
}

resource "docker_container" "grafana" {
  name  = "grafana"
  image = docker_image.grafana.image_id

  networks_advanced {
    name = docker_network.platforms_lab.name
  }

  env = [
    "DISCORD_WEBHOOK_URL=${var.discord_webhook_url}"
  ]

  ports {
    internal = 3000
    external = 3000
  }

  volumes {
    host_path      = "${var.platforms_lab_root}/grafana/provisioning"
    container_path = "/etc/grafana/provisioning"
  }

  volumes {
    host_path      = "${var.platforms_lab_root}/grafana/dashboards"
    container_path = "/var/lib/grafana/dashboards"
  }
}