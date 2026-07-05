#!/usr/bin/env bash

set -euo pipefail

echo "==> Formatting Terraform..."
terraform fmt

echo "==> Validating Terraform..."
terraform validate

echo "==> Planning Terraform changes..."
terraform plan

read -r -p "Apply these changes? [y/N]: " confirm

if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
  echo "Deployment cancelled."
  exit 0
fi

echo "==> Applying Terraform changes..."
terraform apply

echo "==> Deployment complete."