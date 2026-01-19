"""
Comprehensive Direction-wise Itineraries from Bangalore
Hidden Gems and Lesser-Known Destinations within 100km
"""

from services.photo_service import get_curated_photos, get_destination_video

# Direction-wise Hidden Gems from Bangalore
BANGALORE_DIRECTION_ITINERARIES = {
    
    # INSIDE BANGALORE - Hidden Gems within City Limits
    "inside_bangalore": {
        "title": "Hidden Gems Inside Bangalore",
        "subtitle": "Discover the secret spots within the city that locals love",
        "duration": "1 Day",
        "total_distance": "50-80 km",
        "destinations": [
            {
                "name": "Turahalli Forest",
                "distance_km": 15,
                "coordinates": {"lat": 12.8500, "lon": 77.4833},
                "category": "Nature Reserve",
                "time_needed": "2-3 hours",
                "highlights": ["Rock climbing", "Mountain biking", "Bird watching", "Sunset views"],
                "description": "A hidden forest reserve perfect for adventure activities and nature photography. Popular among rock climbers and mountain bikers.",
                "entry_fee": 0,
                "best_time": "Early morning or evening",
                "photos": get_curated_photos("Turahalli Forest Bangalore"),
                "hidden_gem": True
            },
            {
                "name": "Dodda Alada Mara (Big Banyan Tree)",
                "distance_km": 28,
                "coordinates": {"lat": 12.8167, "lon": 77.3833},
                "category": "Natural Wonder",
                "time_needed": "1-2 hours",
                "highlights": ["400-year-old banyan tree", "3-acre canopy", "Photography", "Peaceful environment"],
                "description": "A single 400-year-old banyan tree spreading over 3 acres, creating a natural canopy. Perfect for meditation and photography.",
                "entry_fee": 10,
                "best_time": "Morning or evening",
                "photos": get_curated_photos("Big Banyan Tree Bangalore"),
                "hidden_gem": True
            },
            {
                "name": "Hesaraghatta Lake & Nrityagram",
                "distance_km": 30,
                "coordinates": {"lat": 13.1167, "lon": 77.4500},
                "category": "Cultural & Nature",
                "time_needed": "2-3 hours",
                "highlights": ["Dance village", "Serene lake", "Cultural performances", "Bird watching"],
                "description": "A cultural village dedicated to Indian classical dance, set beside a peaceful lake. Often hosts dance performances and workshops.",
                "entry_fee": 50,
                "best_time": "Morning or during cultural events",
                "photos": get_curated_photos("Nrityagram Hesaraghatta"),
                "hidden_gem": True
            },
            {
                "name": "Avalabetta Hilltop",
                "distance_km": 90,
                "coordinates": {"lat": 13.4000, "lon": 77.7500},
                "category": "Hill Station",
                "time_needed": "3-4 hours",
                "highlights": ["Panoramic views", "Rock climbing", "Sunrise/sunset", "Bird watching"],
                "description": "A lesser-known hilltop offering 360-degree views of the surrounding landscape. Perfect for rock climbing and photography.",
                "entry_fee": 20,
                "best_time": "Early morning for sunrise",
                "photos": get_curated_photos("Avalabetta Hill Bangalore"),
                "hidden_gem": True
            }
        ]
    },
    
    # TOWARDS HOSUR DIRECTION
    "towards_hosur": {
        "title": "Hidden Gems Towards Hosur",
        "subtitle": "Explore the Tamil Nadu border region's secret treasures",
        "duration": "1 Day",
        "total_distance": "120-150 km",
        "destinations": [
            {
                "name": "Kelavarapalli Dam & Reservoir",
                "distance_km": 45,
                "coordinates": {"lat": 12.7167, "lon": 77.8333},
                "category": "Water Body",
                "time_needed": "2-3 hours",
                "highlights": ["Scenic reservoir", "Boating", "Fishing", "Picnic spot"],
                "description": "A beautiful reservoir project near Hosur, perfect for water activities and peaceful picnics. Less crowded than other water bodies.",
                "entry_fee": 25,
                "best_time": "Morning or evening",
                "photos": get_curated_photos("Kelavarapalli Dam Hosur"),
                "hidden_gem": True
            },
            {
                "name": "Chandrachoodeshwara Temple",
                "distance_km": 40,
                "coordinates": {"lat": 12.7333, "lon": 77.8167},
                "category": "Spiritual",
                "time_needed": "1-2 hours",
                "highlights": ["Ancient temple", "Unique architecture", "Peaceful environment", "Local culture"],
                "description": "An ancient temple with unique Dravidian architecture, known for its peaceful ambiance and spiritual significance.",
                "entry_fee": 0,
                "best_time": "Early morning or evening",
                "photos": get_curated_photos("Chandrachoodeshwara Temple Hosur"),
                "hidden_gem": True
            },
            {
                "name": "Jalamangala Narasimha Temple",
                "distance_km": 55,
                "coordinates": {"lat": 12.6833, "lon": 77.8500},
                "category": "Heritage",
                "time_needed": "1-2 hours",
                "highlights": ["Hoysala architecture", "Ancient sculptures", "Historical significance", "Peaceful setting"],
                "description": "A hidden Hoysala-era temple with exquisite stone carvings and sculptures, showcasing ancient Karnataka's architectural brilliance.",
                "entry_fee": 10,
                "best_time": "Morning",
                "photos": get_curated_photos("Jalamangala Temple Karnataka"),
                "hidden_gem": True
            }
        ]
    },
    
    # TOWARDS KOLAR DIRECTION
    "towards_kolar": {
        "title": "Golden Route to Kolar",
        "subtitle": "Discover the land of gold mines and ancient temples",
        "duration": "1 Day",
        "total_distance": "140-180 km",
        "destinations": [
            {
                "name": "Antaragange Cave Complex",
                "distance_km": 70,
                "coordinates": {"lat": 13.7167, "lon": 78.1167},
                "category": "Adventure",
                "time_needed": "4-5 hours",
                "highlights": ["Natural caves", "Rock formations", "Perennial spring", "Night trekking"],
                "description": "Volcanic rock formation with natural caves and a sacred perennial spring. Famous for cave exploration and night treks through rocky terrain.",
                "entry_fee": 20,
                "best_time": "Early morning or for night trek",
                "photos": get_curated_photos("Antaragange Caves Kolar"),
                "hidden_gem": True
            },
            {
                "name": "Kotilingeshwara Temple",
                "distance_km": 75,
                "coordinates": {"lat": 13.7500, "lon": 78.1333},
                "category": "Spiritual",
                "time_needed": "2-3 hours",
                "highlights": ["Millions of Shiva lingas", "World record holder", "Spiritual significance", "Unique architecture"],
                "description": "Home to over 10 million Shiva lingas, this temple holds a world record. The sight of countless lingas is truly mesmerizing and spiritually uplifting.",
                "entry_fee": 0,
                "best_time": "Early morning or evening",
                "photos": get_curated_photos("Kotilingeshwara Temple Kolar"),
                "hidden_gem": False
            },
            {
                "name": "Kolar Gold Fields (KGF)",
                "distance_km": 80,
                "coordinates": {"lat": 12.9500, "lon": 78.2167},
                "category": "Heritage",
                "time_needed": "3-4 hours",
                "highlights": ["Historic gold mines", "Colonial architecture", "Mining heritage", "KGF movie locations"],
                "description": "Historic gold mining area with colonial-era buildings and mining heritage. Made famous by the KGF movie series, showcasing India's mining history.",
                "entry_fee": 50,
                "best_time": "Morning",
                "photos": get_curated_photos("Kolar Gold Fields KGF"),
                "hidden_gem": False
            },
            {
                "name": "Someshwara Temple, Kolar",
                "distance_km": 72,
                "coordinates": {"lat": 13.1333, "lon": 78.1333},
                "category": "Heritage",
                "time_needed": "1-2 hours",
                "highlights": ["Chola architecture", "Ancient sculptures", "Historical significance", "Peaceful environment"],
                "description": "An ancient temple showcasing Chola architectural style with intricate stone carvings. A hidden gem for history and architecture enthusiasts.",
                "entry_fee": 10,
                "best_time": "Morning or evening",
                "photos": get_curated_photos("Someshwara Temple Kolar"),
                "hidden_gem": True
            }
        ]
    },
    
    # TOWARDS KANAKAPURA DIRECTION
    "towards_kanakapura": {
        "title": "Kanakapura's Natural Wonders",
        "subtitle": "Waterfalls, hills, and river confluences",
        "duration": "1 Day",
        "total_distance": "160-200 km",
        "destinations": [
            {
                "name": "Chunchi Falls",
                "distance_km": 83,
                "coordinates": {"lat": 12.4333, "lon": 77.2833},
                "category": "Waterfall",
                "time_needed": "3-4 hours",
                "highlights": ["Cascading waterfall", "Natural pool", "Trekking", "Photography"],
                "description": "A beautiful waterfall cascading from 50 feet height, surrounded by lush greenery. Perfect for swimming in natural pools and photography.",
                "entry_fee": 30,
                "best_time": "Post-monsoon (Oct-Feb)",
                "photos": get_curated_photos("Chunchi Falls Kanakapura"),
                "hidden_gem": True
            },
            {
                "name": "Bilikal Rangaswamy Betta",
                "distance_km": 70,
                "coordinates": {"lat": 12.5167, "lon": 77.2500},
                "category": "Hill Station",
                "time_needed": "4-5 hours",
                "highlights": ["Temple under rock", "Panoramic views", "Trekking", "Sunrise/sunset"],
                "description": "A unique hilltop temple built under a massive granite rock at 3,780 feet. Offers stunning panoramic views and spiritual experience.",
                "entry_fee": 20,
                "best_time": "Early morning for sunrise",
                "photos": get_curated_photos("Bilikal Rangaswamy Betta"),
                "hidden_gem": True
            },
            {
                "name": "Mekedatu (Goat's Leap)",
                "distance_km": 98,
                "coordinates": {"lat": 12.3833, "lon": 77.3167},
                "category": "Natural Wonder",
                "time_needed": "3-4 hours",
                "highlights": ["River gorge", "Cauvery river", "Coracle rides", "Geological wonder"],
                "description": "A narrow gorge where River Cauvery flows through rocks, creating a spectacular natural formation. The name means 'Goat's Leap' in Kannada.",
                "entry_fee": 25,
                "best_time": "Post-monsoon",
                "photos": get_curated_photos("Mekedatu Kanakapura"),
                "hidden_gem": False
            },
            {
                "name": "Sangama",
                "distance_km": 95,
                "coordinates": {"lat": 12.3667, "lon": 77.3000},
                "category": "River Confluence",
                "time_needed": "2-3 hours",
                "highlights": ["River confluence", "Coracle rides", "Fishing", "Peaceful environment"],
                "description": "Confluence of rivers Arkavathi and Cauvery, creating a serene and spiritually significant spot. Popular for coracle rides and fishing.",
                "entry_fee": 15,
                "best_time": "Morning or evening",
                "photos": get_curated_photos("Sangama Kanakapura"),
                "hidden_gem": True
            }
        ]
    },
    
    # TOWARDS MYSORE DIRECTION
    "towards_mysore": {
        "title": "Mysore Road Hidden Treasures",
        "subtitle": "Ancient temples and natural wonders en route to Mysore",
        "duration": "1 Day",
        "total_distance": "120-160 km",
        "destinations": [
            {
                "name": "Muthyala Maduvu (Pearl Valley)",
                "distance_km": 40,
                "coordinates": {"lat": 12.7833, "lon": 77.3167},
                "category": "Waterfall",
                "time_needed": "3-4 hours",
                "highlights": ["92-meter waterfall", "Natural pools", "Trekking", "Photography"],
                "description": "Known as Pearl Valley, this 92-meter waterfall creates a misty spray that looks like falling pearls. Surrounded by rocky terrain and lush vegetation.",
                "entry_fee": 25,
                "best_time": "Post-monsoon",
                "photos": get_curated_photos("Muthyala Maduvu Pearl Valley"),
                "hidden_gem": True
            },
            {
                "name": "Kanva Reservoir",
                "distance_km": 69,
                "coordinates": {"lat": 12.6167, "lon": 77.2833},
                "category": "Water Body",
                "time_needed": "2-3 hours",
                "highlights": ["Artificial lake", "Boating", "Bird watching", "Sunset views"],
                "description": "A serene artificial lake surrounded by hills, perfect for boating and bird watching. Less crowded alternative to other water bodies near Bangalore.",
                "entry_fee": 20,
                "best_time": "Evening for sunset",
                "photos": get_curated_photos("Kanva Reservoir Bangalore"),
                "hidden_gem": True
            },
            {
                "name": "Ramadevara Betta",
                "distance_km": 85,
                "coordinates": {"lat": 12.5833, "lon": 77.1833},
                "category": "Hill Station",
                "time_needed": "3-4 hours",
                "highlights": ["Vulture sanctuary", "Rock climbing", "Panoramic views", "Wildlife"],
                "description": "A rocky hill known for its vulture sanctuary and rock climbing opportunities. Offers excellent views of the surrounding landscape.",
                "entry_fee": 15,
                "best_time": "Early morning",
                "photos": get_curated_photos("Ramadevara Betta Bangalore"),
                "hidden_gem": True
            }
        ]
    },
    
    # TOWARDS MAGADI DIRECTION
    "towards_magadi": {
        "title": "Magadi's Rugged Beauty",
        "subtitle": "Rocky landscapes and ancient forts",
        "duration": "1 Day",
        "total_distance": "100-140 km",
        "destinations": [
            {
                "name": "Savandurga",
                "distance_km": 50,
                "coordinates": {"lat": 12.9167, "lon": 77.2833},
                "category": "Adventure",
                "time_needed": "4-5 hours",
                "highlights": ["Asia's largest monolith", "Rock climbing", "Trekking", "Arkavathi river"],
                "description": "One of Asia's largest monolithic rocks, perfect for rock climbing and trekking. The twin hills of Karigudda and Billigudda offer challenging climbs.",
                "entry_fee": 25,
                "best_time": "Early morning",
                "photos": get_curated_photos("Savandurga Monolith"),
                "hidden_gem": False
            },
            {
                "name": "Manchanabele Dam",
                "distance_km": 40,
                "coordinates": {"lat": 12.8833, "lon": 77.3000},
                "category": "Adventure Sports",
                "time_needed": "3-4 hours",
                "highlights": ["Kayaking", "Rappelling", "Camping", "Water sports"],
                "description": "A popular spot for adventure sports like kayaking and rappelling. The dam creates a beautiful reservoir surrounded by rocky hills.",
                "entry_fee": 50,
                "best_time": "Morning",
                "photos": get_curated_photos("Manchanabele Dam Adventure"),
                "hidden_gem": True
            },
            {
                "name": "Magadi Fort",
                "distance_km": 52,
                "coordinates": {"lat": 12.9500, "lon": 77.2167},
                "category": "Heritage",
                "time_needed": "2-3 hours",
                "highlights": ["Ancient fort", "Historical significance", "Architecture", "Panoramic views"],
                "description": "An ancient fort with historical significance, offering insights into the region's past. The climb to the top provides excellent views.",
                "entry_fee": 20,
                "best_time": "Morning or evening",
                "photos": get_curated_photos("Magadi Fort Karnataka"),
                "hidden_gem": True
            }
        ]
    },
    
    # TOWARDS TUMKUR DIRECTION
    "towards_tumkur": {
        "title": "Tumkur's Spiritual Heights",
        "subtitle": "Ancient temples and hill stations",
        "duration": "1 Day",
        "total_distance": "120-150 km",
        "destinations": [
            {
                "name": "Devarayanadurga",
                "distance_km": 65,
                "coordinates": {"lat": 13.3667, "lon": 77.2833},
                "category": "Hill Station",
                "time_needed": "4-5 hours",
                "highlights": ["Yoga Narasimha temple", "Bhoga Narasimha temple", "Namada Chilume spring", "Panoramic views"],
                "description": "A hill station at 3,940 feet with ancient temples and a sacred natural spring. Perfect blend of spirituality and natural beauty.",
                "entry_fee": 15,
                "best_time": "Early morning",
                "photos": get_curated_photos("Devarayanadurga Hill Station"),
                "hidden_gem": False
            },
            {
                "name": "Madhugiri Fort",
                "distance_km": 100,
                "coordinates": {"lat": 13.6667, "lon": 77.2000},
                "category": "Heritage",
                "time_needed": "4-5 hours",
                "highlights": ["Second largest monolith in Asia", "17th-century fort", "Steep climb", "Historical significance"],
                "description": "Built on Asia's second-largest monolith, this 17th-century fort offers a challenging climb and rich history. The steep ascent is rewarding.",
                "entry_fee": 30,
                "best_time": "Early morning",
                "photos": get_curated_photos("Madhugiri Fort Monolith"),
                "hidden_gem": False
            },
            {
                "name": "Siddara Betta",
                "distance_km": 100,
                "coordinates": {"lat": 13.4167, "lon": 77.1833},
                "category": "Spiritual",
                "time_needed": "3-4 hours",
                "highlights": ["Hill of Saints", "Cave temples", "Spiritual significance", "Trekking"],
                "description": "Known as the 'Hill of Saints', this sacred hill features cave temples and offers a spiritual trekking experience with panoramic views.",
                "entry_fee": 20,
                "best_time": "Early morning",
                "photos": get_curated_photos("Siddara Betta Tumkur"),
                "hidden_gem": True
            },
            {
                "name": "Goravanahalli Mahalakshmi Temple",
                "distance_km": 70,
                "coordinates": {"lat": 13.3833, "lon": 77.2667},
                "category": "Spiritual",
                "time_needed": "1-2 hours",
                "highlights": ["Ancient temple", "Goddess Mahalakshmi", "Peaceful environment", "Local culture"],
                "description": "An ancient temple dedicated to Goddess Mahalakshmi, known for its peaceful ambiance and spiritual significance among locals.",
                "entry_fee": 0,
                "best_time": "Morning or evening",
                "photos": get_curated_photos("Goravanahalli Temple"),
                "hidden_gem": True
            }
        ]
    },
    
    # TOWARDS DODDABALLAPUR DIRECTION
    "towards_doddaballapur": {
        "title": "Doddaballapur's Natural Escapes",
        "subtitle": "Hills, lakes, and adventure spots",
        "duration": "1 Day",
        "total_distance": "80-120 km",
        "destinations": [
            {
                "name": "Nandi Hills",
                "distance_km": 60,
                "coordinates": {"lat": 13.3703, "lon": 77.6838},
                "category": "Hill Station",
                "time_needed": "4-5 hours",
                "highlights": ["Sunrise point", "Tipu's Drop", "Bhoga Nandeeshwara temple", "Paragliding"],
                "description": "Famous hill station known for spectacular sunrise views and historical significance. Popular for paragliding and photography.",
                "entry_fee": 30,
                "best_time": "Early morning for sunrise",
                "photos": get_curated_photos("Nandi Hills Sunrise"),
                "hidden_gem": False
            },
            {
                "name": "Ghati Subramanya Temple",
                "distance_km": 55,
                "coordinates": {"lat": 13.4167, "lon": 77.6167},
                "category": "Spiritual",
                "time_needed": "2-3 hours",
                "highlights": ["Unique temple", "Sarpa Dosha remedy", "Spiritual significance", "Peaceful environment"],
                "description": "A unique temple known for remedies related to Sarpa Dosha (serpent curse). The temple has a peaceful setting amidst hills.",
                "entry_fee": 0,
                "best_time": "Morning",
                "photos": get_curated_photos("Ghati Subramanya Temple"),
                "hidden_gem": True
            },
            {
                "name": "Jakkur Aerodrome & Lake",
                "distance_km": 25,
                "coordinates": {"lat": 13.0833, "lon": 77.6000},
                "category": "Adventure",
                "time_needed": "2-3 hours",
                "highlights": ["Flying club", "Lake views", "Aviation experience", "Bird watching"],
                "description": "A small aerodrome with flying club facilities and a beautiful lake. Perfect for aviation enthusiasts and peaceful lake views.",
                "entry_fee": 100,
                "best_time": "Morning or evening",
                "photos": get_curated_photos("Jakkur Aerodrome Lake"),
                "hidden_gem": True
            }
        ]
    },
    
    # TOWARDS DEVANAHALLI DIRECTION
    "towards_devanahalli": {
        "title": "Devanahalli's Heritage Trail",
        "subtitle": "Birthplace of Tipu Sultan and ancient temples",
        "duration": "1 Day",
        "total_distance": "80-100 km",
        "destinations": [
            {
                "name": "Devanahalli Fort",
                "distance_km": 40,
                "coordinates": {"lat": 13.2500, "lon": 77.7167},
                "category": "Heritage",
                "time_needed": "2-3 hours",
                "highlights": ["Tipu Sultan's birthplace", "18th-century fort", "Historical significance", "Architecture"],
                "description": "Historic fort and birthplace of Tipu Sultan, showcasing 18th-century military architecture and rich history of Mysore kingdom.",
                "entry_fee": 25,
                "best_time": "Morning or evening",
                "photos": get_curated_photos("Devanahalli Fort Tipu Sultan"),
                "hidden_gem": False
            },
            {
                "name": "Venugopala Swamy Temple",
                "distance_km": 42,
                "coordinates": {"lat": 13.2667, "lon": 77.7333},
                "category": "Heritage",
                "time_needed": "1-2 hours",
                "highlights": ["Vijayanagara architecture", "Ancient sculptures", "Peaceful environment", "Historical significance"],
                "description": "An ancient temple showcasing Vijayanagara architectural style with beautiful stone carvings and peaceful surroundings.",
                "entry_fee": 10,
                "best_time": "Morning",
                "photos": get_curated_photos("Venugopala Swamy Temple Devanahalli"),
                "hidden_gem": True
            },
            {
                "name": "Nallur Tamarind Grove",
                "distance_km": 45,
                "coordinates": {"lat": 13.2833, "lon": 77.7500},
                "category": "Natural Heritage",
                "time_needed": "1-2 hours",
                "highlights": ["300 ancient tamarind trees", "Chola dynasty heritage", "Biodiversity hotspot", "Photography"],
                "description": "A grove of 300 ancient tamarind trees believed to be from the Chola dynasty period. Now a biodiversity heritage site.",
                "entry_fee": 15,
                "best_time": "Morning or evening",
                "photos": get_curated_photos("Nallur Tamarind Grove"),
                "hidden_gem": True
            }
        ]
    }
}

