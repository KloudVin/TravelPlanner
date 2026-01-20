import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import sys
import os

# Add current directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import our comprehensive data and components
try:
    from data.destinations import (
        DAY_TRIP_DESTINATIONS, MULTI_DAY_DESTINATIONS, TOUR_PACKAGES,
        KARNATAKA_WATERFALLS, KARNATAKA_HERITAGE_SITES, KARNATAKA_BEACHES
    )
    from components.multimedia import multimedia_manager
    from pages.direction_itineraries import show_itinerary_pages
except ImportError as e:
    st.error(f"Import error: {e}")
    st.info("Some features may be limited due to missing dependencies.")
    # Create minimal fallback data
    DAY_TRIP_DESTINATIONS = []
    MULTI_DAY_DESTINATIONS = []
    KARNATAKA_WATERFALLS = []
    KARNATAKA_HERITAGE_SITES = []
    KARNATAKA_BEACHES = []

# Page configuration
st.set_page_config(
    page_title="Karnataka Travel Planner",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B35;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .video-banner {
        width: 100%;
        height: 400px;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    .trip-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    .trip-card:hover {
        transform: translateY(-5px);
    }
    .feature-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #FF6B35;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .theme-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .theme-card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    .package-builder {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 2rem 0;
    }
    .stButton>button {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255,107,53,0.4);
    }
