"""
Simplified version of Karnataka Travel Planner for testing
Removes dependencies that might cause issues in Codespaces
"""

import streamlit as st
import sys
import os

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Page configuration
st.set_page_config(
    page_title="Karnataka Travel Planner",
    page_icon="🏛️",
    layout="wide"
)

def main():
    st.title("🏛️ Karnataka Travel Planner")
    st.markdown("### Discover Hidden Gems Around Bangalore and Across Karnataka")
    
    # Sidebar navigation
    with st.sidebar:
        st.image("https://via.placeholder.com/300x150/FF6B35/FFFFFF?text=Karnataka+Tourism", width=300)
        
        page = st.selectbox(
            "Choose Your Planning Mode",
            ["🏠 Home", "🧭 Direction Itineraries", "💎 Hidden Gems", "🏛️ Heritage Sites"]
        )
    
    if page == "🏠 Home":
        show_home()
    elif page == "🧭 Direction Itineraries":
        show_directions()
    elif page == "💎 Hidden Gems":
        show_hidden_gems()
    elif page == "🏛️ Heritage Sites":
        show_heritage()

def show_home():
    st.markdown("## Welcome to Karnataka's Hidden Treasures!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Destinations", "100+", "🏛️")
    with col2:
        st.metric("Hidden Gems", "60+", "💎")
    with col3:
        st.metric("Directions", "9", "🧭")
    
    st.markdown("### 🎯 Quick Trip Planner")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        duration = st.selectbox("Trip Duration", ["1 Day", "2-3 Days", "4-5 Days", "6+ Days"])
    
    with col2:
        interests = st.multiselect(
            "Your Interests",
            ["Heritage", "Nature", "Adventure", "Spiritual", "Photography"]
        )
    
    with col3:
        budget = st.select_slider(
            "Budget Range",
            options=["₹1K-3K", "₹3K-7K", "₹7K-15K", "₹15K+"]
        )
    
    if st.button("🔍 Find Perfect Trip", type="primary"):
        st.success("🎉 Found 12 amazing options for you!")
        show_recommendations()

def show_recommendations():
    st.markdown("### 🎯 Recommended for You")
    
    recommendations = [
        {
            "name": "Kailasagiri Hill & Cave Temple",
            "location": "Near Chintamani (80km)",
            "highlights": "Ancient cave temple, Pandava connection, Spiritual experience",
            "category": "Hidden Gem"
        },
        {
            "name": "Antaragange Caves",
            "location": "Kolar (70km)",
            "highlights": "Natural caves, Rock formations, Night trekking",
            "category": "Adventure"
        },
        {
            "name": "Chunchi Falls",
            "location": "Kanakapura (83km)",
            "highlights": "Waterfall, Natural pools, Photography",
            "category": "Nature"
        }
    ]
    
    for rec in recommendations:
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**💎 {rec['name']}**")
                st.markdown(f"📍 {rec['location']}")
                st.markdown(f"✨ {rec['highlights']}")
            
            with col2:
                st.markdown(f"🏷️ {rec['category']}")
                if st.button(f"Explore", key=rec['name']):
                    st.success(f"Added {rec['name']} to your trip!")
            
            st.divider()

def show_directions():
    st.markdown("## 🧭 Direction-wise Hidden Gems from Bangalore")
    
    directions = {
        "🏆 Towards Kolar (Golden Route)": {
            "distance": "70-100km",
            "gems": ["Kailasagiri Hill", "Antaragange Caves", "Kotilingeshwara Temple", "KGF Heritage"]
        },
        "🏞️ Towards Kanakapura": {
            "distance": "70-100km", 
            "gems": ["Chunchi Falls", "Bilikal Rangaswamy Betta", "Mekedatu", "Sangama"]
        },
        "🕉️ Towards Tumkur": {
            "distance": "65-100km",
            "gems": ["Devarayanadurga", "Madhugiri Fort", "Siddara Betta", "Goravanahalli Temple"]
        }
    }
    
    selected = st.selectbox("Choose Direction:", list(directions.keys()))
    
    direction_data = directions[selected]
    
    st.markdown(f"### {selected}")
    st.markdown(f"**Distance Range:** {direction_data['distance']}")
    st.markdown("**Hidden Gems:**")
    
    for gem in direction_data['gems']:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"• **{gem}**")
        with col2:
            if st.button("Details", key=gem):
                show_gem_details(gem)

