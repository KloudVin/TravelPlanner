"""
Direction-wise Itinerary Pages for Karnataka Travel Planner
"""

import streamlit as st
import folium
from streamlit_folium import st_folium
import plotly.express as px
from data.bangalore_direction_itineraries import BANGALORE_DIRECTION_ITINERARIES, SAMPLE_ITINERARIES
from data.karnataka_hidden_gems import KARNATAKA_HIDDEN_GEMS, SEASONAL_HIDDEN_GEMS, DIFFICULTY_BASED_GEMS
from components.multimedia import multimedia_manager

def show_direction_itineraries():
    """Main page for direction-wise itineraries from Bangalore"""
    
    st.title("🧭 Direction-wise Hidden Gems from Bangalore")
    st.markdown("*Discover secret treasures in every direction within 100km of Bangalore*")
    
    # Direction selector
    direction_options = {
        "🏙️ Inside Bangalore": "inside_bangalore",
        "🌅 Towards Hosur": "towards_hosur", 
        "🏆 Towards Kolar (Golden Route)": "towards_kolar",
        "🏞️ Towards Kanakapura": "towards_kanakapura",
        "🏛️ Towards Mysore": "towards_mysore",
        "⛰️ Towards Magadi": "towards_magadi",
        "🕉️ Towards Tumkur": "towards_tumkur",
        "✈️ Towards Doddaballapur": "towards_doddaballapur",
        "🏰 Towards Devanahalli": "towards_devanahalli"
    }
    
    selected_direction = st.selectbox(
        "Choose your exploration direction:",
        list(direction_options.keys())
    )
    
    direction_key = direction_options[selected_direction]
    itinerary = BANGALORE_DIRECTION_ITINERARIES[direction_key]
    
    # Display selected itinerary
    display_direction_itinerary(itinerary, direction_key)
    
    # Interactive map for the direction
    st.markdown("---")
    st.markdown("### 🗺️ Interactive Route Map")
    create_direction_map(itinerary, direction_key)
    
    # Sample combined itineraries
    st.markdown("---")
    st.markdown("### 🎯 Themed Itinerary Suggestions")
    display_themed_itineraries()

def display_direction_itinerary(itinerary, direction_key):
    """Display detailed itinerary for a specific direction"""
    
    # Header
    st.markdown(f"## {itinerary['title']}")
    st.markdown(f"*{itinerary['subtitle']}*")
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Duration", itinerary['duration'])
    with col2:
        st.metric("Total Distance", itinerary['total_distance'])
    with col3:
        st.metric("Destinations", len(itinerary['destinations']))
    with col4:
        hidden_count = sum(1 for dest in itinerary['destinations'] if dest.get('hidden_gem', False))
        st.metric("Hidden Gems", f"{hidden_count}/{len(itinerary['destinations'])}")
    
    # Destinations
    st.markdown("### 📍 Destinations in This Route")
    
    for idx, destination in enumerate(itinerary['destinations']):
        with st.container():
            # Special styling for hidden gems
            if destination.get('hidden_gem', False):
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 1rem;
                    border-radius: 10px;
                    color: white;
                    margin: 1rem 0;
                ">
                    <h4>💎 {destination['name']} - Hidden Gem #{idx + 1}</h4>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"### {idx + 1}. {destination['name']}")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Display photo if available
                if destination.get('photos'):
                    st.image(
                        destination['photos'][0] if isinstance(destination['photos'], list) else destination['photos'],
                        caption=destination['name'],
                        use_container_width=True
                    )
            
            with col2:
                # Destination details
                st.markdown(f"**📍 Distance:** {destination['distance_km']}km from Bangalore")
                st.markdown(f"**🏷️ Category:** {destination['category']}")
                st.markdown(f"**⏱️ Time Needed:** {destination['time_needed']}")
                st.markdown(f"**💰 Entry Fee:** ₹{destination['entry_fee']}")
                st.markdown(f"**🌟 Best Time:** {destination['best_time']}")
                
                # Highlights
                if destination.get('highlights'):
                    st.markdown("**✨ Highlights:**")
                    for highlight in destination['highlights'][:3]:
                        st.markdown(f"• {highlight}")
                
                # Action buttons
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button(f"Add to Trip", key=f"add_{direction_key}_{idx}"):
                        st.success(f"Added {destination['name']} to your itinerary!")
                
                with col_btn2:
                    if st.button(f"Get Directions", key=f"directions_{direction_key}_{idx}"):
                        lat, lon = destination['coordinates']['lat'], destination['coordinates']['lon']
                        maps_url = f"https://www.google.com/maps/dir/Bangalore/{lat},{lon}"
                        st.markdown(f"[🗺️ Open in Google Maps]({maps_url})")
            
            # Description
            st.markdown(f"**📖 About:** {destination['description']}")
            
            # Activities
            if destination.get('activities'):
                st.markdown("**🎯 Activities:**")
                activities_text = " • ".join(destination['activities'])
                st.markdown(activities_text)
            
            st.divider()

