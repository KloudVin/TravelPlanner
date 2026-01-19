# Terraform Deployment for Karnataka Travel Planner

This directory contains Terraform configuration to deploy the Karnataka Travel Planner application to Azure App Service.

## Prerequisites

1. **Azure CLI**: Install and login
   ```bash
   az login
   ```

2. **Terraform**: Install Terraform CLI (v1.0+)
   ```bash
   # macOS with Homebrew
   brew install terraform
   ```

3. **Azure Subscription**: Ensure you have an active Azure subscription

## Quick Start

1. **Initialize Terraform**:
   ```bash
   cd deployment
   terraform init
   ```

2. **Review the plan**:
   ```bash
   terraform plan -var-file="terraform.tfvars"
   ```

3. **Apply the configuration**:
   ```bash
   terraform apply -var-file="terraform.tfvars"
   ```

4. **Get deployment outputs**:
   ```bash
   terraform output
   ```

## Configuration

Edit `terraform.tfvars` to customize:
- `resource_group_name`: Azure resource group name
- `location`: Azure region (default: "Central US")
- `webapp_name`: Web app name (must be globally unique)
- `app_service_plan_name`: App service plan name
- `sku`: Pricing tier (default: "P1v2" - Premium V2)

## Resources Created

- **Resource Group**: Contains all resources
- **App Service Plan**: Linux plan with Premium V2 tier
- **Web App**: Python 3.11 app with Streamlit configuration
- **App Settings**: Pre-configured for Streamlit deployment
- **Logging**: File system logging enabled

## Deployment

After Terraform apply completes:

1. **Get publish profile** for GitHub Actions:
   ```bash
   az webapp deployment list-publishing-profiles \
     --name vintekh \
     --resource-group TravelPlanner \
     --xml
   ```

2. **Add to GitHub Secrets**:
   - Go to repository Settings → Secrets and variables → Actions
   - Create `AZURE_WEBAPP_PUBLISH_PROFILE` with the XML content

3. **Deploy via GitHub Actions**:
   ```bash
   git push origin main
   ```

## Cleanup

To destroy all resources:
```bash
terraform destroy -var-file="terraform.tfvars"
```

## Custom Domain

To add custom domain after deployment:
```bash
az webapp config hostname add \
  --webapp-name vintekh \
  --resource-group TravelPlanner \
  --hostname vintekh.com
```