</style>
""", unsafe_allow_html=True)

def show_custom_package_builder():
    """Interactive Custom Package Builder"""
    st.markdown('<h1 class="main-header">🎯 Custom Package Builder</h1>', unsafe_allow_html=True)
    st.markdown("### Create your perfect Karnataka adventure tailored to your preferences!")
    
    # Initialize session state for package building
    if 'custom_package' not in st.session_state:
        st.session_state.custom_package = {
            'theme': None,
            'districts': [],
            'duration': None,
            'budget': None,
            'destinations': [],
            'activities': []
        }
    
    # Step 1: Theme Selection
    st.markdown("""
    <div class="package-builder">
        <h3>🎨 Step 1: Choose Your Adventure Theme</h3>
        <p>Select the type of experience you're looking for</p>
    </div>
    """, unsafe_allow_html=True)
    
    themes = {
        "🏖️ Beach Paradise": {
            "description": "Relaxing coastal getaways with pristine beaches",
            "districts": ["Udupi", "Mangalore", "Karwar", "Uttara Kannada"],
            "activities": ["Beach relaxation", "Water sports", "Seafood cuisine", "Sunset views"]
        },
        "🏛️ Temple Trails": {
            "description": "Spiritual journey through ancient temples and heritage sites",
            "districts": ["Belagavi", "Dharwad", "Haveri", "Gadag", "Bagalkot"],
            "activities": ["Temple visits", "Religious ceremonies", "Cultural performances", "Meditation"]
        },
        "💕 Honeymoon": {
            "description": "Romantic escapes with scenic beauty and luxury experiences",
            "districts": ["Kodagu", "Chikmagalur", "Hassan", "Mysore"],
            "activities": ["Candlelight dinners", "Spa treatments", "Photography", "Nature walks"]
        },
        "🏔️ Adventure": {
            "description": "Thrilling experiences with trekking, wildlife, and outdoor activities",
            "districts": ["Chikmagalur", "Kodagu", "Uttara Kannada", "Shimoga"],
            "activities": ["Trekking", "River rafting", "Wildlife safari", "Paragliding"]
        },
        "🍽️ Food & Culture": {
            "description": "Culinary journey exploring Karnataka's diverse cuisine and traditions",
            "districts": ["Mysore", "Bangalore", "Mangalore", "Hubli"],
            "activities": ["Local cuisine tasting", "Cooking classes", "Market visits", "Cultural shows"]
        },
        "📸 Photography": {
            "description": "Capture stunning landscapes and architectural marvels",
            "districts": ["Mysore", "Hampi", "Badami", "Gulbarga"],
            "activities": ["Landscape photography", "Sunrise/sunset shoots", "Architecture", "Nature"]
        },
        "👨‍👩‍👧‍👦 Family": {
            "description": "Fun-filled family vacations with educational and recreational activities",
            "districts": ["Bangalore", "Mysore", "Ooty", "Chikmagalur"],
            "activities": ["Family picnics", "Educational tours", "Amusement parks", "Nature walks"]
        },
        "🧘 Spiritual": {
            "description": "Peaceful retreats for meditation, yoga, and spiritual awakening",
            "districts": ["Shimoga", "Chikmagalur", "Udupi", "Dharwad"],
            "activities": ["Yoga sessions", "Meditation", "Temple visits", "Nature retreats"]
        }
    }
    
    cols = st.columns(4)
    selected_theme = None
    
    for idx, (theme_name, theme_data) in enumerate(themes.items()):
        with cols[idx % 4]:
            with st.container():
                if st.button(theme_name, key=f"builder_theme_{idx}", use_container_width=True):
                    selected_theme = theme_name
                    st.session_state.custom_package['theme'] = theme_name
                
                st.caption(theme_data['description'])
    
    # Step 2: District Selection (only show if theme is selected)
    if st.session_state.custom_package['theme']:
        selected_theme_data = themes[st.session_state.custom_package['theme']]
        
        st.markdown("""
        <div class="package-builder">
            <h3>📍 Step 2: Select Districts</h3>
            <p>Choose the regions you want to explore</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info(f"🎯 **Selected Theme:** {st.session_state.custom_package['theme']}")
        st.write(f"**Available Districts:** {', '.join(selected_theme_data['districts'])}")
        
        # District selection
        selected_districts = st.multiselect(
            "Choose districts to include in your package:",
            selected_theme_data['districts'],
            key="district_selector"
        )
        
        if selected_districts:
            st.session_state.custom_package['districts'] = selected_districts
            
            # Step 3: Duration and Budget
            st.markdown("""
            <div class="package-builder">
                <h3>⏰ Step 3: Trip Details</h3>
                <p>Set your travel duration and budget preferences</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                duration = st.selectbox(
                    "Trip Duration:",
                    ["2-3 Days", "4-5 Days", "6-7 Days", "8-10 Days", "11+ Days"],
                    key="duration_selector"
                )
            
            with col2:
                budget = st.selectbox(
                    "Budget Range:",
                    ["Budget (< ₹10K)", "Mid-range (₹10K-25K)", "Premium (₹25K-50K)", "Luxury (> ₹50K)"],
                    key="budget_selector"
                )
            
            st.session_state.custom_package['duration'] = duration
            st.session_state.custom_package['budget'] = budget
            
            # Step 4: Generate Package
            st.markdown("""
            <div class="package-builder">
                <h3>🎉 Step 4: Generate Your Custom Package</h3>
                <p>Review your selections and create your personalized itinerary</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display package summary
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 📋 Package Summary")
                st.write(f"**Theme:** {st.session_state.custom_package['theme']}")
                st.write(f"**Districts:** {', '.join(selected_districts)}")
                st.write(f"**Duration:** {duration}")
                st.write(f"**Budget:** {budget}")
            
            with col2:
                st.markdown("### 🎯 Recommended Activities")
                for activity in selected_theme_data['activities'][:4]:  # Show top 4
                    st.write(f"• {activity}")
            
            if st.button("🚀 Generate My Custom Package", type="primary", use_container_width=True):
                generate_custom_package(st.session_state.custom_package, selected_theme_data)
    
    # Reset button
    if st.button("🔄 Start Over", help="Clear all selections and start fresh"):
        st.session_state.custom_package = {
            'theme': None,
            'districts': [],
            'duration': None,
            'budget': None,
            'destinations': [],
            'activities': []
        }
        st.rerun()

def generate_custom_package(package_data, theme_data):
    """Generate and display custom package based on user selections"""
    st.success("🎉 Your custom package has been generated!")
    
    # Mock destination data based on theme and districts
    mock_destinations = {
        "🏖️ Beach Paradise": [
            {"name": "Maravanthe Beach", "district": "Udupi", "type": "Beach", "rating": 4.5, "hidden_gem": False},
            {"name": "Malpe Beach", "district": "Udupi", "type": "Beach", "rating": 4.2, "hidden_gem": False},
            {"name": "Tannirbhavi Beach", "district": "Mangalore", "type": "Beach", "rating": 4.3, "hidden_gem": False},
            {"name": "Kadike Beach", "district": "Udupi", "type": "Beach", "rating": 4.1, "hidden_gem": True},
            {"name": "Nethrani Island", "district": "Udupi", "type": "Island", "rating": 4.4, "hidden_gem": True}
        ],
        "🏛️ Temple Trails": [
            {"name": "Badami Caves", "district": "Bagalkot", "type": "Heritage", "rating": 4.7, "hidden_gem": False},
            {"name": "Pattadakal", "district": "Bagalkot", "type": "Temple", "rating": 4.6, "hidden_gem": False},
            {"name": "Aihole", "district": "Bagalkot", "type": "Heritage", "rating": 4.4, "hidden_gem": False},
            {"name": "Mahakuta Temple", "district": "Bagalkot", "type": "Temple", "rating": 4.3, "hidden_gem": True},
            {"name": "Banashankari Temple", "district": "Bagalkot", "type": "Temple", "rating": 4.2, "hidden_gem": True}
        ],
        "💕 Honeymoon": [
            {"name": "Mysore Palace", "district": "Mysore", "type": "Palace", "rating": 4.8, "hidden_gem": False},
            {"name": "Coorg Hills", "district": "Kodagu", "type": "Hill Station", "rating": 4.6, "hidden_gem": False},
            {"name": "Kabini Wildlife", "district": "Mysore", "type": "Wildlife", "rating": 4.5, "hidden_gem": False},
            {"name": "Dubare Elephant Camp", "district": "Kodagu", "type": "Wildlife", "rating": 4.4, "hidden_gem": True},
            {"name": "Abbey Falls", "district": "Kodagu", "type": "Waterfall", "rating": 4.3, "hidden_gem": True}
        ],
        "🏔️ Adventure": [
            {"name": "Mullayanagiri", "district": "Chikmagalur", "type": "Trekking", "rating": 4.4, "hidden_gem": False},
            {"name": "Kumara Parvatha", "district": "Kodagu", "type": "Trekking", "rating": 4.7, "hidden_gem": False},
            {"name": "Dandeli Wildlife", "district": "Uttara Kannada", "type": "Adventure", "rating": 4.3, "hidden_gem": False},
            {"name": "Magod Falls", "district": "Uttara Kannada", "type": "Waterfall", "rating": 4.2, "hidden_gem": True},
            {"name": "Unchalli Falls", "district": "Uttara Kannada", "type": "Waterfall", "rating": 4.1, "hidden_gem": True}
        ],
        "🍽️ Food & Culture": [
            {"name": "Mysore Market", "district": "Mysore", "type": "Market", "rating": 4.3, "hidden_gem": False},
            {"name": "Mangalore Food Street", "district": "Mangalore", "type": "Cuisine", "rating": 4.4, "hidden_gem": False},
            {"name": "Bengaluru Food Scene", "district": "Bangalore", "type": "Cuisine", "rating": 4.5, "hidden_gem": False},
            {"name": "Udupi Krishna Temple Food", "district": "Udupi", "type": "Temple Food", "rating": 4.2, "hidden_gem": True},
            {"name": "Coorg Spice Plantations", "district": "Kodagu", "type": "Cuisine", "rating": 4.1, "hidden_gem": True}
        ],
        "📸 Photography": [
            {"name": "Hampi Ruins", "district": "Bellary", "type": "Heritage", "rating": 4.8, "hidden_gem": False},
            {"name": "Mysore Palace", "district": "Mysore", "type": "Palace", "rating": 4.7, "hidden_gem": False},
            {"name": "Coorg Sunrise", "district": "Kodagu", "type": "Nature", "rating": 4.5, "hidden_gem": False},
            {"name": "Chikmagalur Coffee Estates", "district": "Chikmagalur", "type": "Plantation", "rating": 4.3, "hidden_gem": True},
            {"name": "Badami Rock Formations", "district": "Bagalkot", "type": "Nature", "rating": 4.2, "hidden_gem": True}
        ],
        "👨‍👩‍👧‍👦 Family": [
            {"name": "Mysore Zoo", "district": "Mysore", "type": "Zoo", "rating": 4.2, "hidden_gem": False},
            {"name": "Bannerghatta Zoo", "district": "Bangalore", "type": "Zoo", "rating": 4.3, "hidden_gem": False},
            {"name": "Wonderla Amusement Park", "district": "Bangalore", "type": "Amusement", "rating": 4.4, "hidden_gem": False},
            {"name": "Ranganathittu Bird Sanctuary", "district": "Mandya", "type": "Wildlife", "rating": 4.1, "hidden_gem": True},
            {"name": "Gokarna Beach Family Area", "district": "Uttara Kannada", "type": "Beach", "rating": 4.0, "hidden_gem": True}
        ],
        "🧘 Spiritual": [
            {"name": "Udupi Krishna Temple", "district": "Udupi", "type": "Temple", "rating": 4.6, "hidden_gem": False},
            {"name": "Sringeri Sharada Temple", "district": "Chikmagalur", "type": "Temple", "rating": 4.5, "hidden_gem": False},
            {"name": "Dharmasthala Temple", "district": "Dakshina Kannada", "type": "Temple", "rating": 4.4, "hidden_gem": False},
            {"name": "Kateel Durga Parameshwari Temple", "district": "Mangalore", "type": "Temple", "rating": 4.2, "hidden_gem": True},
            {"name": "Kukke Subramanya Temple", "district": "Dakshina Kannada", "type": "Temple", "rating": 4.3, "hidden_gem": True}
        ]
    }
    
    theme_name = package_data['theme']
    selected_districts = package_data['districts']
    
    # Get destinations for selected theme
    available_destinations = mock_destinations.get(theme_name, [])
    
    # Filter by selected districts
    filtered_destinations = [
        dest for dest in available_destinations 
        if dest['district'] in selected_districts
    ]
    
    # Display package details
    st.markdown("### 📋 Your Custom Package Details")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Theme", theme_name.split()[1])
    with col2:
        st.metric("Duration", package_data['duration'])
    with col3:
        st.metric("Destinations", len(filtered_destinations))
    
    # Display destinations
    st.markdown("### 🏛️ Recommended Destinations")
    
    # Add filter for hidden gems
    show_hidden_gems = st.checkbox("💎 Include Hidden Gems", value=True, help="Show lesser-known but amazing destinations")
    
    if show_hidden_gems:
        display_destinations = filtered_destinations
    else:
        display_destinations = [dest for dest in filtered_destinations if not dest.get('hidden_gem', False)]
    
    if display_destinations:
        # Group destinations by type
        popular_destinations = [dest for dest in display_destinations if not dest.get('hidden_gem', False)]
        hidden_gems = [dest for dest in display_destinations if dest.get('hidden_gem', False)]
        
        if popular_destinations:
            st.markdown("#### 🌟 Popular Destinations")
            for dest in popular_destinations:
                with st.expander(f"⭐ {dest['name']} ({dest['district']}) - Rating: {dest['rating']}/5"):
                    display_destination_card(dest)
        
        if hidden_gems and show_hidden_gems:
            st.markdown("#### 💎 Hidden Gems")
            for dest in hidden_gems:
                with st.expander(f"💎 {dest['name']} ({dest['district']}) - Rating: {dest['rating']}/5"):
                    display_destination_card(dest)
    else:
        st.warning("No destinations found for selected districts. Try selecting different districts or contact us for custom recommendations.")

def display_destination_card(destination):
    """Display an attractive destination card"""
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Placeholder image - replace with actual destination images
        image_url = f"https://via.placeholder.com/300x200/FF6B35/FFFFFF?text={destination['name'].replace(' ', '+')}"
        st.image(image_url, caption=destination['name'], use_container_width=True)
    
    with col2:
        st.markdown(f"**🏷️ Type:** {destination['type']}")
        st.markdown(f"**📍 District:** {destination['district']}")
        st.markdown(f"**⭐ Rating:** {destination['rating']}/5")
        
        if destination.get('hidden_gem'):
            st.markdown("**💎 Hidden Gem:** Yes - Lesser known but amazing!")
        
        st.markdown("**✨ Highlights:**")
        highlights = [
            "- Stunning natural beauty",
            "- Rich cultural heritage", 
            "- Perfect for photography",
            "- Unique local experiences"
        ]
        
        for highlight in highlights[:3]:
            st.markdown(highlight)
        
        # Add interactive elements
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("📸 View Photos", key=f"photos_{destination['name']}", use_container_width=True):
                st.info("Photo gallery feature coming soon!")
        with col_b:
            if st.button("📍 Get Directions", key=f"directions_{destination['name']}", use_container_width=True):
                st.info("Interactive map feature coming soon!")
    
    # Package cost estimate
    st.markdown("### 💰 Package Cost Estimate")
    
    base_costs = {
        "2-3 Days": 8000,
        "4-5 Days": 15000,
        "6-7 Days": 22000,
        "8-10 Days": 30000,
        "11+ Days": 40000
    }
    
    duration_cost = base_costs.get(package_data['duration'], 15000)
    destination_multiplier = len(filtered_destinations) * 2000
    total_estimate = duration_cost + destination_multiplier
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Base Cost", f"₹{duration_cost:,}")
    with col2:
        st.metric("Destination Add-ons", f"₹{destination_multiplier:,}")
    with col3:
        st.metric("Total Estimate", f"₹{total_estimate:,}", "Approximate")
    
    st.info("💡 This is an estimate. Actual costs may vary based on accommodation type, activities, and seasonal rates.")
    
    # Call to action
    st.markdown("### 📞 Ready to Book?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📱 Save This Package", type="secondary", use_container_width=True):
            st.success("Package saved to your itineraries!")
    with col2:
        if st.button("📞 Contact Us for Booking", type="primary", use_container_width=True):
            st.success("Our travel experts will contact you within 24 hours!")

def main():
    st.markdown('<h1 class="main-header">🏛️ Karnataka Travel Planner</h1>', unsafe_allow_html=True)
    st.markdown("### Plan your perfect Karnataka adventure starting from Bangalore!")
    
    # Sidebar for main navigation
    with st.sidebar:
        st.image("https://via.placeholder.com/300x150/FF6B35/FFFFFF?text=Karnataka+Tourism", width=300)
        
        page = st.selectbox(
            "Choose Your Planning Mode",
            ["🏠 Home", "🎯 Custom Package Builder", "🧭 Direction Itineraries", "📍 Day Trips from Bangalore", 
             "🗓️ Multi-Day Karnataka Tours", "🏨 Accommodations", "🚗 Transportation", 
             "💰 Budget Planner", "📱 My Itineraries", "💧 Waterfalls", 
             "🏛️ Heritage Sites", "🏖️ Beaches", "💎 Hidden Gems"]
        )
    
    # Route to different pages
    if page == "🏠 Home":
        show_home_page()
    elif page == "🎯 Custom Package Builder":
        show_custom_package_builder()
    elif page == "🧭 Direction Itineraries":
        show_itinerary_pages()
    elif page == "📍 Day Trips from Bangalore":
        show_day_trips()
    elif page == "🗓️ Multi-Day Karnataka Tours":
        show_multi_day_tours()
    elif page == "🏨 Accommodations":
        show_accommodations()
    elif page == "🚗 Transportation":
        show_transportation()
    elif page == "💰 Budget Planner":
        show_budget_planner()
    elif page == "📱 My Itineraries":
        show_my_itineraries()
    elif page == "💧 Waterfalls":
        show_waterfalls_page()
    elif page == "🏛️ Heritage Sites":
        show_heritage_sites_page()
    elif page == "🏖️ Beaches":
        show_beaches_page()
    elif page == "💎 Hidden Gems":
        show_hidden_gems_page()

def show_home_page():
    # Video Banner using Multimedia Manager
    try:
        # Karnataka tourism promotional video - Replace with actual video URL
        karnataka_video_url = "https://www.youtube.com/embed/9bZkp7q19f0"  # Karnataka tourism video
        multimedia_manager.display_video_banner(karnataka_video_url, "Discover Karnataka's Magic")
    except:
        # Fallback banner
        multimedia_manager.display_fallback_banner()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="feature-box">
            <h3>🌟 Welcome to Your Karnataka Adventure!</h3>
            <p>Discover the rich heritage, stunning landscapes, and vibrant culture of Karnataka. 
            From the bustling streets of Bangalore to the majestic palaces of Mysore, 
            we'll help you create unforgettable memories.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Interactive Theme Selection
    st.markdown("### 🎨 Explore by Themes")
    
    themes = {
        "🏖️ Beach Paradise": ["Beaches", "Coastal Karnataka"],
        "🏛️ Temple Trails": ["Heritage Sites", "Temples"],
        "💕 Honeymoon": ["Romantic Destinations", "Hill Stations"],
        "🏔️ Adventure": ["Trekking", "Water Sports", "Wildlife"],
        "🍽️ Food & Culture": ["Local Cuisine", "Festivals"],
        "📸 Photography": ["Scenic Spots", "Sunrise Points"],
        "👨‍👩‍👧‍👦 Family": ["Family-friendly", "Educational"],
        "🧘 Spiritual": ["Temples", "Ashrams", "Meditation"]
    }
    
    cols = st.columns(4)
    selected_theme = None
    
    for idx, (theme_name, theme_tags) in enumerate(themes.items()):
        with cols[idx % 4]:
            if st.button(theme_name, key=f"theme_{idx}", use_container_width=True):
                selected_theme = theme_name
    
    if selected_theme:
        st.success(f"🎯 You selected: {selected_theme}")
        st.info("💡 Use our Custom Package Builder to create personalized itineraries!")
    
    # Quick stats with enhanced graphics
    st.markdown("### 📊 Karnataka Travel Insights")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Popular Destinations", "50+", "🏛️")
    with col2:
        st.metric("Day Trip Options", "25+", "🚗")
    with col3:
        st.metric("Hidden Gems", "30+", "💎")
    with col4:
        st.metric("Happy Travelers", "10K+", "😊")
    
    # Enhanced Quick Trip Planner
    st.markdown("### 🚀 Smart Trip Planner")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        trip_duration = st.selectbox("Trip Duration", ["1 Day", "2-3 Days", "4-5 Days", "6+ Days"])
    
    with col2:
        interests = st.multiselect(
            "Your Interests",
            ["Heritage & Culture", "Nature & Wildlife", "Adventure Sports", 
             "Spiritual Sites", "Food & Cuisine", "Photography", "Beach & Relaxation"]
        )
    
    with col3:
        budget_range = st.selectbox("Budget Range", ["Budget (< ₹5K)", "Mid-range (₹5K-15K)", "Premium (> ₹15K)"])
    
    if st.button("🎯 Find My Perfect Trip", type="primary", use_container_width=True):
        st.success("✨ Based on your preferences, we recommend exploring our Custom Package Builder!")
        st.info("💡 Create personalized packages matching your interests and budget.")
        budget_range = st.select_slider(
            "Budget Range (per person)",
            options=["₹1K-3K", "₹3K-7K", "₹7K-15K", "₹15K-30K", "₹30K+"]
        )
    
    if st.button("🔍 Find My Perfect Trip", type="primary"):
        st.success("🎉 Great! Based on your preferences, we found 12 amazing options for you!")
        show_recommended_trips(trip_duration, interests, budget_range)

def show_recommended_trips(duration, interests, budget):
    st.markdown("### 🎯 Recommended Trips for You")
    
    # Sample recommendations based on inputs
    recommendations = [
        {
            "title": "Mysore Palace & Chamundi Hills",
            "duration": "1 Day",
            "price": "₹2,500",
            "highlights": ["Mysore Palace", "Chamundi Hills", "Local Cuisine"],
            "rating": 4.8
        },
        {
            "title": "Coorg Coffee Plantation Tour",
            "duration": "2 Days",
            "price": "₹8,500",
            "highlights": ["Coffee Plantations", "Abbey Falls", "Raja's Seat"],
            "rating": 4.9
        },
        {
            "title": "Hampi Heritage Circuit",
            "duration": "3 Days",
            "price": "₹12,000",
            "highlights": ["Vijayanagara Ruins", "Vittala Temple", "Matanga Hill"],
            "rating": 4.7
        }
    ]
    
    for i, trip in enumerate(recommendations):
        with st.container():
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                st.markdown(f"**{trip['title']}**")
                st.write(f"⭐ {trip['rating']} | {', '.join(trip['highlights'])}")
            
            with col2:
                st.write(f"🕒 {trip['duration']}")
            
            with col3:
                st.write(f"💰 {trip['price']}")
            
            with col4:
                if st.button(f"Select", key=f"select_{i}"):
                    st.session_state.selected_trip = trip
                    st.success(f"Selected: {trip['title']}")

def show_day_trips():
    st.markdown("## 📍 Day Trips from Bangalore (Within 100km)")
    
    # Interactive map
    st.markdown("### 🗺️ Explore Destinations on Map")
    
    # Sample locations within 100km of Bangalore
    locations = [
        {"name": "Nandi Hills", "lat": 13.3703, "lon": 77.6838, "distance": "60km", "type": "Hill Station"},
        {"name": "Bannerghatta National Park", "lat": 12.7993, "lon": 77.5769, "distance": "25km", "type": "Wildlife"},
        {"name": "Skandagiri", "lat": 13.4067, "lon": 77.6833, "distance": "62km", "type": "Trekking"},
        {"name": "Savandurga", "lat": 12.9167, "lon": 77.2833, "distance": "50km", "type": "Adventure"},
        {"name": "Wonderla", "lat": 12.8347, "lon": 77.3997, "distance": "28km", "type": "Theme Park"}
    ]
    
    # Create map
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=9)
    
    # Add Bangalore marker
    folium.Marker(
        [12.9716, 77.5946],
        popup="Bangalore - Starting Point",
        icon=folium.Icon(color='red', icon='home')
    ).add_to(m)
    
    # Add destination markers
    for loc in locations:
        folium.Marker(
            [loc['lat'], loc['lon']],
            popup=f"{loc['name']} - {loc['distance']} ({loc['type']})",
            icon=folium.Icon(color='blue', icon='map-pin')
        ).add_to(m)
    
    map_data = st_folium(m, width=700, height=400)
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        trip_type = st.selectbox(
            "Trip Type",
            ["All", "Hill Station", "Wildlife", "Trekking", "Adventure", "Theme Park", "Heritage"]
        )
    
    with col2:
        max_distance = st.slider("Maximum Distance (km)", 20, 100, 60)
    
    with col3:
        budget_filter = st.selectbox(
            "Budget Range",
            ["All", "₹500-1500", "₹1500-3000", "₹3000-5000"]
        )
    
    # Display filtered results
    show_day_trip_cards()

