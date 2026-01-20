#!/bin/bash

# Production startup script for Karnataka Travel Planner
echo "🚀 Starting Karnataka Travel Planner..."

# Set environment variables for Streamlit
export STREAMLIT_SERVER_PORT=${PORT:-8000}
export STREAMLIT_SERVER_ADDRESS="0.0.0.0"
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
export STREAMLIT_SERVER_ENABLE_CORS=false

# Create necessary directories
mkdir -p /tmp/streamlit
mkdir -p ~/.streamlit

# Create empty secrets.toml file to prevent Streamlit warnings
# The app uses environment variables as fallback for API keys
touch ~/.streamlit/secrets.toml

# Optional: Create basic config.toml for Streamlit
cat > ~/.streamlit/config.toml << EOF
[server]
headless = true
port = ${PORT:-8000}
address = "0.0.0.0"
enableCORS = false

[browser]
gatherUsageStats = false
EOF

# Start the application
echo "🌐 Starting Streamlit on port $STREAMLIT_SERVER_PORT..."
python -m streamlit run app.py \
    --server.port=$STREAMLIT_SERVER_PORT \
    --server.address=$STREAMLIT_SERVER_ADDRESS \
    --server.headless=$STREAMLIT_SERVER_HEADLESS \
    --browser.gatherUsageStats=$STREAMLIT_BROWSER_GATHER_USAGE_STATS \
    --server.enableCORS=$STREAMLIT_SERVER_ENABLE_CORS