# Sample itinerary combinations
SAMPLE_ITINERARIES = {
    "adventure_lover": {
        "title": "Adventure Seeker's Paradise",
        "destinations": ["Antaragange Cave Complex", "Savandurga", "Manchanabele Dam", "Turahalli Forest"],
        "duration": "2 Days",
        "activities": ["Cave exploration", "Rock climbing", "Kayaking", "Mountain biking"]
    },
    
    "spiritual_journey": {
        "title": "Spiritual Circuit Around Bangalore",
        "destinations": ["Kotilingeshwara Temple", "Devarayanadurga", "Ghati Subramanya Temple", "Bilikal Rangaswamy Betta"],
        "duration": "2 Days",
        "activities": ["Temple visits", "Meditation", "Spiritual trekking", "Sacred spring visit"]
    },
    
    "nature_photographer": {
        "title": "Nature Photography Trail",
        "destinations": ["Chunchi Falls", "Muthyala Maduvu", "Nandi Hills", "Hesaraghatta Lake"],
        "duration": "2 Days",
        "activities": ["Waterfall photography", "Sunrise/sunset shots", "Bird photography", "Landscape shots"]
    },
    
    "heritage_explorer": {
        "title": "Heritage and History Trail",
        "destinations": ["Kolar Gold Fields", "Devanahalli Fort", "Madhugiri Fort", "Jalamangala Temple"],
        "duration": "2 Days",
        "activities": ["Historical exploration", "Architecture study", "Cultural immersion", "Photography"]
    }
}