def show_day_trip_cards():
    st.markdown("### 🎯 Available Day Trips")
    
    trips = [
        {
            "name": "Nandi Hills Sunrise Trek",
            "distance": "60km",
            "duration": "12 hours",
            "price": "₹1,200",
            "rating": 4.6,
            "image": "https://via.placeholder.com/300x200/4CAF50/FFFFFF?text=Nandi+Hills",
            "highlights": ["Sunrise View", "Tipu's Drop", "Bhoga Nandeeshwara Temple"],
            "includes": ["Transport", "Breakfast", "Guide"]
        },
        {
            "name": "Bannerghatta Safari",
            "distance": "25km",
            "duration": "8 hours",
            "price": "₹800",
            "rating": 4.4,
            "image": "https://via.placeholder.com/300x200/FF9800/FFFFFF?text=Safari",
            "highlights": ["Lion Safari", "Tiger Safari", "Butterfly Park"],
            "includes": ["Transport", "Entry Tickets", "Lunch"]
        }
    ]
    
    for trip in trips:
        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(trip["image"], width=300)
            
            with col2:
                st.markdown(f"### {trip['name']}")
                st.write(f"📍 {trip['distance']} | ⏱️ {trip['duration']} | ⭐ {trip['rating']}")
                st.write(f"**Highlights:** {', '.join(trip['highlights'])}")
                st.write(f"**Includes:** {', '.join(trip['includes'])}")
                
                col_price, col_book = st.columns([1, 1])
                with col_price:
                    st.markdown(f"### {trip['price']}")
                with col_book:
                    if st.button(f"Book Now", key=f"book_{trip['name']}"):
                        st.success("Added to your itinerary!")
            
            st.divider()

