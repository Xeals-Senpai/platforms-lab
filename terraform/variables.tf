# terraform/variables.tf

variable "platforms_lab_root" {
  description = "Absolute path to the platforms-lab repository root on the machine running Terraform"
  type        = string
}

variable "discord_webhook_url" {
  description = "Discord webhook URL used by the Grafana contact point"
  type        = string
  sensitive   = true
}