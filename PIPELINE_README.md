# Azure DevOps Pipeline Setup for Karnataka Travel Planner

This document explains how to set up and use the Azure DevOps pipeline for deploying the Karnataka Travel Planner application.

## 📋 Prerequisites

1. **Azure DevOps Organization**: https://dev.azure.com/teknohut
2. **Azure Subscription** with appropriate permissions
3. **Service Connection** in Azure DevOps to your Azure subscription

## 🚀 Pipeline Overview

The pipeline consists of three main stages:

### 1. **SetupBackend** - Create Terraform State Storage
- Creates Azure Storage Account for Terraform state management
- Sets up secure state storage for infrastructure tracking

### 2. **TerraformValidate** - Validate Infrastructure Code
- Initializes Terraform with Azure backend
- Validates Terraform configuration
- Creates and reviews execution plan

### 3. **TerraformApply** - Deploy Infrastructure
- Applies Terraform configuration to create Azure resources
- Creates Resource Group, App Service Plan, and Web App

### 4. **DeployApplication** - Deploy Application Code
- Deploys Streamlit application to Azure Web App
- Uses automatic deployment method

## ⚙️ Setup Instructions

### Step 1: Create Azure DevOps Service Connection

1. Go to **Project Settings** → **Service connections**
2. Click **New service connection**
3. Select **Azure Resource Manager**
4. Choose **Service principal (automatic)**
5. Select your subscription and resource group
6. Name it: `Azure-Subscription` (or update the pipeline variable)

### Step 2: Configure Pipeline Variables

In your pipeline, go to **Variables** tab and add:

| Variable Name | Value | Description |
|---------------|-------|-------------|
| `azureSubscription` | `Azure-Subscription` | Your service connection name |
| `resourceGroupName` | `TravelPlanner` | Resource group name |
| `webAppName` | `vintekh` | Web app name |
| `location` | `Central US` | Azure region |

### Step 3: Create Pipeline

1. Go to **Pipelines** → **New Pipeline**
2. Select **Azure Repos Git**
3. Choose your repository
4. Select **Existing Azure Pipelines YAML file**
5. Path: `/azure-pipelines.yml`
6. Save and run

## 🔧 Pipeline Configuration Details

### Terraform Backend
The pipeline automatically creates and configures Azure Storage for Terraform state:
- Storage Account: `tfstate{BuildId}`
- Container: `tfstate`
- State File: `terraform.tfstate`

### Deployment Method
- Uses Azure Web App deployment task
- Automatic deployment detection
- Supports Python applications with custom startup scripts

## 📊 Pipeline Stages Explained

### Stage 1: SetupBackend
```yaml
- Creates resource group if needed
- Creates storage account for Terraform state
- Creates blob container for state files
```

### Stage 2: TerraformValidate
```yaml
- Installs Terraform 1.6.5
- Initializes with Azure backend
- Validates configuration syntax
- Generates and displays execution plan
```

### Stage 3: TerraformApply
```yaml
- Applies infrastructure changes
- Creates Azure resources (RG, App Service Plan, Web App)
- Configures application settings and startup
```

### Stage 4: DeployApplication
```yaml
- Deploys application code to Web App
- Uses auto-deployment method
- Handles Python dependencies automatically
```

## 🔒 Security Considerations

- **Service Principal**: Uses Azure service connection with minimal required permissions
- **State Storage**: Terraform state stored securely in Azure Storage
- **Secrets**: No hardcoded secrets in pipeline or code

## 🚨 Troubleshooting

### Common Issues:

1. **Service Connection Errors**
   - Verify service connection has correct permissions
   - Check subscription and resource group access

2. **Terraform Backend Issues**
   - Ensure storage account creation succeeds
   - Check Azure subscription limits

3. **Deployment Failures**
   - Check application logs in Azure Portal
   - Verify startup.sh permissions and syntax

### Logs and Debugging:
- Pipeline logs show detailed Terraform output
- Azure Portal → Web App → Logs for application issues
- Terraform state visible in storage account

## 📈 Monitoring and Maintenance

- **Pipeline History**: View all deployments in Azure DevOps
- **Resource Monitoring**: Use Azure Portal for resource health
- **Cost Management**: Monitor App Service Plan usage
- **Updates**: Modify `terraform.tfvars` for infrastructure changes

## 🎯 Next Steps

1. Run the pipeline manually to test
2. Set up branch policies for main branch
3. Configure notifications for pipeline failures
4. Set up staging environment if needed

The pipeline provides a complete CI/CD solution for infrastructure and application deployment!