# platforms-lab

[![CI Pipeline](https://github.com/Xeals-Senpai/platforms-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/Xeals-Senpai/platforms-lab/actions/workflows/ci.yml)

End-to-end Platform Engineering and DevOps learning environment demonstrating Infrastructure as Code, observability, incident simulation, CI, and automated CD using Terraform, Docker, Prometheus, Grafana, Flask, and GitHub Actions.

## Overview

Platforms Lab is a local infrastructure playground used to learn, experiment with, and demonstrate modern DevOps and Platform Engineering concepts using Infrastructure as Code, monitoring, observability, alerting, incident simulation, and deployment automation.

The project is intentionally built using local Docker infrastructure to provide a safe and cost-effective environment for testing and troubleshooting without requiring cloud resources.

Current technologies include:

- Terraform
- Docker
- Flask
- Prometheus
- Grafana
- GitHub Actions
- Self-Hosted GitHub Runner
- Ansible

The repository serves as a long-term learning platform where new technologies, operational scenarios, monitoring strategies, and deployment workflows can be added and explored over time.

---

## Current Architecture

```text
GitHub
│
├── GitHub Actions (CI)
│
└── GitHub Actions (CD)
    │
    └── Self-Hosted Runner
         │
         └── Terraform
              │
              ├── Docker Network
              ├── Flask Application
              ├── Prometheus
              └── Grafana

Monitoring Stack
│
├── Flask Metrics
├── Windows Exporter
├── Prometheus
└── Grafana
```

---

## Components

### Terraform

Terraform manages all infrastructure resources, including:

- Docker network creation
- Flask application container deployment
- Prometheus container deployment
- Grafana container deployment

Terraform is used as the primary Infrastructure as Code tool for the project.

### Flask Application

The Flask application provides a simple web service while exposing Prometheus metrics for monitoring and alerting.

Available routes:

| Route | Purpose |
|---------|---------|
| `/` | Basic application response |
| `/metrics` | Prometheus metrics endpoint |
| `/health` | Health probe |
| `/ready` | Readiness probe |
| `/version` | Application version |
| `/slow` | Simulates slow responses |
| `/random` | Simulates intermittent failures |
| `/load` | Simulates high CPU load |
| `/crash` | Simulates application crashes |

These routes are used to create realistic monitoring, troubleshooting, and incident response scenarios.

### Prometheus

Prometheus collects metrics from:

- Flask application
- Windows Exporter

Metrics can be inspected directly through the Prometheus UI.

### Grafana

Grafana provides dashboarding, visualisation, and alerting for collected metrics.

Configuration is provisioned automatically through:

- Datasources as code
- Dashboards as code

No manual dashboard creation is required after deployment.

### Ansible

Ansible configuration is included as part of the project and will be expanded in future iterations to automate system configuration and deployment tasks.

---

## Repository Structure

```text
platforms-lab/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── ansible/
│   ├── inventory.ini
│   └── playbook.yml
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── grafana/
│   ├── dashboards/
│   └── provisioning/
│
├── prometheus/
│   └── prometheus.yml
│
├── scripts/
│   └── deploy.sh
│
├── terraform/
│   ├── versions.tf
│   ├── providers.tf
│   ├── main.tf
│   ├── outputs.tf
│   └── variables.tf
│
└── README.md
```

---

## Monitoring and Alerting

### Prometheus Targets

Current scrape targets:

- Flask application (`web-container`)
- Windows Exporter (`host.docker.internal:9182`)

### Grafana Dashboard

Current dashboard:

**Platforms Lab - Flask Application**

Includes:

- Service Status
- Total Requests
- Uptime
- Version
- Requests per Second
- Memory Usage
- CPU Usage
- Average Response Time
- Application Errors

### Alerting

Configured alerts:

- Flask Service Down
- Slow Response Time
- High CPU Usage
- Application Errors

The application intentionally exposes failure scenarios to validate monitoring and alert behaviour.

---

## Manual Continuous Delivery

Manual deployments are performed using:

```bash
./scripts/deploy.sh
```

The deployment script automatically:

- Formats Terraform
- Validates Terraform
- Generates a Terraform plan
- Applies infrastructure changes

Deployments can be executed from any repository location through automatic path discovery.

---

## Automated Continuous Delivery

Automated deployments are performed through GitHub Actions using a self-hosted runner.

Workflow:

```text
Git Push
    ↓
GitHub Actions
    ↓
Self-Hosted Runner
    ↓
Terraform Plan
    ↓
Terraform Apply
    ↓
Deployment
```

The self-hosted runner is configured as a Windows service and automatically starts with the host machine.

---

## Deployment

### Initialise Terraform

```bash
cd terraform
terraform init
```

### Validate Terraform

```bash
terraform validate
```

### Review Changes

```bash
terraform plan
```

### Deploy Infrastructure

```bash
terraform apply
```

---

## Accessing Services

### Flask Application

```text
http://localhost:5050
```

### Prometheus

```text
http://localhost:9090
```

### Grafana

```text
http://localhost:3000
```

Default Grafana credentials:

```text
Username: admin
Password: admin
```

---

## Learning Objectives

This repository is used to explore:

- Infrastructure as Code
- Docker Networking
- Monitoring and Observability
- Grafana Provisioning
- Prometheus Configuration
- Alerting
- Incident Simulation
- GitHub Actions
- Continuous Integration
- Continuous Delivery
- Self-Hosted Runners
- Troubleshooting and Root Cause Analysis
- Platform Engineering Concepts
- Configuration Management

---

## Project Progress

Completed:

- Terraform-managed infrastructure
- Docker networking
- Flask application deployment
- Prometheus monitoring
- Grafana provisioning
- Dashboard provisioning
- Alerting
- Incident simulation
- Manual Continuous Delivery
- Automated Continuous Delivery
- GitHub Actions CI
- Self-Hosted GitHub Actions Runner

Future Improvements:

- Linux-based deployment runner
- Remote Terraform backend
- Multi-host monitoring
- Additional application metrics
- Expanded Ansible automation
- Container persistence

---

## Purpose

Platforms Lab is intended to be a practical, hands-on environment for learning and demonstrating Platform Engineering, DevOps, Monitoring, Observability, and Infrastructure Automation skills through reproducible, code-driven infrastructure.