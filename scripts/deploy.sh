#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
TF_DIR="$ROOT_DIR/terraform"

echo "==> Formatting Terraform..."
terraform -chdir="$TF_DIR" fmt

echo "==> Validating Terraform..."
terraform -chdir="$TF_DIR" validate

echo "==> Planning Terraform changes..."
terraform -chdir="$TF_DIR" plan

read -r -p "Apply these changes? [y/N]: " confirm

if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Deployment cancelled."
    exit 0
fi

echo "==> Applying Terraform changes..."
terraform -chdir="$TF_DIR" apply

echo "==> Deployment complete."