def show_multi_day_tours():
    st.markdown("## 🗓️ Multi-Day Karnataka Tours")
    
    # Duration selector
    duration = st.radio(
        "Select Tour Duration",
        ["2-3 Days", "4-5 Days", "6+ Days"],
        horizontal=True
    )
    
    # Theme selector
    themes = st.multiselect(
        "Choose Your Themes",
        ["Heritage & History", "Nature & Wildlife", "Spiritual Journey", 
         "Adventure Sports", "Cultural Experience", "Food Trail"]
    )
    
    if duration == "2-3 Days":
        show_short_tours()
    elif duration == "4-5 Days":
        show_medium_tours()
    else:
        show_long_tours()

def show_short_tours():
    st.markdown("### 🏛️ 2-3 Day Tours")
    
    tours = [
        {
            "title": "Mysore-Coorg Heritage Trail",
            "duration": "3 Days / 2 Nights",
            "price": "₹8,500",
            "itinerary": ["Day 1: Bangalore → Mysore Palace → Chamundi Hills",
                         "Day 2: Mysore → Coorg → Coffee Plantation Tour",
                         "Day 3: Abbey Falls → Raja's Seat → Return to Bangalore"],
            "includes": ["AC Transport", "Hotel Stay", "Breakfast", "Sightseeing"]
        }
    ]
    
    for tour in tours:
        with st.expander(f"{tour['title']} - {tour['price']}"):
            st.write(f"**Duration:** {tour['duration']}")
            st.write("**Detailed Itinerary:**")
            for day in tour['itinerary']:
                st.write(f"• {day}")
            st.write(f"**Package Includes:** {', '.join(tour['includes'])}")
            
            if st.button(f"Customize This Tour", key=f"customize_{tour['title']}"):
                show_customization_options()

