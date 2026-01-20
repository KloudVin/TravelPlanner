"""
Karnataka Tourism Destinations Data - Comprehensive Collection
Including famous destinations and hidden gems with multimedia content
"""

from services.photo_service import get_curated_photos, get_destination_video

# Karnataka Tourism Video URLs
KARNATAKA_VIDEOS = {
    "banner": "https://www.youtube.com/embed/VIDEO_ID_HERE",  # Replace with actual Karnataka tourism video
    "mysore_palace": "https://www.youtube.com/embed/VIDEO_ID_HERE",
    "hampi": "https://www.youtube.com/embed/VIDEO_ID_HERE",
    "coorg": "https://www.youtube.com/embed/VIDEO_ID_HERE",
    "badami": "https://www.youtube.com/embed/VIDEO_ID_HERE",
    "chikmagalur": "https://www.youtube.com/embed/VIDEO_ID_HERE",
    "dandeli": "https://www.youtube.com/embed/VIDEO_ID_HERE",
    "maravanthe": "https://www.youtube.com/embed/VIDEO_ID_HERE"
}

# Photo and video URLs for destinations
def get_destination_media(destination_name, media_type="photo"):
    """Generate media URLs for destinations"""
    if media_type == "photo":
        return get_curated_photos(destination_name)
    elif media_type == "video":
        return get_destination_video(destination_name)
    return None