def create_direction_map(itinerary, direction_key):
    """Create interactive map for the direction"""
    
    # Create map centered on Bangalore
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=9)
    
    # Add Bangalore marker
    folium.Marker(
        [12.9716, 77.5946],
        popup="Bangalore - Starting Point",
        tooltip="Bangalore",
        icon=folium.Icon(color='red', icon='home', prefix='fa')
    ).add_to(m)
    
    # Add destination markers
    for idx, dest in enumerate(itinerary['destinations']):
        coords = dest['coordinates']
        
        # Different colors for hidden gems
        color = 'purple' if dest.get('hidden_gem', False) else 'blue'
        icon = 'star' if dest.get('hidden_gem', False) else 'map-pin'
        
        popup_html = f"""
        <div style="width: 250px;">
            <h4>{'💎 ' if dest.get('hidden_gem', False) else ''}{dest['name']}</h4>
            <p><strong>Distance:</strong> {dest['distance_km']}km</p>
            <p><strong>Category:</strong> {dest['category']}</p>
            <p><strong>Time:</strong> {dest['time_needed']}</p>
            <p>{dest['description'][:100]}...</p>
        </div>
        """
        
        folium.Marker(
            [coords['lat'], coords['lon']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=dest['name'],
            icon=folium.Icon(color=color, icon=icon, prefix='fa')
        ).add_to(m)
    
    # Display map
    map_data = st_folium(m, width=700, height=500)
    
    return map_data

def display_themed_itineraries():
    """Display themed itinerary combinations"""
    
    theme_options = list(SAMPLE_ITINERARIES.keys())
    selected_theme = st.selectbox(
        "Choose a themed itinerary:",
        theme_options,
        format_func=lambda x: SAMPLE_ITINERARIES[x]['title']
    )
    
    theme_data = SAMPLE_ITINERARIES[selected_theme]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"### {theme_data['title']}")
        st.markdown(f"**Duration:** {theme_data['duration']}")
        
        st.markdown("**Destinations:**")
        for dest in theme_data['destinations']:
            st.markdown(f"• {dest}")
        
        st.markdown("**Activities:**")
        for activity in theme_data['activities']:
            st.markdown(f"• {activity}")
    
    with col2:
        if st.button(f"Plan {theme_data['title']}", type="primary"):
            st.success(f"Planning your {theme_data['title']} adventure!")
            st.balloons()

