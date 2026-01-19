"""
Fix import issues for Karnataka Travel Planner
Run this if you encounter import errors
"""

import os
import sys

def fix_import_paths():
    """Add current directory to Python path"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    print(f"✅ Added {current_dir} to Python path")

def create_init_files():
    """Create __init__.py files for proper package structure"""
    
    directories = [
        'data',
        'components', 
        'services',
        'pages',
        'utils',
        'config'
    ]
    
    for directory in directories:
        if os.path.exists(directory):
            init_file = os.path.join(directory, '__init__.py')
            if not os.path.exists(init_file):
                with open(init_file, 'w') as f:
                    f.write(f'"""Package: {directory}"""\n')
                print(f"✅ Created {init_file}")
            else:
                print(f"✅ {init_file} already exists")
        else:
            print(f"⚠️  Directory {directory} not found")

def fix_relative_imports():
    """Fix relative import issues in files"""
    
    # Fix services/photo_service.py if it has import issues
    photo_service_path = 'services/photo_service.py'
    if os.path.exists(photo_service_path):
        with open(photo_service_path, 'r') as f:
            content = f.read()
        
        # Add try-except for streamlit secrets
        if 'st.secrets.get' in content and 'try:' not in content:
            fixed_content = content.replace(
                'self.unsplash_access_key = st.secrets.get("UNSPLASH_ACCESS_KEY", "")',
                '''try:
            self.unsplash_access_key = st.secrets.get("UNSPLASH_ACCESS_KEY", "")
        except:
            self.unsplash_access_key = ""'''
            )
            
            fixed_content = fixed_content.replace(
                'self.pexels_api_key = st.secrets.get("PEXELS_API_KEY", "")',
                '''try:
            self.pexels_api_key = st.secrets.get("PEXELS_API_KEY", "")
        except:
            self.pexels_api_key = ""'''
            )
            
            with open(photo_service_path, 'w') as f:
                f.write(fixed_content)
            
            print(f"✅ Fixed secrets handling in {photo_service_path}")

def create_streamlit_config():
    """Create Streamlit config if it doesn't exist"""
    
    streamlit_dir = '.streamlit'
    config_file = os.path.join(streamlit_dir, 'config.toml')
    
    if not os.path.exists(streamlit_dir):
        os.makedirs(streamlit_dir)
        print(f"✅ Created {streamlit_dir} directory")
    
    if not os.path.exists(config_file):
        config_content = '''[global]
developmentMode = false

[server]
headless = true
enableCORS = false
enableXsrfProtection = true
maxUploadSize = 200

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#FF6B35"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
'''
        
        with open(config_file, 'w') as f:
            f.write(config_content)
        
        print(f"✅ Created {config_file}")

def main():
    """Run all fixes"""
    print("🔧 Fixing import and configuration issues...\n")
    
    fix_import_paths()
    create_init_files()
    fix_relative_imports()
    create_streamlit_config()
    
    print("\n✅ All fixes applied!")
    print("\nNow try running:")
    print("python test_app.py")
    print("streamlit run app.py")

if __name__ == "__main__":
    main()