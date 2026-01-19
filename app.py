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
    }
    .trip-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .feature-box {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #FF6B35;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🏛️ Karnataka Travel Planner</h1>', unsafe_allow_html=True)
    st.markdown("### Plan your perfect Karnataka adventure starting from Bangalore!")
    
    # Sidebar for main navigation
    with st.sidebar:
        st.image("https://via.placeholder.com/300x150/FF6B35/FFFFFF?text=Karnataka+Tourism", width=300)
        
        page = st.selectbox(
            "Choose Your Planning Mode",
            ["🏠 Home", "🧭 Direction Itineraries", "📍 Day Trips from Bangalore", 
             "🗓️ Multi-Day Karnataka Tours", "🏨 Accommodations", "🚗 Transportation", 
             "💰 Budget Planner", "📱 My Itineraries", "💧 Waterfalls", 
             "🏛️ Heritage Sites", "🏖️ Beaches", "💎 Hidden Gems"]
        )
    
    # Route to different pages
    if page == "🏠 Home":
        show_home_page()
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
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Popular Destinations", "50+", "🏛️")
    with col2:
        st.metric("Day Trip Options", "25+", "🚗")
    with col3:
        st.metric("Accommodation Partners", "200+", "🏨")
    with col4:
        st.metric("Happy Travelers", "10K+", "😊")
    
    # Quick trip planner
    st.markdown("### 🚀 Quick Trip Planner")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        trip_duration = st.selectbox("Trip Duration", ["1 Day", "2-3 Days", "4-5 Days", "6+ Days"])
    
    with col2:
        interests = st.multiselect(
            "Your Interests",
            ["Heritage & Culture", "Nature & Wildlife", "Adventure Sports", 
             "Spiritual Sites", "Food & Cuisine", "Photography"]
        )
    
    with col3:
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