def show_karnataka_hidden_gems():
    """Display Karnataka-wide hidden gems"""
    
    st.title("💎 Karnataka's Hidden Gems")
    st.markdown("*Discover the unexplored treasures across all regions of Karnataka*")
    
    # Region selector
    region_options = {
        "🏔️ North Karnataka": "north_karnataka",
        "🌿 Central Karnataka": "central_karnataka", 
        "🏞️ South Karnataka": "south_karnataka",
        "🏖️ Coastal Karnataka": "coastal_karnataka",
        "⛰️ Eastern Karnataka": "eastern_karnataka",
        "🌲 Western Karnataka": "western_karnataka"
    }
    
    selected_region = st.selectbox(
        "Choose a region to explore:",
        list(region_options.keys())
    )
    
    region_key = region_options[selected_region]
    region_data = KARNATAKA_HIDDEN_GEMS[region_key]
    
    # Display region information
    st.markdown(f"## {region_data['region_name']}")
    st.markdown(f"*{region_data['description']}*")
    
    # Region statistics
    destinations = region_data['destinations']
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Hidden Gems", len(destinations))
    with col2:
        categories = set(dest['category'] for dest in destinations)
        st.metric("Categories", len(categories))
    with col3:
        avg_distance = sum(dest['distance_from_bangalore'] for dest in destinations) // len(destinations)
        st.metric("Avg Distance", f"{avg_distance}km")
    with col4:
        hidden_count = sum(1 for dest in destinations if dest.get('hidden_gem', True))
        st.metric("True Hidden Gems", hidden_count)
    
    # Display destinations
    st.markdown("### 🗺️ Hidden Gems in This Region")
    
    for idx, destination in enumerate(destinations):
        with st.container():
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
                padding: 1rem;
                border-radius: 10px;
                color: white;
                margin: 1rem 0;
            ">
                <h4>💎 {destination['name']} - {destination['district']} District</h4>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if destination.get('photos'):
                    st.image(
                        destination['photos'][0] if isinstance(destination['photos'], list) else destination['photos'],
                        caption=destination['name'],
                        use_container_width=True
                    )
            
            with col2:
                st.markdown(f"**📍 District:** {destination['district']}")
                st.markdown(f"**🚗 Distance:** {destination['distance_from_bangalore']}km from Bangalore")
                st.markdown(f"**🏷️ Category:** {destination['category']}")
                st.markdown(f"**🌟 Best Time:** {destination['best_time']}")
                st.markdown(f"**💰 Entry Fee:** ₹{destination['entry_fee']}")
                
                # Highlights
                if destination.get('highlights'):
                    st.markdown("**✨ Key Attractions:**")
                    for highlight in destination['highlights'][:3]:
                        st.markdown(f"• {highlight}")
                
                # Action buttons
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button(f"Add to Wishlist", key=f"wishlist_{region_key}_{idx}"):
                        st.success(f"Added {destination['name']} to your wishlist!")
                
                with col_btn2:
                    if st.button(f"Plan Trip", key=f"plan_{region_key}_{idx}"):
                        st.info(f"Planning trip to {destination['name']}...")
            
            # Description and activities
            st.markdown(f"**📖 Description:** {destination['description']}")
            
            if destination.get('activities'):
                st.markdown("**🎯 Activities:**")
                activities_text = " • ".join(destination['activities'])
                st.markdown(activities_text)
            
            st.divider()
    
    # Regional map
    st.markdown("---")
    st.markdown("### 🗺️ Regional Hidden Gems Map")
    create_regional_map(region_data)