def show_customization_options():
    st.markdown("### 🎨 Customize Your Tour")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Accommodation Preferences**")
        accommodation = st.selectbox(
            "Choose Accommodation Type",
            ["3-Star Hotels", "4-Star Hotels", "5-Star Hotels", "Heritage Hotels", "Homestays", "Resorts"]
        )
        
        room_type = st.selectbox(
            "Room Type",
            ["Standard Room", "Deluxe Room", "Suite", "Family Room"]
        )
    
    with col2:
        st.markdown("**Transportation Preferences**")
        transport = st.selectbox(
            "Choose Transport",
            ["AC Sedan (4 seater)", "AC SUV (6 seater)", "Tempo Traveller (12 seater)", "AC Bus"]
        )
        
        meal_plan = st.selectbox(
            "Meal Plan",
            ["Breakfast Only", "Half Board (B&D)", "Full Board (B,L&D)", "All Inclusive"]
        )
    
    # Price calculator
    base_price = 8500
    accommodation_multiplier = {"3-Star Hotels": 1.0, "4-Star Hotels": 1.3, "5-Star Hotels": 1.8, 
                              "Heritage Hotels": 1.5, "Homestays": 0.8, "Resorts": 1.6}
    
    final_price = base_price * accommodation_multiplier.get(accommodation, 1.0)
    
    st.markdown(f"### Updated Price: ₹{final_price:,.0f}")
    
    if st.button("💾 Save Customized Tour"):
        st.success("Your customized tour has been saved to 'My Itineraries'!")