# Day trip destinations within 100km of Bangalore
DAY_TRIP_DESTINATIONS = [
    {
        "id": 1,
        "name": "Nandi Hills",
        "distance_km": 60,
        "coordinates": {"lat": 13.3703, "lon": 77.6838},
        "category": "Hill Station",
        "best_time": "Early Morning (5 AM - 9 AM)",
        "entry_fee": 30,
        "highlights": ["Sunrise Point", "Tipu's Drop", "Bhoga Nandeeshwara Temple", "Paragliding"],
        "activities": ["Trekking", "Photography", "Paragliding", "Temple Visit"],
        "estimated_time": "6-8 hours",
        "difficulty": "Easy to Moderate",
        "best_season": "October to March",
        "facilities": ["Parking", "Restrooms", "Food Stalls", "Guide Services"]
    },
    {
        "id": 2,
        "name": "Bannerghatta National Park",
        "distance_km": 25,
        "coordinates": {"lat": 12.7993, "lon": 77.5769},
        "category": "Wildlife",
        "best_time": "9 AM - 5 PM",
        "entry_fee": 80,
        "highlights": ["Lion Safari", "Tiger Safari", "Bear Rescue Center", "Butterfly Park"],
        "activities": ["Safari", "Zoo Visit", "Nature Walk", "Photography"],
        "estimated_time": "4-6 hours",
        "difficulty": "Easy",
        "best_season": "Year Round",
        "facilities": ["Parking", "Cafeteria", "Gift Shop", "Battery Car"]
    },
    {
        "id": 3,
        "name": "Skandagiri (Kalavara Durga)",
        "distance_km": 62,
        "coordinates": {"lat": 13.4067, "lon": 77.6833},
        "category": "Trekking",
        "best_time": "Night Trek (2 AM - 7 AM)",
        "entry_fee": 300,
        "highlights": ["Sunrise Trek", "Ancient Fort Ruins", "Cloud Walking", "360° View"],
        "activities": ["Night Trekking", "Photography", "Camping", "Stargazing"],
        "estimated_time": "8-10 hours",
        "difficulty": "Moderate to Difficult",
        "best_season": "October to February",
        "facilities": ["Guide Mandatory", "Basic Restrooms", "Parking"]
    },
    {
        "id": 4,
        "name": "Savandurga",
        "distance_km": 50,
        "coordinates": {"lat": 12.9167, "lon": 77.2833},
        "category": "Adventure",
        "best_time": "6 AM - 6 PM",
        "entry_fee": 25,
        "highlights": ["Asia's Largest Monolith", "Rock Climbing", "Arkavathi River", "Narasimha Temple"],
        "activities": ["Rock Climbing", "Trekking", "River Activities", "Temple Visit"],
        "estimated_time": "6-8 hours",
        "difficulty": "Moderate to Difficult",
        "best_season": "October to March",
        "facilities": ["Parking", "Basic Facilities", "Guide Available"]
    },
    {
        "id": 5,
        "name": "Wonderla Amusement Park",
        "distance_km": 28,
        "coordinates": {"lat": 12.8347, "lon": 77.3997},
        "category": "Theme Park",
        "best_time": "10 AM - 6 PM",
        "entry_fee": 1099,
        "highlights": ["Water Rides", "Dry Rides", "Wave Pool", "Rain Disco"],
        "activities": ["Water Sports", "Rides", "Games", "Entertainment Shows"],
        "estimated_time": "8-10 hours",
        "difficulty": "Easy",
        "best_season": "Year Round",
        "facilities": ["Parking", "Restaurants", "Lockers", "First Aid", "Shopping"]
    },
    {
        "id": 6,
        "name": "Shivanasamudra Falls",
        "distance_km": 85,
        "coordinates": {"lat": 12.2833, "lon": 77.1833},
        "category": "Waterfalls",
        "best_time": "8 AM - 6 PM",
        "entry_fee": 20,
        "highlights": ["Gaganachukki Falls", "Bharachukki Falls", "Hydroelectric Plant", "Coracle Ride"],
        "activities": ["Sightseeing", "Photography", "Coracle Ride", "Picnic"],
        "estimated_time": "6-8 hours",
        "difficulty": "Easy",
        "best_season": "July to February",
        "facilities": ["Parking", "Restrooms", "Food Stalls", "Boat Services"]
    },
    {
        "id": 7,
        "name": "Bheemeshwari",
        "distance_km": 95,
        "coordinates": {"lat": 12.4167, "lon": 77.0833},
        "category": "Adventure",
        "best_time": "6 AM - 6 PM",
        "entry_fee": 50,
        "highlights": ["River Rafting", "Angling", "Crocodile Spotting", "Nature Camp"],
        "activities": ["River Rafting", "Fishing", "Kayaking", "Wildlife Spotting"],
        "estimated_time": "8-10 hours",
        "difficulty": "Moderate",
        "best_season": "October to March",
        "facilities": ["Adventure Gear", "Guides", "Camping", "Restaurant"]
    },
    {
        "id": 8,
        "name": "Ramanagara",
        "distance_km": 50,
        "coordinates": {"lat": 12.7167, "lon": 77.2833},
        "category": "Adventure",
        "best_time": "6 AM - 6 PM",
        "entry_fee": 100,
        "highlights": ["Rock Climbing", "Rappelling", "Sholay Rocks", "Silk Farming"],
        "activities": ["Rock Climbing", "Rappelling", "Trekking", "Photography"],
        "estimated_time": "6-8 hours",
        "difficulty": "Moderate",
        "best_season": "October to March",
        "facilities": ["Adventure Gear Rental", "Instructors", "Parking", "Food"],
        "photos": [get_destination_media("Ramanagara", "photo")],
        "videos": [get_destination_media("Ramanagara", "video")]
    },
    # Hidden Gems - Lesser Known Destinations
    {
        "id": 9,
        "name": "Kailasagiri Hill & Cave Temple",
        "distance_km": 80,
        "coordinates": {"lat": 13.4000, "lon": 78.0500},
        "category": "Spiritual",
        "best_time": "6 AM - 6 PM",
        "entry_fee": 0,
        "highlights": ["Ancient Cave Temple", "Chathurmukhalingeshwara", "Pandava Connection", "Bhima Bakasura Legend"],
        "activities": ["Temple Visit", "Cave Exploration", "Trekking", "Photography", "Spiritual Experience"],
        "estimated_time": "4-6 hours",
        "difficulty": "Moderate",
        "best_season": "October to March",
        "facilities": ["Parking", "Basic Facilities", "Stone Path"],
        "description": "Hidden gem near Chintamani featuring a man-made cave temple with three shrines dedicated to Lord Shiva (Chathurmukhalingeshwara), Goddess Parvathi, and Lord Ganesha. Legend says Pandavas lived here during exile.",
        "photos": [get_destination_media("Kailasagiri Cave Temple", "photo")],
        "videos": [get_destination_media("Kailasagiri Cave Temple", "video")],
        "hidden_gem": True
    },
    {
        "id": 10,
        "name": "Antaragange",
        "distance_km": 70,
        "coordinates": {"lat": 13.7167, "lon": 78.1167},
        "category": "Adventure",
        "best_time": "6 AM - 6 PM",
        "entry_fee": 20,
        "highlights": ["Cave Exploration", "Rock Formation", "Perennial Spring", "Night Trek"],
        "activities": ["Cave Exploration", "Rock Climbing", "Night Trekking", "Photography"],
        "estimated_time": "6-8 hours",
        "difficulty": "Moderate to Difficult",
        "best_season": "October to March",
        "facilities": ["Parking", "Guide Services", "Basic Facilities"],
        "description": "Volcanic rock formation with natural caves and a perennial water source. Popular for cave exploration and night treks.",
        "photos": [get_destination_media("Antaragange", "photo")],
        "videos": [get_destination_media("Antaragange", "video")],
        "hidden_gem": True
    },
    {
        "id": 11,
        "name": "Devarayanadurga",
        "distance_km": 65,
        "coordinates": {"lat": 13.3667, "lon": 77.2833},
        "category": "Hill Station",
        "best_time": "6 AM - 6 PM",
        "entry_fee": 15,
        "highlights": ["Yoga Narasimha Temple", "Bhoga Narasimha Temple", "Natural Spring", "Sunrise Point"],
        "activities": ["Temple Visit", "Trekking", "Photography", "Meditation"],
        "estimated_time": "6-8 hours",
        "difficulty": "Easy to Moderate",
        "best_season": "October to March",
        "facilities": ["Parking", "Restrooms", "Food Stalls", "Temple Facilities"],
        "description": "Hill station at 3940 feet with ancient temples and natural spring called Namada Chilume.",
        "photos": [get_destination_media("Devarayanadurga", "photo")],
        "videos": [get_destination_media("Devarayanadurga", "video")],
        "hidden_gem": True
    },
    {
        "id": 12,
        "name": "Makalidurga",
        "distance_km": 60,
        "coordinates": {"lat": 13.2167, "lon": 77.6833},
        "category": "Trekking",
        "best_time": "5 AM - 7 PM",
        "entry_fee": 25,
        "highlights": ["Ancient Fort", "Railway Track Trek", "Sunrise View", "Rock Formations"],
        "activities": ["Trekking", "Fort Exploration", "Photography", "Railway Track Walk"],
        "estimated_time": "6-8 hours",
        "difficulty": "Moderate",
        "best_season": "October to March",
        "facilities": ["Railway Station", "Basic Facilities", "Parking"],
        "description": "Unique trek that starts from a railway station and leads to an ancient hilltop fort with panoramic views.",
        "photos": [get_destination_media("Makalidurga", "photo")],
        "videos": [get_destination_media("Makalidurga", "video")],
        "hidden_gem": True
    }
]

