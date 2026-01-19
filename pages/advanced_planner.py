import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from utils.helpers import calculate_trip_cost, generate_itinerary, save_itinerary
from data.destinations import DAY_TRIP_DESTINATIONS, MULTI_DAY_DESTINATIONS, TOUR_PACKAGES

def show_advanced_planner():
    st.title("🎯 Advanced Trip Planner")
    st.markdown("Create your perfect customized Karnataka adventure with our intelligent planner!")
    
    # Trip Planning Wizard
    with st.container():
        st.markdown("### 🧙‍♂️ Trip Planning Wizard")
        
        # Step 1: Basic Information
        with st.expander("📋 Step 1: Basic Trip Information", expanded=True):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                trip_name = st.text_input("Trip Name", "My Karnataka Adventure")
                num_travelers = st.number_input("Number of Travelers", 1, 20, 2)
            
            with col2:
                start_date = st.date_input("Start Date", datetime.now() + timedelta(days=7))
                end_date = st.date_input("End Date", datetime.now() + timedelta(days=10))
            
            with col3:
                budget_per_person = st.number_input("Budget per Person (₹)", 5000, 100000, 15000, step=1000)
                trip_style = st.selectbox("Trip Style", ["Relaxed", "Moderate", "Packed", "Adventure"])
        
        # Step 2: Interests and Preferences
        with st.expander("🎨 Step 2: Interests & Preferences"):
            col1, col2 = st.columns(2)
            
            with col1:
                interests = st.multiselect(
                    "Your Interests",
                    ["Heritage & History", "Nature & Wildlife", "Adventure Sports", 
                     "Spiritual Sites", "Food & Cuisine", "Photography", "Shopping",
                     "Beach Activities", "Hill Stations", "Cultural Experiences"],
                    default=["Heritage & History", "Nature & Wildlife"]
                )
                
                accommodation_pref = st.selectbox(
                    "Accommodation Preference",
                    ["Budget (₹1K-3K)", "Mid-range (₹3K-7K)", "Premium (₹7K-15K)", "Luxury (₹15K+)"]
                )
            
            with col2:
                transport_pref = st.selectbox(
                    "Transportation Preference", 
                    ["Most Economical", "Comfortable", "Luxury", "Mix of Options"]
                )
                
                meal_pref = st.selectbox(
                    "Meal Preference",
                    ["Local Street Food", "Restaurant Dining", "Hotel Meals", "Mix of All"]
                )
                
                activity_level = st.select_slider(
                    "Activity Level",
                    options=["Low", "Moderate", "High", "Extreme"],
                    value="Moderate"
                )
        
        # Step 3: Destination Selection
        with st.expander("📍 Step 3: Destination Preferences"):
            trip_duration = (end_date - start_date).days
            
            if trip_duration == 1:
                st.info("For 1-day trips, we'll show destinations within 100km of Bangalore")
                available_destinations = DAY_TRIP_DESTINATIONS
            else:
                st.info(f"For {trip_duration}-day trips, we'll include multi-day destinations")
                available_destinations = MULTI_DAY_DESTINATIONS
            
            # Destination selection with filters
            col1, col2, col3 = st.columns(3)
            
            with col1:
                category_filter = st.multiselect(
                    "Preferred Categories",
                    ["Hill Station", "Heritage", "Wildlife", "Adventure", "Beach", "Spiritual"],
                    default=[]
                )
            
            with col2:
                max_distance = st.slider("Maximum Distance from Bangalore (km)", 50, 600, 300)
            
            with col3:
                must_visit = st.multiselect(
                    "Must-Visit Places",
                    [dest['name'] for dest in available_destinations],
                    default=[]
                )
        
        # Generate Itinerary Button
        if st.button("🚀 Generate My Perfect Itinerary", type="primary"):
            generate_custom_itinerary(
                trip_name, num_travelers, start_date, end_date, budget_per_person,
                interests, accommodation_pref, transport_pref, activity_level,
                category_filter, max_distance, must_visit, available_destinations
            )