def show_accommodations():
    st.markdown("## 🏨 Accommodations")
    
    # Filters
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        location = st.selectbox("Location", ["All", "Bangalore", "Mysore", "Coorg", "Hampi", "Gokarna"])
    
    with col2:
        category = st.selectbox("Category", ["All", "3-Star", "4-Star", "5-Star", "Heritage", "Homestay", "Resort"])
    
    with col3:
        price_range = st.selectbox("Price Range", ["All", "₹1K-3K", "₹3K-7K", "₹7K-15K", "₹15K+"])
    
    with col4:
        amenities = st.multiselect("Amenities", ["WiFi", "Pool", "Spa", "Restaurant", "Gym", "Parking"])
    
    # Sample accommodations
    accommodations = [
        {
            "name": "The Lalit Ashok Bangalore",
            "category": "5-Star",
            "location": "Bangalore",
            "price": "₹8,500",
            "rating": 4.5,
            "amenities": ["WiFi", "Pool", "Spa", "Restaurant", "Gym"],
            "image": "https://via.placeholder.com/300x200/2196F3/FFFFFF?text=5-Star+Hotel"
        },
        {
            "name": "Coorg Wilderness Resort",
            "category": "Resort",
            "location": "Coorg",
            "price": "₹6,200",
            "rating": 4.7,
            "amenities": ["WiFi", "Pool", "Restaurant", "Nature Walks"],
            "image": "https://via.placeholder.com/300x200/4CAF50/FFFFFF?text=Resort"
        }
    ]
    
    for hotel in accommodations:
        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(hotel["image"], width=300)
            
            with col2:
                st.markdown(f"### {hotel['name']}")
                st.write(f"📍 {hotel['location']} | ⭐ {hotel['rating']} | 🏷️ {hotel['category']}")
                st.write(f"**Amenities:** {', '.join(hotel['amenities'])}")
                
                col_price, col_book = st.columns([1, 1])
                with col_price:
                    st.markdown(f"### {hotel['price']}/night")
                with col_book:
                    if st.button(f"Book", key=f"book_hotel_{hotel['name']}"):
                        st.success("Hotel added to your itinerary!")
            
            st.divider()