# Multi-day tour destinations
MULTI_DAY_DESTINATIONS = [
    {
        "id": 101,
        "name": "Mysore",
        "distance_km": 150,
        "coordinates": {"lat": 12.2958, "lon": 76.6394},
        "category": "Heritage",
        "min_days": 2,
        "highlights": ["Mysore Palace", "Chamundi Hills", "Brindavan Gardens", "St. Philomena's Church"],
        "activities": ["Palace Tour", "Temple Visit", "Garden Walk", "Shopping"],
        "best_season": "October to March",
        "famous_for": "Royal Heritage, Silk Sarees, Sandalwood",
        "photos": [get_destination_media("Mysore Palace", "photo")],
        "videos": [get_destination_media("Mysore Palace", "video")]
    },
    {
        "id": 102,
        "name": "Coorg (Kodagu)",
        "distance_km": 260,
        "coordinates": {"lat": 12.3375, "lon": 75.8069},
        "category": "Hill Station",
        "min_days": 2,
        "highlights": ["Coffee Plantations", "Abbey Falls", "Raja's Seat", "Dubare Elephant Camp"],
        "activities": ["Plantation Tour", "Elephant Interaction", "River Rafting", "Trekking"],
        "best_season": "October to March",
        "famous_for": "Coffee, Spices, Natural Beauty",
        "photos": [get_destination_media("Coorg Coffee Plantation", "photo")],
        "videos": [get_destination_media("Coorg Coffee Plantation", "video")]
    },
    {
        "id": 103,
        "name": "Hampi",
        "distance_km": 340,
        "coordinates": {"lat": 15.3350, "lon": 76.4600},
        "category": "Heritage",
        "min_days": 2,
        "highlights": ["Vijayanagara Ruins", "Vittala Temple", "Hampi Bazaar", "Matanga Hill"],
        "activities": ["Heritage Walk", "Coracle Ride", "Rock Climbing", "Photography"],
        "best_season": "October to February",
        "famous_for": "UNESCO World Heritage Site, Ancient Architecture",
        "photos": [get_destination_media("Hampi Vittala Temple", "photo")],
        "videos": [get_destination_media("Hampi Vittala Temple", "video")]
    },
    {
        "id": 104,
        "name": "Gokarna",
        "distance_km": 485,
        "coordinates": {"lat": 14.5492, "lon": 74.3200},
        "category": "Beach",
        "min_days": 2,
        "highlights": ["Om Beach", "Kudle Beach", "Mahabaleshwar Temple", "Half Moon Beach"],
        "activities": ["Beach Activities", "Temple Visit", "Trekking", "Water Sports"],
        "best_season": "October to March",
        "famous_for": "Pristine Beaches, Spiritual Significance",
        "photos": [get_destination_media("Gokarna Om Beach", "photo")],
        "videos": [get_destination_media("Gokarna Om Beach", "video")]
    },
    {
        "id": 105,
        "name": "Chikmagalur",
        "distance_km": 245,
        "coordinates": {"lat": 13.3161, "lon": 75.7720},
        "category": "Hill Station",
        "min_days": 2,
        "highlights": ["Mullayanagiri Peak", "Baba Budangiri", "Coffee Plantations", "Hebbe Falls"],
        "activities": ["Trekking", "Plantation Tour", "Waterfall Visit", "Wildlife Safari"],
        "best_season": "September to March",
        "famous_for": "Coffee Origin, Trekking, Natural Beauty",
        "photos": [get_destination_media("Chikmagalur Mullayanagiri", "photo")],
        "videos": [get_destination_media("Chikmagalur Mullayanagiri", "video")]
    },
    # Hidden Gems - Multi-day destinations
    {
        "id": 106,
        "name": "Agumbe",
        "distance_km": 350,
        "coordinates": {"lat": 13.5167, "lon": 75.1000},
        "category": "Hill Station",
        "min_days": 2,
        "highlights": ["Sunset Point", "Rainforest", "Barkana Falls", "Onake Abbi Falls"],
        "activities": ["Rainforest Trek", "Waterfall Visit", "Sunset Viewing", "Wildlife Spotting"],
        "best_season": "October to March",
        "famous_for": "Cherrapunji of South India, Rainforest",
        "description": "Known as the Cherrapunji of South India, Agumbe receives the highest rainfall in Karnataka and offers stunning sunset views.",
        "photos": [get_destination_media("Agumbe Sunset", "photo")],
        "videos": [get_destination_media("Agumbe Sunset", "video")],
        "hidden_gem": True
    },
    {
        "id": 107,
        "name": "Yana Rocks",
        "distance_km": 520,
        "coordinates": {"lat": 14.5500, "lon": 74.6167},
        "category": "Adventure",
        "min_days": 1,
        "highlights": ["Unique Rock Formations", "Bhairaveshwara Shikhara", "Mohini Shikhara", "Cave Temple"],
        "activities": ["Rock Climbing", "Cave Exploration", "Trekking", "Photography"],
        "best_season": "October to March",
        "famous_for": "Unique Limestone Rock Formations",
        "description": "Unique limestone rock formations rising 90m high, accessible through dense forest trek.",
        "photos": [get_destination_media("Yana Rocks", "photo")],
        "videos": [get_destination_media("Yana Rocks", "video")],
        "hidden_gem": True
    },
    {
        "id": 108,
        "name": "Kudremukh",
        "distance_km": 320,
        "coordinates": {"lat": 13.2500, "lon": 75.0167},
        "category": "Trekking",
        "min_days": 2,
        "highlights": ["Kudremukh Peak", "National Park", "Hanuman Gundi Falls", "Kalasa Temple"],
        "activities": ["Trekking", "Wildlife Safari", "Waterfall Visit", "Temple Visit"],
        "best_season": "October to March",
        "famous_for": "Horse Face Peak, Biodiversity",
        "description": "Peak resembling a horse's face, part of Western Ghats with rich biodiversity.",
        "photos": [get_destination_media("Kudremukh Peak", "photo")],
        "videos": [get_destination_media("Kudremukh Peak", "video")],
        "hidden_gem": True
    },
    {
        "id": 109,
        "name": "Netravati Peak",
        "distance_km": 330,
        "coordinates": {"lat": 13.1500, "lon": 75.0500},
        "category": "Trekking",
        "min_days": 2,
        "highlights": ["Untouched Wilderness", "Western Ghats Views", "Rare Flora", "Pristine Trails"],
        "activities": ["Wilderness Trekking", "Bird Watching", "Photography", "Camping"],
        "best_season": "October to February",
        "famous_for": "Offbeat Trekking, Raw Wilderness",
        "description": "Hidden deep within Kudremukh National Park, this offbeat trail offers unspoiled Western Ghats views.",
        "photos": [get_destination_media("Netravati Peak", "photo")],
        "videos": [get_destination_media("Netravati Peak", "video")],
        "hidden_gem": True
    },
    {
        "id": 110,
        "name": "Sakleshpur",
        "distance_km": 220,
        "coordinates": {"lat": 12.9444, "lon": 75.7847},
        "category": "Hill Station",
        "min_days": 2,
        "highlights": ["Railway Trek", "Coffee Estates", "Manjarabad Fort", "Green Route"],
        "activities": ["Railway Track Trekking", "Plantation Visit", "Fort Exploration", "Nature Walk"],
        "best_season": "October to March",
        "famous_for": "Railway Trek, Coffee Plantations",
        "description": "Hill station famous for railway track trekking through tunnels and bridges amidst coffee plantations.",
        "photos": [get_destination_media("Sakleshpur Railway Trek", "photo")],
        "videos": [get_destination_media("Sakleshpur Railway Trek", "video")],
        "hidden_gem": True
    }
]

