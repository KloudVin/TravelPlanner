"""
Utility functions for the Karnataka Travel Planner
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import folium
from folium import plugins
import json

def calculate_trip_cost(num_people, days, accommodation_type, transport_type, meal_plan="breakfast"):
    """Calculate estimated trip cost based on parameters"""
    
    # Base costs per person per day
    accommodation_costs = {
        "3_star": 3000,
        "4_star": 6000, 
        "5_star": 12000,
        "heritage": 8000,
        "homestay": 2500,
        "resort": 10000
    }
    
    transport_costs = {
        "sedan": 12,  # per km
        "suv": 16,
        "tempo": 22,
        "bus": 35
    }
    
    meal_costs = {
        "breakfast": 300,
        "half_board": 800,
        "full_board": 1200,
        "all_inclusive": 1500
    }
    
    # Calculate costs
    accommodation_cost = accommodation_costs.get(accommodation_type, 3000) * days
    transport_cost = transport_costs.get(transport_type, 12) * 200 * days  # Assuming 200km per day
    meal_cost = meal_costs.get(meal_plan, 300) * num_people * days
    
    # Additional costs
    activity_cost = 1500 * num_people  # Average activity cost per person
    misc_cost = 500 * num_people * days  # Miscellaneous expenses
    
    total_cost = accommodation_cost + transport_cost + meal_cost + activity_cost + misc_cost
    
    return {
        "accommodation": accommodation_cost,
        "transport": transport_cost,
        "meals": meal_cost,
        "activities": activity_cost,
        "miscellaneous": misc_cost,
        "total": total_cost,
        "per_person": total_cost / num_people
    }

def create_destination_map(destinations, center_lat=12.9716, center_lon=77.5946):
    """Create an interactive map with destinations"""
    
    m = folium.Map(location=[center_lat, center_lon], zoom_start=8)
    
    # Add Bangalore marker (starting point)
    folium.Marker(
        [12.9716, 77.5946],
        popup="Bangalore - Starting Point",
        tooltip="Bangalore",
        icon=folium.Icon(color='red', icon='home', prefix='fa')
    ).add_to(m)
    
    # Add destination markers
    for dest in destinations:
        color = get_marker_color(dest.get('category', 'other'))
        
        folium.Marker(
            [dest['coordinates']['lat'], dest['coordinates']['lon']],
            popup=f"""
            <b>{dest['name']}</b><br>
            Distance: {dest['distance_km']}km<br>
            Category: {dest['category']}<br>
            Best Time: {dest.get('best_time', 'Anytime')}
            """,
            tooltip=dest['name'],
            icon=folium.Icon(color=color, icon='map-pin', prefix='fa')
        ).add_to(m)
    
    return m

def get_marker_color(category):
    """Get marker color based on destination category"""
    color_map = {
        'Hill Station': 'green',
        'Wildlife': 'orange', 
        'Trekking': 'purple',
        'Adventure': 'red',
        'Theme Park': 'pink',
        'Waterfalls': 'blue',
        'Heritage': 'darkred',
        'Beach': 'lightblue',
        'Spiritual': 'gray'
    }
    return color_map.get(category, 'blue')

def filter_destinations(destinations, filters):
    """Filter destinations based on user criteria"""
    filtered = destinations.copy()
    
    if filters.get('category') and filters['category'] != 'All':
        filtered = [d for d in filtered if d['category'] == filters['category']]
    
    if filters.get('max_distance'):
        filtered = [d for d in filtered if d['distance_km'] <= filters['max_distance']]
    
    if filters.get('difficulty') and filters['difficulty'] != 'All':
        filtered = [d for d in filtered if d.get('difficulty') == filters['difficulty']]
    
    if filters.get('season') and filters['season'] != 'All':
        filtered = [d for d in filtered if filters['season'] in d.get('best_season', '')]
    
    return filtered

def generate_itinerary(destinations, days, preferences):
    """Generate a suggested itinerary based on destinations and preferences"""
    
    itinerary = {}
    
    # Simple algorithm to distribute destinations across days
    destinations_per_day = len(destinations) // days
    remainder = len(destinations) % days
    
    start_idx = 0
    for day in range(1, days + 1):
        end_idx = start_idx + destinations_per_day
        if remainder > 0:
            end_idx += 1
            remainder -= 1
        
        day_destinations = destinations[start_idx:end_idx]
        
        itinerary[f"Day {day}"] = {
            "destinations": day_destinations,
            "activities": [],
            "estimated_time": "8-10 hours",
            "travel_distance": sum([d['distance_km'] for d in day_destinations])
        }
        
        start_idx = end_idx
    
    return itinerary

def save_itinerary(itinerary_data):
    """Save itinerary to session state"""
    if 'saved_itineraries' not in st.session_state:
        st.session_state.saved_itineraries = []
    
    itinerary_data['created_date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    st.session_state.saved_itineraries.append(itinerary_data)
    
    return True

def load_saved_itineraries():
    """Load saved itineraries from session state"""
    return st.session_state.get('saved_itineraries', [])

def format_currency(amount):
    """Format currency in Indian Rupees"""
    return f"₹{amount:,.0f}"

def calculate_distance_matrix(destinations):
    """Calculate distance matrix between destinations (simplified)"""
    # This is a simplified version - in production, you'd use Google Maps API
    matrix = {}
    
    for i, dest1 in enumerate(destinations):
        matrix[dest1['name']] = {}
        for j, dest2 in enumerate(destinations):
            if i == j:
                matrix[dest1['name']][dest2['name']] = 0
            else:
                # Simplified distance calculation
                lat1, lon1 = dest1['coordinates']['lat'], dest1['coordinates']['lon']
                lat2, lon2 = dest2['coordinates']['lat'], dest2['coordinates']['lon']
                
                # Haversine formula (simplified)
                distance = ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5 * 111  # Rough km conversion
                matrix[dest1['name']][dest2['name']] = round(distance, 1)
    
    return matrix

def get_weather_info(destination, date=None):
    """Get weather information for destination (mock data)"""
    # In production, integrate with weather API
    weather_data = {
        "temperature": "25°C - 32°C",
        "condition": "Partly Cloudy",
        "humidity": "65%",
        "rainfall": "Low",
        "recommendation": "Perfect weather for sightseeing!"
    }
    
    return weather_data

def validate_trip_dates(start_date, end_date):
    """Validate trip dates"""
    if start_date < datetime.now().date():
        return False, "Start date cannot be in the past"
    
    if end_date <= start_date:
        return False, "End date must be after start date"
    
    if (end_date - start_date).days > 30:
        return False, "Trip duration cannot exceed 30 days"
    
    return True, "Valid dates"

def generate_packing_list(destinations, season, activities):
    """Generate packing list based on trip details"""
    
    base_items = [
        "Comfortable walking shoes",
        "Sunscreen and sunglasses", 
        "Personal medications",
        "Phone charger and power bank",
        "Camera",
        "Valid ID proof",
        "Cash and cards"
    ]
    
    seasonal_items = {
        "summer": ["Light cotton clothes", "Hat/cap", "Water bottle", "Cooling towel"],
        "winter": ["Warm clothes", "Jacket", "Gloves", "Warm socks"],
        "monsoon": ["Raincoat/umbrella", "Waterproof bag", "Quick-dry clothes", "Extra footwear"]
    }
    
    activity_items = {
        "trekking": ["Trekking shoes", "Backpack", "First aid kit", "Torch/headlamp"],
        "beach": ["Swimwear", "Beach towel", "Flip-flops", "Waterproof phone case"],
        "wildlife": ["Binoculars", "Neutral colored clothes", "Insect repellent"],
        "heritage": ["Comfortable walking shoes", "Modest clothing", "Guidebook"]
    }
    
    packing_list = base_items.copy()
    
    # Add seasonal items
    current_season = get_current_season()
    if current_season in seasonal_items:
        packing_list.extend(seasonal_items[current_season])
    
    # Add activity-specific items
    for activity in activities:
        if activity.lower() in activity_items:
            packing_list.extend(activity_items[activity.lower()])
    
    return list(set(packing_list))  # Remove duplicates

def get_current_season():
    """Determine current season based on month"""
    month = datetime.now().month
    
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "summer"
    elif month in [6, 7, 8, 9]:
        return "monsoon"
    else:
        return "winter"  # Oct-Nov

def create_expense_tracker():
    """Create expense tracking functionality"""
    if 'trip_expenses' not in st.session_state:
        st.session_state.trip_expenses = []
    
    return st.session_state.trip_expenses

def add_expense(category, amount, description, date=None):
    """Add expense to tracker"""
    if 'trip_expenses' not in st.session_state:
        st.session_state.trip_expenses = []
    
    expense = {
        "category": category,
        "amount": amount,
        "description": description,
        "date": date or datetime.now().strftime("%Y-%m-%d"),
        "timestamp": datetime.now().isoformat()
    }
    
    st.session_state.trip_expenses.append(expense)
    return True

def get_expense_summary():
    """Get expense summary by category"""
    expenses = st.session_state.get('trip_expenses', [])
    
    summary = {}
    total = 0
    
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        
        if category not in summary:
            summary[category] = 0
        
        summary[category] += amount
        total += amount
    
    return summary, total