def show_gem_details(gem_name):
    """Show details for a specific gem"""
    
    gem_details = {
        "Kailasagiri Hill": {
            "description": "Hidden cave temple near Chintamani with ancient Chathurmukhalingeshwara shrine. Legend connects it to Pandavas' exile period.",
            "distance": "80km from Bangalore",
            "highlights": ["Cave temple", "Four-faced Shiva", "Pandava connection", "Spiritual significance"],
            "activities": ["Cave exploration", "Temple visit", "Trekking", "Photography"]
        },
        "Antaragange Caves": {
            "description": "Volcanic rock formation with natural caves and perennial spring. Popular for night trekking and cave exploration.",
            "distance": "70km from Bangalore", 
            "highlights": ["Natural caves", "Rock formations", "Perennial spring", "Night trek"],
            "activities": ["Cave exploration", "Rock climbing", "Night trekking", "Photography"]
        }
    }
    
    if gem_name in gem_details:
        details = gem_details[gem_name]
        
        with st.expander(f"📖 {gem_name} Details", expanded=True):
            st.markdown(f"**📍 Distance:** {details['distance']}")
            st.markdown(f"**📖 Description:** {details['description']}")
            
            st.markdown("**✨ Highlights:**")
            for highlight in details['highlights']:
                st.markdown(f"• {highlight}")
            
            st.markdown("**🎯 Activities:**")
            for activity in details['activities']:
                st.markdown(f"• {activity}")

def show_hidden_gems():
    st.markdown("## 💎 Karnataka's Hidden Gems")
    
    regions = {
        "🏔️ North Karnataka": ["Yana Rocks", "Sathodi Falls", "Magod Falls"],
        "🌿 Central Karnataka": ["Agumbe Rainforest", "Barkana Falls", "Onake Abbi Falls"],
        "🏞️ South Karnataka": ["Netravati Peak", "Ettina Bhuja", "Pandavar Gudda"],
        "🏖️ Coastal Karnataka": ["Hoode Beach", "Kodi Beach", "Byndoor Beach"]
    }
    
    selected_region = st.selectbox("Choose Region:", list(regions.keys()))
    
    st.markdown(f"### {selected_region}")
    
    for gem in regions[selected_region]:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"💎 **{gem}**")
        with col2:
            if st.button("Explore", key=f"region_{gem}"):
                st.success(f"Added {gem} to your wishlist!")

def show_heritage():
    st.markdown("## 🏛️ Heritage Sites")
    
    heritage_sites = [
        {
            "name": "Hampi Group of Monuments",
            "status": "UNESCO World Heritage Site",
            "distance": "340km from Bangalore",
            "highlights": "Vijayanagara Empire ruins, Vittala Temple, Stone Chariot"
        },
        {
            "name": "Pattadakal Monuments", 
            "status": "UNESCO World Heritage Site",
            "distance": "450km from Bangalore",
            "highlights": "Chalukyan architecture, Temple complex, Ancient art"
        },
        {
            "name": "Kailasagiri Cave Temple",
            "status": "Hidden Heritage Gem",
            "distance": "80km from Bangalore", 
            "highlights": "Ancient cave temple, Pandava connection, Spiritual significance"
        }
    ]
    
    for site in heritage_sites:
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### {site['name']}")
                st.markdown(f"**Status:** {site['status']}")
                st.markdown(f"**Distance:** {site['distance']}")
                st.markdown(f"**Highlights:** {site['highlights']}")
            
            with col2:
                if st.button("Visit", key=site['name']):
                    st.success(f"Added {site['name']} to your heritage tour!")
            
            st.divider()

if __name__ == "__main__":
    main()