# Accommodation categories
ACCOMMODATION_TYPES = {
    "3_star": {
        "name": "3-Star Hotels",
        "price_range": "₹2,000 - ₹4,000",
        "amenities": ["AC", "WiFi", "Restaurant", "Room Service"],
        "description": "Comfortable stay with essential amenities"
    },
    "4_star": {
        "name": "4-Star Hotels", 
        "price_range": "₹4,000 - ₹8,000",
        "amenities": ["AC", "WiFi", "Restaurant", "Pool", "Gym", "Spa"],
        "description": "Premium comfort with luxury amenities"
    },
    "5_star": {
        "name": "5-Star Hotels",
        "price_range": "₹8,000 - ₹20,000",
        "amenities": ["AC", "WiFi", "Multiple Restaurants", "Pool", "Spa", "Concierge", "Butler Service"],
        "description": "Luxury accommodation with world-class service"
    },
    "heritage": {
        "name": "Heritage Hotels",
        "price_range": "₹5,000 - ₹15,000",
        "amenities": ["AC", "WiFi", "Restaurant", "Heritage Architecture", "Cultural Programs"],
        "description": "Stay in converted palaces and heritage properties"
    },
    "homestay": {
        "name": "Homestays",
        "price_range": "₹1,500 - ₹3,500",
        "amenities": ["Home-cooked Meals", "Local Experience", "WiFi", "Family Interaction"],
        "description": "Authentic local experience with families"
    },
    "resort": {
        "name": "Resorts",
        "price_range": "₹6,000 - ₹18,000",
        "amenities": ["AC", "WiFi", "Pool", "Spa", "Adventure Activities", "Multiple Restaurants"],
        "description": "All-inclusive experience with recreational facilities"
    }
}