def show_transportation():
    st.markdown("## 🚗 Transportation Options")
    
    transport_options = [
        {
            "type": "AC Sedan",
            "capacity": "4 passengers",
            "price": "₹12/km",
            "features": ["AC", "Professional Driver", "Fuel Included"],
            "best_for": "Couples, Small Families"
        },
        {
            "type": "AC SUV",
            "capacity": "6-7 passengers",
            "price": "₹16/km",
            "features": ["AC", "Spacious", "Luggage Space", "Professional Driver"],
            "best_for": "Families, Groups"
        },
        {
            "type": "Tempo Traveller",
            "capacity": "12 passengers",
            "price": "₹22/km",
            "features": ["AC", "Comfortable Seating", "Large Luggage Space"],
            "best_for": "Large Groups"
        },
        {
            "type": "AC Bus",
            "capacity": "25+ passengers",
            "price": "₹35/km",
            "features": ["AC", "Reclining Seats", "Entertainment System"],
            "best_for": "Corporate Groups, Large Families"
        }
    ]
    
    for transport in transport_options:
        with st.container():
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"### {transport['type']}")
                st.write(f"**Capacity:** {transport['capacity']}")
                st.write(f"**Features:** {', '.join(transport['features'])}")
                st.write(f"**Best for:** {transport['best_for']}")
            
            with col2:
                st.markdown(f"### {transport['price']}")
            
            with col3:
                if st.button(f"Select", key=f"transport_{transport['type']}"):
                    st.success(f"Selected {transport['type']}")
            
            st.divider()

def show_budget_planner():
    st.markdown("## 💰 Budget Planner")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Trip Details")
        
        num_people = st.number_input("Number of People", min_value=1, max_value=20, value=2)
        trip_days = st.number_input("Number of Days", min_value=1, max_value=15, value=3)
        
        accommodation_budget = st.slider("Accommodation Budget per night", 1000, 20000, 5000)
        transport_budget = st.slider("Transportation Budget per day", 500, 5000, 2000)
        food_budget = st.slider("Food Budget per person per day", 300, 2000, 800)
        activity_budget = st.slider("Activities Budget per person", 500, 5000, 1500)
    
    with col2:
        st.markdown("### Budget Breakdown")
        
        total_accommodation = accommodation_budget * trip_days
        total_transport = transport_budget * trip_days
        total_food = food_budget * num_people * trip_days
        total_activities = activity_budget * num_people
        
        total_budget = total_accommodation + total_transport + total_food + total_activities
        
        # Create pie chart
        labels = ['Accommodation', 'Transportation', 'Food', 'Activities']
        values = [total_accommodation, total_transport, total_food, total_activities]
        
        fig = px.pie(values=values, names=labels, title="Budget Distribution")
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"### Total Budget: ₹{total_budget:,}")
        st.markdown(f"**Per Person: ₹{total_budget/num_people:,.0f}**")

def show_my_itineraries():
    st.markdown("## 📱 My Itineraries")
    
    # Sample saved itineraries
    if 'saved_itineraries' not in st.session_state:
        st.session_state.saved_itineraries = [
            {
                "name": "Mysore Weekend Getaway",
                "duration": "2 Days",
                "budget": "₹6,500",
                "status": "Planned"
            }
        ]
    
    if st.session_state.saved_itineraries:
        for i, itinerary in enumerate(st.session_state.saved_itineraries):
            with st.container():
                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                
                with col1:
                    st.write(f"**{itinerary['name']}**")
                
                with col2:
                    st.write(itinerary['duration'])
                
                with col3:
                    st.write(itinerary['budget'])
                
                with col4:
                    if st.button(f"View", key=f"view_{i}"):
                        st.info("Itinerary details would open here")
                
                st.divider()
    else:
        st.info("No saved itineraries yet. Start planning your trip!")

