#!/bin/bash

# Script to get Azure Web App publish profile for GitHub Actions

RESOURCE_GROUP="TravelPlanner"
WEBAPP_NAME="vintekh"

echo "🔑 Getting publish profile for GitHub Actions..."

# Get the publish profile
az webapp deployment list-publishing-profiles \
    --resource-group $RESOURCE_GROUP \
    --name $WEBAPP_NAME \
    --xml

echo ""
echo "📋 Instructions:"
echo "1. Copy the entire XML output above"
echo "2. Go to your GitHub repository"
echo "3. Navigate to Settings > Secrets and variables > Actions"
echo "4. Click 'New repository secret'"
echo "5. Name: AZURE_WEBAPP_PUBLISH_PROFILE"
echo "6. Value: Paste the XML content"
echo "7. Click 'Add secret'"
echo ""
echo "After adding the secret, push to main branch to trigger deployment!"