# Transportation options
TRANSPORT_OPTIONS = [
    {
        "type": "AC Sedan",
        "capacity": "4 passengers",
        "rate_per_km": 12,
        "features": ["AC", "Professional Driver", "Fuel Included", "Toll Included"],
        "best_for": "Couples, Small Families",
        "vehicles": ["Swift Dzire", "Honda Amaze", "Hyundai Xcent"]
    },
    {
        "type": "AC SUV",
        "capacity": "6-7 passengers", 
        "rate_per_km": 16,
        "features": ["AC", "Spacious", "Large Luggage Space", "Professional Driver"],
        "best_for": "Families, Small Groups",
        "vehicles": ["Toyota Innova", "Mahindra Xylo", "Marazzo"]
    },
    {
        "type": "Tempo Traveller",
        "capacity": "12 passengers",
        "rate_per_km": 22,
        "features": ["AC", "Comfortable Seating", "Large Luggage Space", "Entertainment System"],
        "best_for": "Large Groups, Corporate",
        "vehicles": ["Force Traveller", "Mahindra Tourister"]
    },
    {
        "type": "AC Bus",
        "capacity": "25+ passengers",
        "rate_per_km": 35,
        "features": ["AC", "Reclining Seats", "Entertainment System", "Washroom"],
        "best_for": "Large Groups, Events",
        "vehicles": ["Volvo", "Mercedes", "Ashok Leyland"]
    }
]

# Sample tour packages
TOUR_PACKAGES = {
    "2_3_days": [
        {
            "id": "PKG001",
            "title": "Mysore-Coorg Heritage Trail",
            "duration": "3 Days / 2 Nights",
            "base_price": 8500,
            "destinations": ["Mysore", "Coorg"],
            "itinerary": {
                "day1": "Bangalore → Mysore Palace → Chamundi Hills → Hotel Check-in",
                "day2": "Mysore → Coorg → Coffee Plantation Tour → Abbey Falls",
                "day3": "Raja's Seat → Dubare Elephant Camp → Return to Bangalore"
            },
            "includes": ["AC Transport", "Hotel Stay", "Breakfast", "Sightseeing", "Entry Tickets"],
            "excludes": ["Lunch", "Dinner", "Personal Expenses", "Camera Charges"],
            "themes": ["Heritage", "Nature", "Culture"]
        },
        {
            "id": "PKG002", 
            "title": "Chikmagalur Coffee & Hills",
            "duration": "2 Days / 1 Night",
            "base_price": 6500,
            "destinations": ["Chikmagalur"],
            "itinerary": {
                "day1": "Bangalore → Mullayanagiri Trek → Coffee Plantation → Hotel",
                "day2": "Baba Budangiri → Hebbe Falls → Return to Bangalore"
            },
            "includes": ["AC Transport", "Hotel Stay", "Breakfast", "Plantation Tour"],
            "excludes": ["Meals", "Personal Expenses", "Adventure Activity Charges"],
            "themes": ["Adventure", "Nature", "Coffee Culture"]
        }
    ],
    "4_5_days": [
        {
            "id": "PKG003",
            "title": "Hampi Heritage Circuit",
            "duration": "4 Days / 3 Nights", 
            "base_price": 15500,
            "destinations": ["Hampi", "Badami", "Aihole"],
            "itinerary": {
                "day1": "Bangalore → Hampi → Virupaksha Temple → Hampi Bazaar",
                "day2": "Vittala Temple → Royal Enclosure → Matanga Hill Sunset",
                "day3": "Hampi → Badami → Cave Temples → Agastya Lake",
                "day4": "Aihole → Pattadakal → Return to Bangalore"
            },
            "includes": ["AC Transport", "Hotel Stay", "Breakfast", "Guide Services", "Entry Tickets"],
            "excludes": ["Lunch", "Dinner", "Personal Expenses"],
            "themes": ["Heritage", "Architecture", "History"]
        }
    ],
    "6_plus_days": [
        {
            "id": "PKG004",
            "title": "Complete Karnataka Explorer",
            "duration": "7 Days / 6 Nights",
            "base_price": 28500,
            "destinations": ["Mysore", "Coorg", "Hampi", "Gokarna", "Udupi"],
            "itinerary": {
                "day1": "Bangalore → Mysore → Palace → Chamundi Hills",
                "day2": "Mysore → Coorg → Coffee Plantation → Abbey Falls",
                "day3": "Coorg → Hampi → Check-in → Evening Exploration",
                "day4": "Hampi Full Day → Vittala Temple → Royal Enclosure",
                "day5": "Hampi → Gokarna → Beach Time → Temple Visit",
                "day6": "Gokarna → Udupi → Krishna Temple → Beach",
                "day7": "Udupi → Bangalore via Coastal Route"
            },
            "includes": ["AC Transport", "Hotel Stay", "Breakfast", "Guide Services", "Entry Tickets"],
            "excludes": ["Lunch", "Dinner", "Personal Expenses", "Water Sports"],
            "themes": ["Heritage", "Nature", "Beach", "Culture", "Spiritual"]
        }
    ]
}