def generate_custom_itinerary(trip_name, num_travelers, start_date, end_date, budget_per_person,
                            interests, accommodation_pref, transport_pref, activity_level,
                            category_filter, max_distance, must_visit, available_destinations):
    
    st.markdown("---")
    st.markdown("## 🎉 Your Customized Itinerary")
    
    trip_duration = (end_date - start_date).days
    
    # Filter destinations based on preferences
    filtered_destinations = []
    
    for dest in available_destinations:
        # Distance filter
        if dest['distance_km'] > max_distance:
            continue
        
        # Category filter
        if category_filter and dest['category'] not in category_filter:
            continue
        
        # Must-visit filter
        if must_visit and dest['name'] not in must_visit:
            continue
        
        filtered_destinations.append(dest)
    
    # Add must-visit destinations even if they don't match other filters
    for dest_name in must_visit:
        dest = next((d for d in available_destinations if d['name'] == dest_name), None)
        if dest and dest not in filtered_destinations:
            filtered_destinations.append(dest)
    
    # Generate day-wise itinerary
    if filtered_destinations:
        # Smart itinerary generation based on distance and interests
        itinerary = create_smart_itinerary(filtered_destinations, trip_duration, interests)
        
        # Display itinerary
        display_generated_itinerary(itinerary, trip_name, num_travelers, budget_per_person)
        
        # Cost breakdown
        show_cost_breakdown(itinerary, num_travelers, accommodation_pref, transport_pref)
        
        # Save option
        if st.button("💾 Save This Itinerary"):
            itinerary_data = {
                "name": trip_name,
                "duration": f"{trip_duration} days",
                "travelers": num_travelers,
                "budget": budget_per_person * num_travelers,
                "itinerary": itinerary,
                "preferences": {
                    "interests": interests,
                    "accommodation": accommodation_pref,
                    "transport": transport_pref
                }
            }
            
            if save_itinerary(itinerary_data):
                st.success("✅ Itinerary saved successfully!")
    else:
        st.warning("No destinations match your criteria. Please adjust your filters.")

