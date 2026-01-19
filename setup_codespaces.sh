#!/bin/bash

# Setup script for GitHub Codespaces
# Handles Python 3.12 compatibility issues

echo "🚀 Setting up Karnataka Travel Planner in GitHub Codespaces..."

# Update system packages
echo "📦 Updating system packages..."
sudo apt-get update -qq

# Upgrade pip and setuptools
echo "🔧 Upgrading pip and setuptools..."
python -m pip install --upgrade pip setuptools wheel --quiet

# Install dependencies individually to handle any failures gracefully
echo "📚 Installing Python dependencies..."

dependencies=(
    "streamlit==1.28.1"
    "pandas==2.1.3" 
    "folium==0.15.0"
    "streamlit-folium==0.15.0"
    "plotly==5.17.0"
    "requests==2.31.0"
    "Pillow==10.1.0"
    "numpy==1.24.3"
    "python-dateutil==2.8.2"
)

for dep in "${dependencies[@]}"; do
    echo "Installing $dep..."
    pip install "$dep" --quiet || {
        echo "⚠️  Failed to install $dep, trying alternative method..."
        pip install --user "$dep" --quiet || {
            echo "❌ Could not install $dep"
        }
    }
done

# Fix import paths
echo "🔧 Fixing import paths..."
python fix_imports.py

# Run tests
echo "🧪 Running tests..."
python test_app.py

echo "✅ Setup complete! Now run:"
echo "streamlit run app.py --server.port 8000 --server.address 0.0.0.0"