def create_regional_map(region_data):
    """Create map for regional hidden gems"""
    
    destinations = region_data['destinations']
    
    # Calculate center point
    avg_lat = sum(dest['coordinates']['lat'] for dest in destinations) / len(destinations)
    avg_lon = sum(dest['coordinates']['lon'] for dest in destinations) / len(destinations)
    
    # Create map
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=8)
    
    # Add destination markers
    for dest in destinations:
        coords = dest['coordinates']
        
        popup_html = f"""
        <div style="width: 250px;">
            <h4>💎 {dest['name']}</h4>
            <p><strong>District:</strong> {dest['district']}</p>
            <p><strong>Category:</strong> {dest['category']}</p>
            <p><strong>Distance:</strong> {dest['distance_from_bangalore']}km</p>
            <p>{dest['description'][:100]}...</p>
        </div>
        """
        
        folium.Marker(
            [coords['lat'], coords['lon']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=dest['name'],
            icon=folium.Icon(color='purple', icon='star', prefix='fa')
        ).add_to(m)
    
    # Display map
    map_data = st_folium(m, width=700, height=500)
    
    return map_data

def show_seasonal_recommendations():
    """Display seasonal hidden gems recommendations"""
    
    st.title("🌤️ Seasonal Hidden Gems")
    st.markdown("*Discover the best hidden gems for each season in Karnataka*")
    
    # Season selector
    season_options = list(SEASONAL_HIDDEN_GEMS.keys())
    selected_season = st.selectbox(
        "Choose a season:",
        season_options,
        format_func=lambda x: SEASONAL_HIDDEN_GEMS[x]['title']
    )
    
    season_data = SEASONAL_HIDDEN_GEMS[selected_season]
    
    # Display season information
    st.markdown(f"## {season_data['title']}")
    st.markdown(f"**Season:** {season_data['season']}")
    st.markdown(f"**Description:** {season_data['description']}")
    
    # Display recommended destinations
    st.markdown("### 🎯 Recommended Hidden Gems")
    
    cols = st.columns(min(len(season_data['destinations']), 3))
    
    for idx, dest_name in enumerate(season_data['destinations']):
        with cols[idx % 3]:
            st.markdown(f"**{dest_name}**")
            
            # Find destination details from the main database
            dest_details = find_destination_details(dest_name)
            
            if dest_details:
                if dest_details.get('photos'):
                    st.image(dest_details['photos'][0], use_container_width=True)
                
                st.markdown(f"📍 {dest_details.get('district', 'Karnataka')}")
                st.markdown(f"🏷️ {dest_details.get('category', 'Hidden Gem')}")
                
                if st.button(f"Explore", key=f"seasonal_{selected_season}_{idx}"):
                    st.success(f"Added {dest_name} to your {selected_season} itinerary!")

def find_destination_details(dest_name):
    """Find destination details from the hidden gems database"""
    
    for region_data in KARNATAKA_HIDDEN_GEMS.values():
        for dest in region_data['destinations']:
            if dest_name.lower() in dest['name'].lower():
                return dest
    
    return None

def show_difficulty_based_gems():
    """Display hidden gems based on difficulty level"""
    
    st.title("🎯 Hidden Gems by Difficulty")
    st.markdown("*Choose hidden gems based on your adventure level*")
    
    # Difficulty selector
    difficulty_options = list(DIFFICULTY_BASED_GEMS.keys())
    selected_difficulty = st.selectbox(
        "Choose your adventure level:",
        difficulty_options,
        format_func=lambda x: DIFFICULTY_BASED_GEMS[x]['title']
    )
    
    difficulty_data = DIFFICULTY_BASED_GEMS[selected_difficulty]
    
    # Display difficulty information
    st.markdown(f"## {difficulty_data['title']}")
    st.markdown(f"**Description:** {difficulty_data['description']}")
    
    # Display recommended destinations
    st.markdown("### 🎯 Recommended Hidden Gems")
    
    for idx, dest_name in enumerate(difficulty_data['destinations']):
        dest_details = find_destination_details(dest_name)
        
        if dest_details:
            with st.container():
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    if dest_details.get('photos'):
                        st.image(dest_details['photos'][0], use_container_width=True)
                
                with col2:
                    st.markdown(f"### {dest_details['name']}")
                    st.markdown(f"**📍 District:** {dest_details.get('district', 'Karnataka')}")
                    st.markdown(f"**🏷️ Category:** {dest_details.get('category', 'Hidden Gem')}")
                    st.markdown(f"**🚗 Distance:** {dest_details.get('distance_from_bangalore', 'N/A')}km")
                    
                    if dest_details.get('highlights'):
                        st.markdown("**✨ Highlights:**")
                        for highlight in dest_details['highlights'][:2]:
                            st.markdown(f"• {highlight}")
                    
                    if st.button(f"Plan Adventure", key=f"difficulty_{selected_difficulty}_{idx}"):
                        st.success(f"Planning your {selected_difficulty} adventure to {dest_details['name']}!")
                
                st.markdown(f"**📖 Description:** {dest_details.get('description', '')}")
                st.divider()

# Main navigation function
def show_itinerary_pages():
    """Main function to show itinerary pages"""
    
    page_options = {
        "🧭 Direction-wise from Bangalore": show_direction_itineraries,
        "💎 Karnataka Hidden Gems": show_karnataka_hidden_gems,
        "🌤️ Seasonal Recommendations": show_seasonal_recommendations,
        "🎯 Difficulty-based Adventures": show_difficulty_based_gems
    }
    
    selected_page = st.sidebar.selectbox(
        "Choose Itinerary Type:",
        list(page_options.keys())
    )
    
    # Execute selected page function
    page_options[selected_page]()