# Comprehensive Waterfalls Database
KARNATAKA_WATERFALLS = [
    {
        "id": 201,
        "name": "Jog Falls",
        "district": "Shivamogga",
        "height": "253 meters",
        "distance_from_bangalore": 400,
        "coordinates": {"lat": 14.2281, "lon": 74.7644},
        "best_time": "July to January",
        "highlights": ["Second highest waterfall in India", "Four cascades: Raja, Rani, Rocket, Roarer"],
        "activities": ["Sightseeing", "Photography", "Trekking"],
        "entry_fee": 25,
        "facilities": ["Parking", "Viewpoints", "Cafeteria", "Restrooms"],
        "photos": [get_destination_media("Jog Falls", "photo")],
        "videos": [get_destination_media("Jog Falls", "video")],
        "description": "The crown jewel of Karnataka waterfalls, Jog Falls plunges 253 meters in four distinct streams."
    },
    {
        "id": 202,
        "name": "Abbey Falls",
        "district": "Kodagu",
        "height": "70 feet",
        "distance_from_bangalore": 270,
        "coordinates": {"lat": 12.4500, "lon": 75.7167},
        "best_time": "June to February",
        "highlights": ["Coffee plantation setting", "Hanging bridge view", "Spice gardens"],
        "activities": ["Photography", "Nature Walk", "Plantation Tour"],
        "entry_fee": 30,
        "facilities": ["Parking", "Hanging Bridge", "Spice Garden", "Cafeteria"],
        "photos": [get_destination_media("Abbey Falls", "photo")],
        "videos": [get_destination_media("Abbey Falls", "video")],
        "description": "Picturesque waterfall nestled amidst coffee and spice plantations in Coorg."
    },
    {
        "id": 203,
        "name": "Shivanasamudra Falls",
        "district": "Mandya",
        "height": "98 meters",
        "distance_from_bangalore": 135,
        "coordinates": {"lat": 12.2833, "lon": 77.1833},
        "best_time": "July to February",
        "highlights": ["Gaganachukki Falls", "Bharachukki Falls", "Asia's first hydroelectric power station"],
        "activities": ["Sightseeing", "Coracle Ride", "Photography", "Picnic"],
        "entry_fee": 20,
        "facilities": ["Parking", "Boat Services", "Viewpoints", "Food Stalls"],
        "photos": [get_destination_media("Shivanasamudra Falls", "photo")],
        "videos": [get_destination_media("Shivanasamudra Falls", "video")],
        "description": "Twin waterfalls on River Cauvery, site of Asia's first hydroelectric power station."
    },
    {
        "id": 204,
        "name": "Hebbe Falls",
        "district": "Chikmagalur",
        "height": "168 meters",
        "distance_from_bangalore": 300,
        "coordinates": {"lat": 13.4167, "lon": 75.7000},
        "best_time": "July to March",
        "highlights": ["Two-tier waterfall", "Coffee plantation trek", "Dodda Hebbe and Chikka Hebbe"],
        "activities": ["Trekking", "Photography", "Jeep Safari", "Swimming"],
        "entry_fee": 50,
        "facilities": ["Jeep Service", "Trekking Trails", "Basic Facilities"],
        "photos": [get_destination_media("Hebbe Falls", "photo")],
        "videos": [get_destination_media("Hebbe Falls", "video")],
        "description": "Two-tier waterfall accessible through coffee plantation trek near Kemmangundi."
    },
    {
        "id": 205,
        "name": "Iruppu Falls",
        "district": "Kodagu",
        "height": "170 feet",
        "distance_from_bangalore": 310,
        "coordinates": {"lat": 11.9167, "lon": 75.9833},
        "best_time": "June to February",
        "highlights": ["Sacred waterfall", "Rameshwara Temple", "Brahmagiri Wildlife Sanctuary"],
        "activities": ["Temple Visit", "Trekking", "Wildlife Spotting", "Photography"],
        "entry_fee": 25,
        "facilities": ["Temple", "Parking", "Trekking Trails", "Forest Department Rest House"],
        "photos": [get_destination_media("Iruppu Falls", "photo")],
        "videos": [get_destination_media("Iruppu Falls", "video")],
        "description": "Sacred waterfall in Brahmagiri range, associated with Rameshwara Temple."
    },
    # Hidden Waterfall Gems
    {
        "id": 206,
        "name": "Barkana Falls",
        "district": "Shivamogga",
        "height": "259 meters",
        "distance_from_bangalore": 380,
        "coordinates": {"lat": 13.5000, "lon": 75.1167},
        "best_time": "June to February",
        "highlights": ["10th highest waterfall in India", "Sita River", "Dense forest trek"],
        "activities": ["Trekking", "Photography", "Bird Watching", "Nature Study"],
        "entry_fee": 30,
        "facilities": ["Forest Trek", "Basic Facilities", "Guide Services"],
        "photos": [get_destination_media("Barkana Falls", "photo")],
        "videos": [get_destination_media("Barkana Falls", "video")],
        "description": "India's 10th highest waterfall, hidden in Agumbe rainforest, requires forest trek.",
        "hidden_gem": True
    },
    {
        "id": 207,
        "name": "Onake Abbi Falls",
        "district": "Shivamogga",
        "height": "116 meters",
        "distance_from_bangalore": 370,
        "coordinates": {"lat": 13.5167, "lon": 75.1000},
        "best_time": "June to February",
        "highlights": ["Pestle-shaped rock formation", "Agumbe rainforest", "Pristine nature"],
        "activities": ["Trekking", "Photography", "Rainforest Exploration"],
        "entry_fee": 25,
        "facilities": ["Forest Trek", "Basic Facilities"],
        "photos": [get_destination_media("Onake Abbi Falls", "photo")],
        "videos": [get_destination_media("Onake Abbi Falls", "video")],
        "description": "Named after pestle-shaped rock formation, hidden gem in Agumbe rainforest.",
        "hidden_gem": True
    },
    {
        "id": 208,
        "name": "Magod Falls",
        "district": "Uttara Kannada",
        "height": "200 meters",
        "distance_from_bangalore": 500,
        "coordinates": {"lat": 14.9167, "lon": 74.6167},
        "best_time": "June to February",
        "highlights": ["Bedthi River", "Two-stage waterfall", "Western Ghats"],
        "activities": ["Trekking", "Photography", "Nature Walk"],
        "entry_fee": 20,
        "facilities": ["Viewpoints", "Trekking Trails", "Basic Facilities"],
        "photos": [get_destination_media("Magod Falls", "photo")],
        "videos": [get_destination_media("Magod Falls", "video")],
        "description": "Two-stage waterfall on Bedthi River, relatively unexplored gem in Western Ghats.",
        "hidden_gem": True
    },
    {
        "id": 209,
        "name": "Unchalli Falls",
        "district": "Uttara Kannada",
        "height": "116 meters",
        "distance_from_bangalore": 480,
        "coordinates": {"lat": 14.8167, "lon": 74.7167},
        "best_time": "June to February",
        "highlights": ["Aghanashini River", "Lush green surroundings", "Pristine location"],
        "activities": ["Trekking", "Photography", "Swimming", "Picnic"],
        "entry_fee": 15,
        "facilities": ["Trekking Path", "Viewpoints", "Basic Facilities"],
        "photos": [get_destination_media("Unchalli Falls", "photo")],
        "videos": [get_destination_media("Unchalli Falls", "video")],
        "description": "Also known as Lushington Falls, formed by Aghanashini River in pristine Western Ghats.",
        "hidden_gem": True
    },
    {
        "id": 210,
        "name": "Sathodi Falls",
        "district": "Uttara Kannada",
        "height": "15 meters",
        "distance_from_bangalore": 520,
        "coordinates": {"lat": 15.0167, "lon": 74.5167},
        "best_time": "June to February",
        "highlights": ["Mini Niagara of India", "Kali River", "Multiple streams"],
        "activities": ["Photography", "Picnic", "Nature Walk", "Swimming"],
        "entry_fee": 10,
        "facilities": ["Parking", "Picnic Spots", "Basic Facilities"],
        "photos": [get_destination_media("Sathodi Falls", "photo")],
        "videos": [get_destination_media("Sathodi Falls", "video")],
        "description": "Known as Mini Niagara of India, multiple streams cascading over rocks on Kali River.",
        "hidden_gem": True
    }
]

