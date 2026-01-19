"""
Test script to validate Karnataka Travel Planner before deployment
Run this to check for common issues
"""

import sys
import importlib
import traceback

def test_imports():
    """Test all imports to ensure no missing dependencies"""
    print("🧪 Testing imports...")
    
    required_modules = [
        'streamlit',
        'pandas', 
        'folium',
        'streamlit_folium',
        'plotly.express',
        'plotly.graph_objects',
        'requests',
        'PIL'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module} - {e}")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n⚠️  Missing modules: {missing_modules}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All required modules available")
    return True

def test_data_files():
    """Test if all data files can be imported"""
    print("\n🗂️  Testing data files...")
    
    try:
        from data.destinations import DAY_TRIP_DESTINATIONS, MULTI_DAY_DESTINATIONS
        print(f"✅ destinations.py - {len(DAY_TRIP_DESTINATIONS)} day trips, {len(MULTI_DAY_DESTINATIONS)} multi-day")
        
        from data.bangalore_direction_itineraries import BANGALORE_DIRECTION_ITINERARIES
        print(f"✅ bangalore_direction_itineraries.py - {len(BANGALORE_DIRECTION_ITINERARIES)} directions")
        
        from data.karnataka_hidden_gems import KARNATAKA_HIDDEN_GEMS
        print(f"✅ karnataka_hidden_gems.py - {len(KARNATAKA_HIDDEN_GEMS)} regions")
        
        return True
        
    except Exception as e:
        print(f"❌ Data file error: {e}")
        traceback.print_exc()
        return False

def test_components():
    """Test if components can be imported"""
    print("\n🧩 Testing components...")
    
    try:
        from components.multimedia import multimedia_manager
        print("✅ multimedia.py")
        
        from services.photo_service import get_curated_photos
        print("✅ photo_service.py")
        
        from pages.direction_itineraries import show_itinerary_pages
        print("✅ direction_itineraries.py")
        
        return True
        
    except Exception as e:
        print(f"❌ Component error: {e}")
        traceback.print_exc()
        return False

def test_app_structure():
    """Test main app structure"""
    print("\n🏗️  Testing app structure...")
    
    try:
        import app
        print("✅ app.py imports successfully")
        
        # Check if main function exists
        if hasattr(app, 'main'):
            print("✅ main() function found")
        else:
            print("❌ main() function not found")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ App structure error: {e}")
        traceback.print_exc()
        return False

def test_secrets_config():
    """Test secrets configuration"""
    print("\n🔐 Testing secrets configuration...")
    
    try:
        import streamlit as st
        
        # Test if secrets file exists and is accessible
        secrets_keys = ['UNSPLASH_ACCESS_KEY', 'PEXELS_API_KEY', 'YOUTUBE_API_KEY']
        
        for key in secrets_keys:
            value = st.secrets.get(key, "")
            if value and value != "your_" + key.lower() + "_here":
                print(f"✅ {key} configured")
            else:
                print(f"⚠️  {key} not configured (will use placeholders)")
        
        return True
        
    except Exception as e:
        print(f"⚠️  Secrets not accessible: {e}")
        print("This is normal for local testing - app will use placeholder images")
        return True

def run_all_tests():
    """Run all tests"""
    print("🚀 Karnataka Travel Planner - Pre-deployment Tests\n")
    
    tests = [
        test_imports,
        test_data_files, 
        test_components,
        test_app_structure,
        test_secrets_config
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "="*50)
    
    if all(results):
        print("🎉 All tests passed! Ready for deployment.")
        print("\nTo run locally:")
        print("streamlit run app.py")
        print("\nTo deploy to Azure:")
        print("Follow the deployment guide in README.md")
    else:
        print("⚠️  Some tests failed. Please fix issues before deployment.")
        print("Check the error messages above for details.")
    
    return all(results)

if __name__ == "__main__":
    run_all_tests()