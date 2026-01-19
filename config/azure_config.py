"""
Azure Web App Configuration for Karnataka Travel Planner
"""

import os
from pathlib import Path

# Azure Web App Configuration
class AzureConfig:
    """Configuration settings for Azure Web App deployment"""
    
    # App Service Configuration
    APP_NAME = "karnataka-travel-planner"
    RESOURCE_GROUP = "travel-planner-rg"
    LOCATION = "Central India"  # or "South India"
    
    # Runtime Configuration
    PYTHON_VERSION = "3.11"
    STARTUP_COMMAND = "python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0"
    
    # Environment Variables
    ENVIRONMENT_VARIABLES = {
        "STREAMLIT_SERVER_PORT": "8000",
        "STREAMLIT_SERVER_ADDRESS": "0.0.0.0",
        "STREAMLIT_SERVER_HEADLESS": "true",
        "STREAMLIT_BROWSER_GATHER_USAGE_STATS": "false",
        "STREAMLIT_SERVER_ENABLE_CORS": "false"
    }
    
    # App Settings for Azure
    APP_SETTINGS = {
        "SCM_DO_BUILD_DURING_DEPLOYMENT": "true",
        "ENABLE_ORYX_BUILD": "true",
        "POST_BUILD_SCRIPT_PATH": "deployment/post_build.sh"
    }
    
    # Database Configuration (if needed)
    DATABASE_CONFIG = {
        "use_database": False,  # Set to True if you want to use Azure SQL/CosmosDB
        "connection_string": os.getenv("DATABASE_CONNECTION_STRING", ""),
        "database_name": "travel_planner_db"
    }
    
    # Storage Configuration
    STORAGE_CONFIG = {
        "use_blob_storage": False,  # Set to True for file uploads
        "storage_account": os.getenv("AZURE_STORAGE_ACCOUNT", ""),
        "storage_key": os.getenv("AZURE_STORAGE_KEY", ""),
        "container_name": "travel-images"
    }
    
    # Application Insights (Optional)
    MONITORING_CONFIG = {
        "enable_app_insights": True,
        "instrumentation_key": os.getenv("APPINSIGHTS_INSTRUMENTATION_KEY", ""),
        "connection_string": os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING", "")
    }
    
    # Security Configuration
    SECURITY_CONFIG = {
        "enable_https_redirect": True,
        "enable_auth": False,  # Set to True for Azure AD authentication
        "allowed_origins": ["*"],  # Configure for production
        "session_timeout": 3600  # 1 hour
    }
    
    # Performance Configuration
    PERFORMANCE_CONFIG = {
        "enable_caching": True,
        "cache_ttl": 300,  # 5 minutes
        "max_upload_size": "10MB",
        "enable_compression": True
    }

# Deployment Configuration
DEPLOYMENT_CONFIG = {
    "build_command": "pip install -r requirements.txt",
    "startup_command": AzureConfig.STARTUP_COMMAND,
    "health_check_path": "/",
    "scale_settings": {
        "min_instances": 1,
        "max_instances": 5,
        "scale_out_cpu_threshold": 70,
        "scale_in_cpu_threshold": 30
    }
}

# Azure CLI Deployment Commands
AZURE_CLI_COMMANDS = {
    "create_resource_group": f"az group create --name {AzureConfig.RESOURCE_GROUP} --location '{AzureConfig.LOCATION}'",
    
    "create_app_service_plan": f"""az appservice plan create 
        --name {AzureConfig.APP_NAME}-plan 
        --resource-group {AzureConfig.RESOURCE_GROUP} 
        --sku B1 
        --is-linux""",
    
    "create_web_app": f"""az webapp create 
        --resource-group {AzureConfig.RESOURCE_GROUP} 
        --plan {AzureConfig.APP_NAME}-plan 
        --name {AzureConfig.APP_NAME} 
        --runtime "PYTHON|{AzureConfig.PYTHON_VERSION}" 
        --deployment-local-git""",
    
    "configure_app_settings": f"""az webapp config appsettings set 
        --resource-group {AzureConfig.RESOURCE_GROUP} 
        --name {AzureConfig.APP_NAME} 
        --settings {' '.join([f'{k}={v}' for k, v in AzureConfig.ENVIRONMENT_VARIABLES.items()])}""",
    
    "set_startup_command": f"""az webapp config set 
        --resource-group {AzureConfig.RESOURCE_GROUP} 
        --name {AzureConfig.APP_NAME} 
        --startup-file "{AzureConfig.STARTUP_COMMAND}" """,
    
    "deploy_code": f"""az webapp deployment source config-local-git 
        --name {AzureConfig.APP_NAME} 
        --resource-group {AzureConfig.RESOURCE_GROUP}"""
}

# Environment-specific configurations
class DevelopmentConfig(AzureConfig):
    """Development environment configuration"""
    DEBUG = True
    TESTING = False
    
class ProductionConfig(AzureConfig):
    """Production environment configuration"""
    DEBUG = False
    TESTING = False
    
    # Override security settings for production
    SECURITY_CONFIG = {
        **AzureConfig.SECURITY_CONFIG,
        "allowed_origins": ["https://karnataka-travel-planner.azurewebsites.net"],
        "enable_auth": True
    }

# Configuration factory
def get_config(environment="development"):
    """Get configuration based on environment"""
    configs = {
        "development": DevelopmentConfig,
        "production": ProductionConfig
    }
    return configs.get(environment, DevelopmentConfig)