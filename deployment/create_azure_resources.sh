#!/bin/bash

# Azure Resource Creation Script for Karnataka Travel Planner
# Creates all necessary resources for vintekh.com deployment

echo "🚀 Creating Azure resources for Karnataka Travel Planner..."

# Variables
RESOURCE_GROUP="TravelPlanner"
WEBAPP_NAME="vintekh"
APP_SERVICE_PLAN="vintekh-plan"
LOCATION="Central India"
SKU="B1"  # Basic tier - can upgrade later
RUNTIME="PYTHON|3.11"

# Create Resource Group
echo "📦 Creating resource group: $RESOURCE_GROUP"
az group create \
    --name $RESOURCE_GROUP \
    --location "$LOCATION"

if [ $? -eq 0 ]; then
    echo "✅ Resource group created successfully"
else
    echo "❌ Failed to create resource group"
    exit 1
fi

# Create App Service Plan
echo "📋 Creating App Service Plan: $APP_SERVICE_PLAN"
az appservice plan create \
    --name $APP_SERVICE_PLAN \
    --resource-group $RESOURCE_GROUP \
    --location "$LOCATION" \
    --sku $SKU \
    --is-linux

if [ $? -eq 0 ]; then
    echo "✅ App Service Plan created successfully"
else
    echo "❌ Failed to create App Service Plan"
    exit 1
fi

# Create Web App
echo "🌐 Creating Web App: $WEBAPP_NAME"
az webapp create \
    --resource-group $RESOURCE_GROUP \
    --plan $APP_SERVICE_PLAN \
    --name $WEBAPP_NAME \
    --runtime "$RUNTIME" \
    --deployment-local-git

if [ $? -eq 0 ]; then
    echo "✅ Web App created successfully"
else
    echo "❌ Failed to create Web App"
    exit 1
fi

# Configure App Settings for Streamlit
echo "⚙️ Configuring app settings..."
az webapp config appsettings set \
    --resource-group $RESOURCE_GROUP \
    --name $WEBAPP_NAME \
    --settings \
        STREAMLIT_SERVER_PORT=8000 \
        STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
        STREAMLIT_SERVER_HEADLESS=true \
        STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
        STREAMLIT_SERVER_ENABLE_CORS=false \
        SCM_DO_BUILD_DURING_DEPLOYMENT=true \
        ENABLE_ORYX_BUILD=true \
        WEBSITES_PORT=8000

if [ $? -eq 0 ]; then
    echo "✅ App settings configured successfully"
else
    echo "❌ Failed to configure app settings"
    exit 1
fi

# Set startup command
echo "🚀 Setting startup command..."
az webapp config set \
    --resource-group $RESOURCE_GROUP \
    --name $WEBAPP_NAME \
    --startup-file "python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0 --server.headless=true"

if [ $? -eq 0 ]; then
    echo "✅ Startup command set successfully"
else
    echo "❌ Failed to set startup command"
    exit 1
fi

# Enable logging
echo "📝 Enabling application logging..."
az webapp log config \
    --resource-group $RESOURCE_GROUP \
    --name $WEBAPP_NAME \
    --application-logging filesystem \
    --level information

# Get deployment URL
WEBAPP_URL="https://$WEBAPP_NAME.azurewebsites.net"

echo ""
echo "🎉 Azure resources created successfully!"
echo "=================================="
echo "Resource Group: $RESOURCE_GROUP"
echo "Web App Name: $WEBAPP_NAME"
echo "App Service Plan: $APP_SERVICE_PLAN"
echo "Web App URL: $WEBAPP_URL"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Set up GitHub Actions deployment"
echo "2. Push your code to trigger deployment"
echo "3. Configure custom domain vintekh.com (optional)"
echo ""
echo "To configure custom domain later:"
echo "az webapp config hostname add --webapp-name $WEBAPP_NAME --resource-group $RESOURCE_GROUP --hostname vintekh.com"