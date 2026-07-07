terraform {
  required_version = ">= 1.8.0"

  cloud {
    organization = "xeals"

    workspaces {
      name = "platforms-lab-local"
    }
  }

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}