# Heritage Sites Database
KARNATAKA_HERITAGE_SITES = [
    {
        "id": 301,
        "name": "Hampi Group of Monuments",
        "district": "Vijayanagara",
        "unesco_status": True,
        "period": "14th-16th Century",
        "dynasty": "Vijayanagara Empire",
        "distance_from_bangalore": 340,
        "coordinates": {"lat": 15.3350, "lon": 76.4600},
        "highlights": ["Virupaksha Temple", "Vittala Temple", "Stone Chariot", "Royal Enclosure"],
        "activities": ["Heritage Walk", "Photography", "Coracle Ride", "Sunset at Matanga Hill"],
        "entry_fee": 40,
        "best_time": "October to March",
        "facilities": ["Museum", "Guide Services", "Parking", "Cafeteria"],
        "photos": [get_destination_media("Hampi Vittala Temple", "photo")],
        "videos": [get_destination_media("Hampi Heritage", "video")],
        "description": "UNESCO World Heritage Site, ruins of the magnificent Vijayanagara Empire capital."
    },
    {
        "id": 302,
        "name": "Pattadakal Group of Monuments",
        "district": "Bagalkot",
        "unesco_status": True,
        "period": "7th-8th Century",
        "dynasty": "Chalukya Dynasty",
        "distance_from_bangalore": 450,
        "coordinates": {"lat": 15.9450, "lon": 75.8167},
        "highlights": ["Virupaksha Temple", "Mallikarjuna Temple", "Papanatha Temple", "Jain Temple"],
        "activities": ["Temple Tour", "Architecture Study", "Photography"],
        "entry_fee": 30,
        "best_time": "October to March",
        "facilities": ["Museum", "Guide Services", "Parking"],
        "photos": [get_destination_media("Pattadakal Temples", "photo")],
        "videos": [get_destination_media("Pattadakal Heritage", "video")],
        "description": "UNESCO site showcasing evolution of temple architecture from Dravidian to Nagara styles."
    },
    {
        "id": 303,
        "name": "Badami Cave Temples",
        "district": "Bagalkot",
        "unesco_status": False,
        "period": "6th-8th Century",
        "dynasty": "Chalukya Dynasty",
        "distance_from_bangalore": 470,
        "coordinates": {"lat": 15.9167, "lon": 75.6833},
        "highlights": ["Four Rock-cut Caves", "Agastya Lake", "Bhutanatha Temples", "Fort Ruins"],
        "activities": ["Cave Exploration", "Lake Boating", "Fort Trekking", "Photography"],
        "entry_fee": 25,
        "best_time": "October to March",
        "facilities": ["Parking", "Boat Services", "Cafeteria", "Guide Services"],
        "photos": [get_destination_media("Badami Caves", "photo")],
        "videos": [get_destination_media("Badami Caves", "video")],
        "description": "Ancient rock-cut cave temples showcasing early Chalukyan architecture and art."
    },
    # Hidden Heritage Gems
    {
        "id": 304,
        "name": "Aihole",
        "district": "Bagalkot",
        "unesco_status": False,
        "period": "5th-12th Century",
        "dynasty": "Chalukya Dynasty",
        "distance_from_bangalore": 460,
        "coordinates": {"lat": 15.9500, "lon": 75.8000},
        "highlights": ["Durga Temple", "Lad Khan Temple", "Ravalphadi Cave", "125+ Temples"],
        "activities": ["Temple Hopping", "Architecture Study", "Photography", "Village Walk"],
        "entry_fee": 15,
        "best_time": "October to March",
        "facilities": ["Parking", "Basic Facilities", "Local Guides"],
        "photos": [get_destination_media("Aihole Temples", "photo")],
        "videos": [get_destination_media("Aihole Heritage", "video")],
        "description": "Cradle of Indian temple architecture with 125+ temples spanning different periods.",
        "hidden_gem": True
    },
    {
        "id": 305,
        "name": "Halebidu",
        "district": "Hassan",
        "unesco_status": False,
        "period": "12th Century",
        "dynasty": "Hoysala Dynasty",
        "distance_from_bangalore": 220,
        "coordinates": {"lat": 13.2167, "lon": 75.9833},
        "highlights": ["Hoysaleswara Temple", "Kedareshwara Temple", "Intricate Sculptures"],
        "activities": ["Temple Tour", "Sculpture Study", "Photography"],
        "entry_fee": 25,
        "best_time": "October to March",
        "facilities": ["Museum", "Parking", "Guide Services"],
        "photos": [get_destination_media("Halebidu Temple", "photo")],
        "videos": [get_destination_media("Halebidu Heritage", "video")],
        "description": "Masterpiece of Hoysala architecture with incredibly detailed stone carvings.",
        "hidden_gem": True
    }
]