def show_waterfalls_page():
    """Display comprehensive waterfalls page with multimedia"""
    multimedia_manager.display_waterfall_showcase(KARNATAKA_WATERFALLS)
    
    # Interactive map of waterfalls
    st.markdown("### 🗺️ Waterfalls Map")
    multimedia_manager.create_interactive_map_with_media(KARNATAKA_WATERFALLS)
    
    # Hidden waterfall gems
    st.markdown("---")
    hidden_waterfalls = [wf for wf in KARNATAKA_WATERFALLS if wf.get('hidden_gem', False)]
    if hidden_waterfalls:
        multimedia_manager.display_hidden_gems_section(hidden_waterfalls)

def show_heritage_sites_page():
    """Display comprehensive heritage sites page"""
    multimedia_manager.display_heritage_showcase(KARNATAKA_HERITAGE_SITES)
    
    # Interactive heritage map
    st.markdown("### 🗺️ Heritage Sites Map")
    multimedia_manager.create_interactive_map_with_media(KARNATAKA_HERITAGE_SITES)

def show_beaches_page():
    """Display beaches page with multimedia"""
    st.markdown("## 🏖️ Karnataka's Beautiful Beaches")
    
    for beach in KARNATAKA_BEACHES:
        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if beach.get('photos'):
                    st.image(
                        beach['photos'][0],
                        caption=beach['name'],
                        use_container_width=True
                    )
            
            with col2:
                st.markdown(f"### {beach['name']}")
                st.markdown(f"**📍 District:** {beach['district']}")
                st.markdown(f"**🚗 Distance:** {beach['distance_from_bangalore']}km from Bangalore")
                st.markdown(f"**🌊 Beaches:** {', '.join(beach['beaches'])}")
                st.markdown(f"**🎯 Activities:** {', '.join(beach['activities'])}")
                st.markdown(f"**🌟 Best Time:** {beach['best_time']}")
                
                if st.button(f"Add {beach['name']} to Trip", key=f"beach_{beach['id']}"):
                    st.success(f"Added {beach['name']} to your coastal adventure!")
            
            st.write(beach['description'])
            st.divider()

def show_hidden_gems_page():
    """Display hidden gems page"""
    st.markdown("# 💎 Hidden Gems of Karnataka")
    st.markdown("*Discover Karnataka's best-kept secrets that even locals might not know about!*")
    
    # Combine all hidden gems from different categories
    all_destinations = DAY_TRIP_DESTINATIONS + MULTI_DAY_DESTINATIONS + KARNATAKA_WATERFALLS + KARNATAKA_HERITAGE_SITES
    hidden_gems = [dest for dest in all_destinations if dest.get('hidden_gem', False)]
    
    if hidden_gems:
        # Featured hidden gem
        st.markdown("## 🌟 Featured Hidden Gem")
        
        # Highlight Kailasagiri Hill
        kailasagiri = next((gem for gem in hidden_gems if 'Kailasagiri' in gem['name']), None)
        if kailasagiri:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"### 💎 {kailasagiri['name']}")
                st.write(kailasagiri.get('description', ''))
                
                if kailasagiri.get('highlights'):
                    st.markdown("**✨ Special Features:**")
                    for highlight in kailasagiri['highlights']:
                        st.markdown(f"• {highlight}")
                
                if kailasagiri.get('activities'):
                    st.markdown("**🎯 Activities:**")
                    for activity in kailasagiri['activities']:
                        st.markdown(f"• {activity}")
            
            with col2:
                if kailasagiri.get('photos'):
                    st.image(
                        kailasagiri['photos'][0],
                        caption="Kailasagiri Cave Temple - A Hidden Spiritual Gem",
                        use_container_width=True
                    )
                
                st.markdown(f"**📍 Distance:** {kailasagiri.get('distance_km', 'N/A')}km")
                st.markdown(f"**💰 Entry Fee:** ₹{kailasagiri.get('entry_fee', 0)}")
                st.markdown(f"**⏱️ Time Needed:** {kailasagiri.get('estimated_time', 'N/A')}")
                
                if st.button("🚀 Plan Trip to Kailasagiri"):
                    st.success("Added Kailasagiri Hill to your hidden gems adventure!")
        
        st.markdown("---")
        
        # All hidden gems
        multimedia_manager.display_hidden_gems_section(hidden_gems)
        
        # Interactive map
        st.markdown("### 🗺️ Hidden Gems Map")
        multimedia_manager.create_interactive_map_with_media(hidden_gems)
        
        # Tips for exploring hidden gems
        st.markdown("---")
        st.markdown("## 💡 Tips for Exploring Hidden Gems")
        
        tips = [
            "🗺️ **Research Local Guides**: Many hidden gems require local knowledge to access safely",
            "📱 **Download Offline Maps**: Remote locations may have poor network connectivity",
            "🎒 **Pack Essentials**: Carry water, snacks, first aid kit, and appropriate gear",
            "🌅 **Start Early**: Beat the crowds and enjoy peaceful moments at these pristine locations",
            "📸 **Respect Nature**: Follow Leave No Trace principles to preserve these gems",
            "👥 **Travel in Groups**: Some remote locations are safer when visited with companions",
            "🚗 **Check Road Conditions**: Verify accessibility, especially during monsoon season",
            "📞 **Inform Someone**: Share your itinerary with family/friends when visiting remote areas"
        ]
        
        for tip in tips:
            st.markdown(tip)
    
    else:
        st.info("Hidden gems data is being updated. Check back soon for amazing discoveries!")

if __name__ == "__main__":
    main()