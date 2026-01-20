# Terraform configuration for Karnataka Travel Planner Azure resources
# Creates all necessary resources for vintekh.com deployment

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>4.57"
    }
  }

  # Backend configuration for Azure DevOps pipeline
  backend "azurerm" {
    resource_group_name  = "TerraformBackent"
    storage_account_name = "vintekhtfbackend"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

# Variables
variable "resource_group_name" {
  description = "Name of the resource group"
  default     = "TravelPlanner"
}

variable "location" {
  description = "Azure region"
  default     = "Central US"
}

variable "webapp_name" {
  description = "Name of the web app"
  default     = "vintekh"
}

variable "app_service_plan_name" {
  description = "Name of the app service plan"
  default     = "vintekh-plan"
}

variable "sku" {
  description = "App service plan SKU"
  default     = "P1v2"
}

# Resource Group
resource "azurerm_resource_group" "travelplanner" {
  name     = var.resource_group_name
  location = var.location
}

# App Service Plan
resource "azurerm_service_plan" "travelplanner" {
  name                = var.app_service_plan_name
  resource_group_name = azurerm_resource_group.travelplanner.name
  location            = azurerm_resource_group.travelplanner.location
  os_type             = "Linux"
  sku_name            = var.sku
}

# Web App
resource "azurerm_linux_web_app" "travelplanner" {
  name                = var.webapp_name
  resource_group_name = azurerm_resource_group.travelplanner.name
  location            = azurerm_resource_group.travelplanner.location
  service_plan_id     = azurerm_service_plan.travelplanner.id

  site_config {
    application_stack {
      python_version = "3.11"
    }

    # Startup file
    app_command_line = "startup.sh"
  }

  # App Settings for Streamlit
  app_settings = {
    "STREAMLIT_SERVER_PORT"                   = "8000"
    "STREAMLIT_SERVER_ADDRESS"                = "0.0.0.0"
    "STREAMLIT_SERVER_HEADLESS"               = "true"
    "STREAMLIT_BROWSER_GATHER_USAGE_STATS"    = "false"
    "STREAMLIT_SERVER_ENABLE_CORS"            = "false"
    "SCM_DO_BUILD_DURING_DEPLOYMENT"          = "true"
    "ENABLE_ORYX_BUILD"                       = "true"
    "WEBSITES_PORT"                           = "8000"
  }

  # Logging configuration
  logs {
    application_logs {
      file_system_level = "Information"
    }
  }
}

# Outputs
output "webapp_url" {
  description = "URL of the deployed web app"
  value       = "https://${azurerm_linux_web_app.travelplanner.name}.azurewebsites.net"
}

output "resource_group_name" {
  description = "Name of the resource group"
  value       = azurerm_resource_group.travelplanner.name
}

output "webapp_name" {
  description = "Name of the web app"
  value       = azurerm_linux_web_app.travelplanner.name
}