# Beach Destinations
KARNATAKA_BEACHES = [
    {
        "id": 401,
        "name": "Gokarna Beach",
        "district": "Uttara Kannada",
        "distance_from_bangalore": 485,
        "coordinates": {"lat": 14.5492, "lon": 74.3200},
        "beaches": ["Om Beach", "Kudle Beach", "Half Moon Beach", "Paradise Beach", "Gokarna Main Beach"],
        "activities": ["Beach Trekking", "Water Sports", "Temple Visit", "Sunset Viewing"],
        "best_time": "October to March",
        "facilities": ["Accommodation", "Restaurants", "Water Sports", "Temple"],
        "photos": [get_destination_media("Gokarna Om Beach", "photo")],
        "videos": [get_destination_media("Gokarna Beaches", "video")],
        "description": "Sacred town with pristine beaches, perfect blend of spirituality and natural beauty."
    },
    {
        "id": 402,
        "name": "Karwar Beach",
        "district": "Uttara Kannada",
        "distance_from_bangalore": 520,
        "coordinates": {"lat": 14.8167, "lon": 74.1333},
        "beaches": ["Karwar Beach", "Devbagh Beach", "Majali Beach"],
        "activities": ["Water Sports", "Island Hopping", "Dolphin Spotting", "Fishing"],
        "best_time": "October to March",
        "facilities": ["Naval Base", "Resorts", "Water Sports Center", "Boat Services"],
        "photos": [get_destination_media("Karwar Beach", "photo")],
        "videos": [get_destination_media("Karwar Beach", "video")],
        "description": "Pristine beaches with naval heritage and excellent water sports facilities."
    }
]