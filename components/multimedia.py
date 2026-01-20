"""
Multimedia components for Karnataka Travel Planner
Handles photos, videos, and interactive media content
"""

import streamlit as st
import requests
from PIL import Image
import io

class MultimediaManager:
    """Manages multimedia content for destinations"""
    
    def __init__(self):
        self.photo_cache = {}
        self.video_cache = {}
    
    def display_video_banner(self, video_url=None, title="Karnataka Tourism", height=400):
        """Display an attractive video banner"""
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #FF6B35; margin-bottom: 1rem;">🌟 {title}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if video_url:
            try:
                # Display video with custom styling
                video_html = f"""
                <div style="width: 100%; height: {height}px; border-radius: 15px; overflow: hidden; box-shadow: 0 8px 32px rgba(0,0,0,0.1); margin-bottom: 2rem;">
                    <iframe width="100%" height="{height}" src="{video_url}" 
                            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                            allowfullscreen style="border-radius: 15px;">
                    </iframe>
                </div>
                """
                st.markdown(video_html, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Could not load video: {e}")
                self.display_fallback_banner()
        else:
            self.display_fallback_banner()
    
    def display_fallback_banner(self):
        """Display a beautiful fallback image banner"""
        banner_html = """
        <div style="width: 100%; height: 400px; border-radius: 15px; overflow: hidden; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    display: flex; align-items: center; justify-content: center; 
                    box-shadow: 0 8px 32px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <div style="text-align: center; color: white;">
                <h1 style="font-size: 3rem; margin-bottom: 1rem;">🏛️ Karnataka</h1>
                <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">Land of Rich Heritage & Natural Beauty</h2>
                <p style="font-size: 1.2rem;">Discover the magic of Karnataka's temples, beaches, and hidden gems</p>
            </div>
        </div>
        """
        st.markdown(banner_html, unsafe_allow_html=True)
    
    def display_destination_gallery(self, destination):
        """Display photo gallery for a destination"""
        
        st.markdown(f"### 📸 {destination['name']} Gallery")
        
        # Photo gallery
        if destination.get('photos'):
            cols = st.columns(min(len(destination['photos']), 3))
            
            for idx, photo_url in enumerate(destination['photos']):
                with cols[idx % 3]:
                    try:
                        # In production, replace with actual image loading
                        st.image(
                            photo_url,
                            caption=f"{destination['name']} - View {idx + 1}",
                            use_container_width=True
                        )
                    except Exception as e:
                        st.error(f"Could not load image: {e}")
        
        # Video content
        if destination.get('videos'):
            st.markdown("### 🎥 Videos")
            
            for idx, video_url in enumerate(destination['videos']):
                try:
                    # For YouTube videos
                    if 'youtube.com' in video_url or 'youtu.be' in video_url:
                        st.video(video_url)
                    else:
                        st.video(video_url)
                except Exception as e:
                    st.error(f"Could not load video: {e}")
    
    def display_waterfall_showcase(self, waterfalls):
        """Display waterfall showcase with multimedia"""
        
        st.markdown("## 💧 Karnataka's Magnificent Waterfalls")
        
        # Featured waterfall carousel
        featured_waterfalls = [wf for wf in waterfalls if not wf.get('hidden_gem', False)][:5]
        
        if featured_waterfalls:
            selected_waterfall = st.selectbox(
                "Choose a waterfall to explore:",
                featured_waterfalls,
                format_func=lambda x: f"{x['name']} - {x['height']} ({x['district']})"
            )
            
            if selected_waterfall:
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    # Main image
                    if selected_waterfall.get('photos'):
                        st.image(
                            selected_waterfall['photos'][0],
                            caption=f"{selected_waterfall['name']} - {selected_waterfall['height']}",
                            use_container_width=True
                        )
                
                with col2:
                    st.markdown(f"**📍 Location:** {selected_waterfall['district']}")
                    st.markdown(f"**📏 Height:** {selected_waterfall['height']}")
                    st.markdown(f"**🚗 Distance:** {selected_waterfall['distance_from_bangalore']}km from Bangalore")
                    st.markdown(f"**🌟 Best Time:** {selected_waterfall['best_time']}")
                    st.markdown(f"**💰 Entry Fee:** ₹{selected_waterfall['entry_fee']}")
                    
                    if st.button(f"Add {selected_waterfall['name']} to Trip"):
                        st.success(f"Added {selected_waterfall['name']} to your itinerary!")
                
                # Description and highlights
                st.markdown(f"**About {selected_waterfall['name']}:**")
                st.write(selected_waterfall['description'])
                
                # Highlights
                if selected_waterfall.get('highlights'):
                    st.markdown("**✨ Highlights:**")
                    for highlight in selected_waterfall['highlights']:
                        st.markdown(f"• {highlight}")
    
    def display_heritage_showcase(self, heritage_sites):
        """Display heritage sites with multimedia"""
        
        st.markdown("## 🏛️ Karnataka's Rich Heritage")
        
        # UNESCO vs Non-UNESCO sites
        unesco_sites = [site for site in heritage_sites if site.get('unesco_status', False)]
        other_sites = [site for site in heritage_sites if not site.get('unesco_status', False)]
        
        tab1, tab2 = st.tabs(["🌟 UNESCO World Heritage Sites", "🏺 Other Heritage Sites"])
        
        with tab1:
            for site in unesco_sites:
                self._display_heritage_card(site, is_unesco=True)
        
        with tab2:
            for site in other_sites:
                self._display_heritage_card(site, is_unesco=False)
    
    def _display_heritage_card(self, site, is_unesco=False):
        """Display individual heritage site card"""
        
        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if site.get('photos'):
                    st.image(
                        site['photos'][0],
                        caption=site['name'],
                        use_container_width=True
                    )
            
            with col2:
                unesco_badge = "🌟 UNESCO" if is_unesco else "🏺 Heritage"
                st.markdown(f"### {site['name']} {unesco_badge}")
                
                st.markdown(f"**📍 District:** {site['district']}")
                st.markdown(f"**⏳ Period:** {site['period']}")
                st.markdown(f"**👑 Dynasty:** {site['dynasty']}")
                st.markdown(f"**🚗 Distance:** {site['distance_from_bangalore']}km")
                st.markdown(f"**💰 Entry Fee:** ₹{site['entry_fee']}")
                
                # Highlights
                if site.get('highlights'):
                    highlights_text = " • ".join(site['highlights'][:3])
                    st.markdown(f"**✨ Key Attractions:** {highlights_text}")
                
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button(f"Add to Trip", key=f"heritage_{site['id']}"):
                        st.success(f"Added {site['name']} to itinerary!")
                
                with col_btn2:
                    if st.button(f"View Details", key=f"details_{site['id']}"):
                        self._show_heritage_details(site)
            
            st.divider()
    
    def _show_heritage_details(self, site):
        """Show detailed information about heritage site"""
        
        with st.expander(f"📖 Detailed Information - {site['name']}", expanded=True):
            st.write(site['description'])
            
            # Photo gallery
            if site.get('photos'):
                st.markdown("**📸 Photo Gallery:**")
                cols = st.columns(min(len(site['photos']), 4))
                for idx, photo in enumerate(site['photos']):
                    with cols[idx % 4]:
                        st.image(photo, use_container_width=True)
            
            # Activities
            if site.get('activities'):
                st.markdown("**🎯 Activities:**")
                for activity in site['activities']:
                    st.markdown(f"• {activity}")
            
            # Facilities
            if site.get('facilities'):
                st.markdown("**🏢 Facilities:**")
                facilities_text = " • ".join(site['facilities'])
                st.markdown(facilities_text)
    
    def display_hidden_gems_section(self, destinations):
        """Display hidden gems with special highlighting"""
        
        st.markdown("## 💎 Hidden Gems of Karnataka")
        st.markdown("*Discover the unexplored treasures that most tourists miss*")
        
        hidden_gems = [dest for dest in destinations if dest.get('hidden_gem', False)]
        
        if not hidden_gems:
            st.info("No hidden gems data available yet.")
            return
        
        # Create a special layout for hidden gems
        for gem in hidden_gems:
            with st.container():
                # Special styling for hidden gems
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 1rem;
                    border-radius: 10px;
                    color: white;
                    margin: 1rem 0;
                ">
                    <h3>💎 {gem['name']} - Hidden Gem</h3>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    if gem.get('photos'):
                        st.image(
                            gem['photos'][0],
                            caption=f"Hidden Gem: {gem['name']}",
                            use_container_width=True
                        )
                
                with col2:
                    st.markdown(f"**📍 Distance:** {gem.get('distance_km', 'N/A')}km from Bangalore")
                    st.markdown(f"**🏷️ Category:** {gem.get('category', 'N/A')}")
                    
                    if gem.get('description'):
                        st.markdown(f"**📖 About:** {gem['description']}")
                    
                    # Highlights
                    if gem.get('highlights'):
                        st.markdown("**✨ What makes it special:**")
                        for highlight in gem['highlights'][:3]:
                            st.markdown(f"• {highlight}")
                    
                    if st.button(f"Explore {gem['name']}", key=f"gem_{gem['id']}"):
                        st.success(f"Added {gem['name']} to your adventure list!")
                
                st.divider()
    
    def create_interactive_map_with_media(self, destinations):
        """Create interactive map with multimedia popups"""
        
        import folium
        from streamlit_folium import st_folium
        
        # Create base map
        m = folium.Map(location=[13.0827, 77.5877], zoom_start=7)
        
        # Add markers with multimedia content
        for dest in destinations:
            if dest.get('coordinates'):
                # Create popup content with media
                popup_html = f"""
                <div style="width: 300px;">
                    <h4>{dest['name']}</h4>
                    <p><strong>Category:</strong> {dest.get('category', 'N/A')}</p>
                    <p><strong>Distance:</strong> {dest.get('distance_km', 'N/A')}km</p>
                    <p>{dest.get('description', '')[:100]}...</p>
                </div>
                """
                
                # Color code by category
                color_map = {
                    'Heritage': 'red',
                    'Hill Station': 'green',
                    'Adventure': 'orange',
                    'Beach': 'blue',
                    'Spiritual': 'purple',
                    'Waterfalls': 'lightblue'
                }
                
                color = color_map.get(dest.get('category'), 'gray')
                
                folium.Marker(
                    [dest['coordinates']['lat'], dest['coordinates']['lon']],
                    popup=folium.Popup(popup_html, max_width=300),
                    tooltip=dest['name'],
                    icon=folium.Icon(color=color, icon='camera' if dest.get('photos') else 'info-sign')
                ).add_to(m)
        
        # Display map
        map_data = st_folium(m, width=700, height=500)
        
        return map_data
    
    def display_seasonal_recommendations(self, destinations):
        """Display destinations based on current season"""
        
        import datetime
        
        current_month = datetime.datetime.now().month
        
        # Determine season
        if current_month in [12, 1, 2]:
            season = "Winter"
            season_destinations = [d for d in destinations if "December" in d.get('best_season', '') or "January" in d.get('best_season', '')]
        elif current_month in [3, 4, 5]:
            season = "Summer"
            season_destinations = [d for d in destinations if "March" in d.get('best_season', '') or "April" in d.get('best_season', '')]
        elif current_month in [6, 7, 8, 9]:
            season = "Monsoon"
            season_destinations = [d for d in destinations if "July" in d.get('best_season', '') or "August" in d.get('best_season', '')]
        else:
            season = "Post-Monsoon"
            season_destinations = [d for d in destinations if "October" in d.get('best_season', '') or "November" in d.get('best_season', '')]
        
        st.markdown(f"## 🌤️ Perfect for {season} Season")
        st.markdown(f"*Best destinations to visit during {season.lower()} in Karnataka*")
        
        if season_destinations:
            cols = st.columns(min(len(season_destinations), 3))
            
            for idx, dest in enumerate(season_destinations[:6]):  # Show max 6
                with cols[idx % 3]:
                    if dest.get('photos'):
                        st.image(dest['photos'][0], use_container_width=True)
                    
                    st.markdown(f"**{dest['name']}**")
                    st.markdown(f"📍 {dest.get('distance_km', 'N/A')}km")
                    st.markdown(f"🏷️ {dest.get('category', 'N/A')}")
                    
                    if st.button(f"Explore", key=f"season_{dest['id']}"):
                        st.success(f"Added {dest['name']} to your {season.lower()} itinerary!")
        else:
            st.info(f"No specific recommendations available for {season} season.")

# Initialize multimedia manager
multimedia_manager = MultimediaManager()