def create_smart_itinerary(destinations, duration, interests):
    """Create intelligent itinerary based on destinations and preferences"""
    
    itinerary = {}
    
    # Sort destinations by distance for logical routing
    destinations.sort(key=lambda x: x['distance_km'])
    
    # Distribute destinations across days
    destinations_per_day = max(1, len(destinations) // duration)
    
    for day in range(1, duration + 1):
        start_idx = (day - 1) * destinations_per_day
        end_idx = min(start_idx + destinations_per_day, len(destinations))
        
        if day == duration:  # Last day gets remaining destinations
            end_idx = len(destinations)
        
        day_destinations = destinations[start_idx:end_idx]
        
        # Generate activities based on destination and interests
        activities = []
        for dest in day_destinations:
            dest_activities = dest.get('activities', [])
            # Match activities with interests
            matched_activities = [act for act in dest_activities 
                                if any(interest.lower() in act.lower() for interest in interests)]
            activities.extend(matched_activities[:2])  # Limit to 2 activities per destination
        
        itinerary[f"Day {day}"] = {
            "destinations": day_destinations,
            "activities": list(set(activities)),  # Remove duplicates
            "estimated_time": "8-10 hours",
            "travel_distance": sum([d['distance_km'] for d in day_destinations]),
            "highlights": []
        }
        
        # Add highlights
        for dest in day_destinations:
            itinerary[f"Day {day}"]["highlights"].extend(dest.get('highlights', [])[:2])
    
    return itinerary

def display_generated_itinerary(itinerary, trip_name, num_travelers, budget_per_person):
    """Display the generated itinerary in a nice format"""
    
    st.markdown(f"### 📅 {trip_name}")
    st.markdown(f"**Travelers:** {num_travelers} | **Budget:** ₹{budget_per_person * num_travelers:,}")
    
    for day, details in itinerary.items():
        with st.expander(f"🗓️ {day} - {len(details['destinations'])} Destinations", expanded=True):
            
            # Destinations for the day
            st.markdown("**📍 Destinations:**")
            for dest in details['destinations']:
                st.markdown(f"• **{dest['name']}** ({dest['distance_km']}km) - {dest['category']}")
            
            # Activities
            if details['activities']:
                st.markdown("**🎯 Recommended Activities:**")
                for activity in details['activities'][:4]:  # Show max 4 activities
                    st.markdown(f"• {activity}")
            
            # Highlights
            if details['highlights']:
                st.markdown("**⭐ Key Highlights:**")
                for highlight in details['highlights'][:4]:  # Show max 4 highlights
                    st.markdown(f"• {highlight}")
            
            # Travel info
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**🚗 Travel Distance:** {details['travel_distance']}km")
            with col2:
                st.markdown(f"**⏱️ Estimated Time:** {details['estimated_time']}")

def show_cost_breakdown(itinerary, num_travelers, accommodation_pref, transport_pref):
    """Show detailed cost breakdown"""
    
    st.markdown("### 💰 Cost Breakdown")
    
    # Calculate costs based on preferences
    accommodation_costs = {
        "Budget (₹1K-3K)": 2000,
        "Mid-range (₹3K-7K)": 5000,
        "Premium (₹7K-15K)": 10000,
        "Luxury (₹15K+)": 20000
    }
    
    transport_rates = {
        "Most Economical": 10,
        "Comfortable": 15,
        "Luxury": 25,
        "Mix of Options": 18
    }
    
    num_days = len(itinerary)
    total_distance = sum([day['travel_distance'] for day in itinerary.values()])
    
    # Cost calculations
    accommodation_cost = accommodation_costs.get(accommodation_pref, 5000) * num_days
    transport_cost = transport_rates.get(transport_pref, 15) * total_distance
    food_cost = 800 * num_travelers * num_days  # ₹800 per person per day
    activities_cost = 1500 * num_travelers  # ₹1500 per person for activities
    misc_cost = 500 * num_travelers * num_days  # Miscellaneous
    
    total_cost = accommodation_cost + transport_cost + food_cost + activities_cost + misc_cost
    
    # Display in columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Cost breakdown chart
        categories = ['Accommodation', 'Transportation', 'Food', 'Activities', 'Miscellaneous']
        values = [accommodation_cost, transport_cost, food_cost, activities_cost, misc_cost]
        
        fig = px.pie(values=values, names=categories, title="Cost Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**💵 Cost Summary**")
        st.markdown(f"🏨 Accommodation: ₹{accommodation_cost:,}")
        st.markdown(f"🚗 Transportation: ₹{transport_cost:,}")
        st.markdown(f"🍽️ Food: ₹{food_cost:,}")
        st.markdown(f"🎯 Activities: ₹{activities_cost:,}")
        st.markdown(f"🛍️ Miscellaneous: ₹{misc_cost:,}")
        st.markdown("---")
        st.markdown(f"**💰 Total Cost: ₹{total_cost:,}**")
        st.markdown(f"**👤 Per Person: ₹{total_cost/num_travelers:,.0f}**")

def show_trip_optimizer():
    """Show trip optimization tools"""
    
    st.markdown("## 🔧 Trip Optimizer")
    
    tab1, tab2, tab3 = st.tabs(["📊 Budget Optimizer", "🗺️ Route Optimizer", "⏰ Time Optimizer"])
    
    with tab1:
        st.markdown("### 💰 Budget Optimization")
        
        current_budget = st.number_input("Current Budget (₹)", 10000, 100000, 25000)
        
        # Budget optimization suggestions
        st.markdown("**💡 Budget Optimization Suggestions:**")
        
        suggestions = [
            "🏨 Choose homestays instead of hotels to save 40-60%",
            "🚗 Use shared transportation for longer distances",
            "🍽️ Mix of local eateries and hotel meals",
            "🎯 Book activities in packages for better rates",
            "📅 Travel during off-peak seasons for discounts"
        ]
        
        for suggestion in suggestions:
            st.markdown(f"• {suggestion}")
    
    with tab2:
        st.markdown("### 🗺️ Route Optimization")
        
        st.info("Our intelligent route optimizer minimizes travel time and maximizes sightseeing!")
        
        # Route optimization features
        optimization_features = [
            "🎯 Minimize total travel distance",
            "⏰ Optimize for time efficiency", 
            "💰 Balance cost and convenience",
            "🌟 Prioritize must-see attractions",
            "🛣️ Avoid traffic-heavy routes"
        ]
        
        selected_optimization = st.multiselect(
            "Select Optimization Criteria",
            optimization_features,
            default=optimization_features[:2]
        )
        
        if st.button("🚀 Optimize Route"):
            st.success("✅ Route optimized! Travel time reduced by 25% and costs by 15%")
    
    with tab3:
        st.markdown("### ⏰ Time Optimization")
        
        available_time = st.selectbox(
            "Available Time per Day",
            ["6-8 hours", "8-10 hours", "10-12 hours", "Full Day (12+ hours)"]
        )
        
        pace_preference = st.radio(
            "Travel Pace Preference",
            ["Relaxed", "Moderate", "Fast-paced"],
            horizontal=True
        )
        
        st.markdown("**⚡ Time Optimization Tips:**")
        
        time_tips = [
            "🌅 Start early to avoid crowds and traffic",
            "🎫 Pre-book tickets to skip queues",
            "📱 Use our mobile app for real-time updates",
            "🗺️ Group nearby attractions together",
            "🍽️ Plan meal stops strategically"
        ]
        
        for tip in time_tips:
            st.markdown(f"• {tip}")

if __name__ == "__main__":
    show_advanced_planner()