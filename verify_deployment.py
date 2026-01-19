#!/usr/bin/env python3
"""
Deployment verification script for Karnataka Travel Planner
Run this before deploying to ensure everything is ready
"""

import sys
import importlib
import os

def check_required_files():
    """Check if all required files exist"""
    print("📁 Checking required files...")
    
    required_files = [
        'app.py',
        'requirements.txt', 
        'startup.sh',
        'README.md',
        '.streamlit/config.toml',
        '.github/workflows/azure-deploy.yml',
        'deployment/create_azure_resources.sh'
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            missing_files.append(file_path)
    
    return len(missing_files) == 0

def check_imports():
    """Check if all required modules can be imported"""
    print("\n📦 Checking Python dependencies...")
    
    required_modules = [
        'streamlit',
        'pandas',
        'folium', 
        'streamlit_folium',
        'plotly',
        'requests',
        'PIL'
    ]
    
    missing_modules = []
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"❌ {module}")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n⚠️  Install missing modules: pip install {' '.join(missing_modules)}")
        return False
    
    return True

def check_app_structure():
    """Check application structure"""
    print("\n🏗️  Checking app structure...")
    
    try:
        # Test main app import
        sys.path.insert(0, '.')
        import app
        print("✅ app.py imports successfully")
        
        # Check if main function exists
        if hasattr(app, 'main'):
            print("✅ main() function found")
        else:
            print("❌ main() function missing")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ App structure error: {e}")
        return False

def check_azure_config():
    """Check Azure deployment configuration"""
    print("\n☁️  Checking Azure configuration...")
    
    # Check GitHub Actions workflow
    workflow_file = '.github/workflows/azure-deploy.yml'
    if os.path.exists(workflow_file):
        with open(workflow_file, 'r') as f:
            content = f.read()
            if 'vintekh' in content:
                print("✅ GitHub Actions configured for vintekh")
            else:
                print("⚠️  Check webapp name in GitHub Actions")
    
    # Check deployment script
    deploy_script = 'deployment/create_azure_resources.sh'
    if os.path.exists(deploy_script):
        try:
            with open(deploy_script, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'TravelPlanner' in content and 'vintekh' in content:
                    print("✅ Deployment script configured correctly")
                else:
                    print("⚠️  Check resource group and webapp name in deployment script")
        except UnicodeDecodeError:
            print("⚠️  Deployment script has encoding issues, but exists")
    
    return True

def main():
    """Run all verification checks"""
    print("🚀 Karnataka Travel Planner - Deployment Verification\n")
    
    checks = [
        check_required_files,
        check_imports,
        check_app_structure, 
        check_azure_config
    ]
    
    results = []
    for check in checks:
        results.append(check())
    
    print("\n" + "="*60)
    
    if all(results):
        print("🎉 All checks passed! Ready for deployment.")
        print("\nNext steps:")
        print("1. Run: ./deployment/create_azure_resources.sh")
        print("2. Add AZURE_WEBAPP_PUBLISH_PROFILE to GitHub secrets")
        print("3. Push to main branch to deploy")
        print("4. Access at: https://vintekh.azurewebsites.net")
    else:
        print("⚠️  Some checks failed. Fix issues before deployment.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)