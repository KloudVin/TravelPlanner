#!/bin/bash

# Azure Web App Startup Script for Karnataka Travel Planner
echo "Starting Karnataka Travel Planner..."

# Set environment variables
export STREAMLIT_SERVER_PORT=${PORT:-8000}
export STREAMLIT_SERVER_ADDRESS="0.0.0.0"
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Create necessary directories
mkdir -p /tmp/streamlit
mkdir -p logs

# Install any additional dependencies if needed
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Set up logging
echo "Setting up logging..."
export STREAMLIT_LOGGER_LEVEL=INFO

# Health check endpoint setup
echo "Setting up health monitoring..."

# Start the Streamlit application
echo "Starting Streamlit application on port $STREAMLIT_SERVER_PORT..."
python -m streamlit run app.py \
    --server.port=$STREAMLIT_SERVER_PORT \
    --server.address=$STREAMLIT_SERVER_ADDRESS \
    --server.headless=$STREAMLIT_SERVER_HEADLESS \
    --browser.gatherUsageStats=$STREAMLIT_BROWSER_GATHER_USAGE_STATS \
    --server.enableCORS=false \
    --server.enableXsrfProtection=true