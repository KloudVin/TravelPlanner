"""
Comprehensive Karnataka Hidden Gems Database
Lesser-known destinations across all districts of Karnataka
"""

from services.photo_service import get_curated_photos, get_destination_video

# Karnataka Hidden Gems by Region
KARNATAKA_HIDDEN_GEMS = {
    
    # NORTH KARNATAKA HIDDEN GEMS
    "north_karnataka": {
        "region_name": "North Karnataka Hidden Treasures",
        "description": "Discover the unexplored heritage and natural wonders of North Karnataka",
        "destinations": [
            {
                "name": "Yana Rocks",
                "district": "Uttara Kannada",
                "distance_from_bangalore": 520,
                "coordinates": {"lat": 14.5500, "lon": 74.6167},
                "category": "Natural Wonder",
                "highlights": ["Unique limestone formations", "Bhairaveshwara Shikhara", "Mohini Shikhara", "Cave temple"],
                "description": "Two massive limestone rock formations rising 90m high, accessible through dense forest trek. The rocks have unique karst topography and ancient cave temples.",
                "activities": ["Rock climbing", "Cave exploration", "Forest trekking", "Photography"],
                "best_time": "October to March",
                "entry_fee": 30,
                "photos": get_curated_photos("Yana Rocks Karnataka"),
                "hidden_gem": True
            },
            {
                "name": "Sathodi Falls",
                "district": "Uttara Kannada",
                "distance_from_bangalore": 520,
                "coordinates": {"lat": 15.0167, "lon": 74.5167},
                "category": "Waterfall",
                "highlights": ["Mini Niagara of India", "Multiple streams", "Kali River", "Pristine location"],
                "description": "Known as Mini Niagara of India, multiple streams cascade over rocks creating a spectacular waterfall on Kali River.",
                "activities": ["Photography", "Swimming", "Picnic", "Nature walk"],
                "best_time": "June to February",
                "entry_fee": 10,
                "photos": get_curated_photos("Sathodi Falls Uttara Kannada"),
                "hidden_gem": True
            },
            {
                "name": "Magod Falls",
                "district": "Uttara Kannada",
                "distance_from_bangalore": 500,
                "coordinates": {"lat": 14.9167, "lon": 74.6167},
                "category": "Waterfall",
                "highlights": ["Two-stage waterfall", "Bedthi River", "200m height", "Western Ghats"],
                "description": "A spectacular two-stage waterfall on Bedthi River, relatively unexplored gem in Western Ghats with pristine surroundings.",
                "activities": ["Trekking", "Photography", "Nature study"],
                "best_time": "June to February",
                "entry_fee": 20,
                "photos": get_curated_photos("Magod Falls Karnataka"),
                "hidden_gem": True
            },
            {
                "name": "Unchalli Falls (Lushington Falls)",
                "district": "Uttara Kannada",
                "distance_from_bangalore": 480,
                "coordinates": {"lat": 14.8167, "lon": 74.7167},
                "category": "Waterfall",
                "highlights": ["116m height", "Aghanashini River", "Pristine location", "Trekking trail"],
                "description": "Also known as Lushington Falls, formed by Aghanashini River plunging 116 meters through pristine Western Ghats forest.",
                "activities": ["Trekking", "Photography", "Swimming", "Bird watching"],
                "best_time": "June to February",
                "entry_fee": 15,
                "photos": get_curated_photos("Unchalli Falls Karnataka"),
                "hidden_gem": True
            },
            {
                "name": "Vibhooti Falls",
                "district": "Uttara Kannada",
                "distance_from_bangalore": 530,
                "coordinates": {"lat": 14.7500, "lon": 74.5833},
                "category": "Waterfall",
                "highlights": ["Hidden waterfall", "Dense forest", "Pristine nature", "Less crowded"],
                "description": "A hidden waterfall deep in Western Ghats forest, accessible only through trekking. Perfect for those seeking untouched nature.",
                "activities": ["Forest trekking", "Photography", "Nature study", "Bird watching"],
                "best_time": "June to January",
                "entry_fee": 25,
                "photos": get_curated_photos("Vibhooti Falls Uttara Kannada"),
                "hidden_gem": True
            }
        ]
    },
    
    # CENTRAL KARNATAKA HIDDEN GEMS
    "central_karnataka": {
        "region_name": "Central Karnataka Secrets",
        "description": "Hidden treasures in the heart of Karnataka",
        "destinations": [
            {
                "name": "Agumbe Rainforest",
                "district": "Shivamogga",
                "distance_from_bangalore": 350,
                "coordinates": {"lat": 13.5167, "lon": 75.1000},
                "category": "Rainforest",
                "highlights": ["Cherrapunji of South India", "Sunset point", "King Cobra research", "Rainforest trek"],
                "description": "Known as Cherrapunji of South India, receives highest rainfall in Karnataka. Famous for sunset views and rainforest biodiversity.",
                "activities": ["Rainforest trekking", "Sunset viewing", "Wildlife spotting", "Photography"],
                "best_time": "October to March",
                "entry_fee": 25,
                "photos": get_curated_photos("Agumbe Rainforest Karnataka"),
                "hidden_gem": True
            },
            {
                "name": "Barkana Falls",
                "district": "Shivamogga",
                "distance_from_bangalore": 380,
                "coordinates": {"lat": 13.5000, "lon": 75.1167},
                "category": "Waterfall",
                "highlights": ["10th highest waterfall in India", "259m height", "Sita River", "Dense forest trek"],
                "description": "India's 10th highest waterfall at 259 meters, hidden in Agumbe rainforest. Requires forest trek through dense vegetation.",
                "activities": ["Forest trekking", "Photography", "Bird watching", "Nature study"],
                "best_time": "June to February",
                "entry_fee": 30,
                "photos": get_curated_photos("Barkana Falls Agumbe"),
                "hidden_gem": True
            },
            {
                "name": "Onake Abbi Falls",
                "district": "Shivamogga",
                "distance_from_bangalore": 370,
                "coordinates": {"lat": 13.5167, "lon": 75.1000},
                "category": "Waterfall",
                "highlights": ["Pestle-shaped rock", "116m height", "Agumbe rainforest", "Pristine nature"],
                "description": "Named after pestle-shaped rock formation, this 116m waterfall is hidden gem in Agumbe rainforest with pristine surroundings.",
                "activities": ["Trekking", "Photography", "Rock formation study"],
                "best_time": "June to February",
                "entry_fee": 25,
                "photos": get_curated_photos("Onake Abbi Falls"),
                "hidden_gem": True
            },
            {
                "name": "Dabbe Falls",
                "district": "Shivamogga",
                "distance_from_bangalore": 390,
                "coordinates": {"lat": 13.8833, "lon": 75.0167},
                "category": "Waterfall",
                "highlights": ["Hidden waterfall", "Forest trek", "Natural pool", "Less crowded"],
                "description": "A hidden waterfall near Hosagadde, accessible through forest trek. Features natural pools perfect for swimming.",
                "activities": ["Forest trekking", "Swimming", "Photography", "Picnic"],
                "best_time": "June to January",
                "entry_fee": 20,
                "photos": get_curated_photos("Dabbe Falls Shivamogga"),
                "hidden_gem": True
            },
            {
                "name": "Kodachadri Peak",
                "district": "Shivamogga",
                "distance_from_bangalore": 380,
                "coordinates": {"lat": 13.9167, "lon": 75.1167},
                "category": "Trekking",
                "highlights": ["Western Ghats peak", "Mookambika temple", "Sunset views", "Biodiversity"],
                "description": "A peak in Western Ghats with ancient Mookambika temple on top. Offers spectacular sunset views and rich biodiversity.",
                "activities": ["Trekking", "Temple visit", "Sunset viewing", "Wildlife spotting"],
                "best_time": "October to March",
                "entry_fee": 50,
                "photos": get_curated_photos("Kodachadri Peak Karnataka"),
                "hidden_gem": False
            }
        ]
    },
    
    # SOUTH KARNATAKA HIDDEN GEMS
    "south_karnataka": {
        "region_name": "South Karnataka Mysteries",
        "description": "Unexplored gems in South Karnataka's diverse landscape",
        "destinations": [
            {
                "name": "Netravati Peak",
                "district": "Dakshina Kannada",
                "distance_from_bangalore": 330,
                "coordinates": {"lat": 13.1500, "lon": 75.0500},
                "category": "Trekking",
                "highlights": ["Offbeat trek", "Kudremukh National Park", "Raw wilderness", "Western Ghats views"],
                "description": "Hidden deep within Kudremukh National Park, this offbeat trail offers unspoiled Western Ghats views and raw wilderness experience.",
                "activities": ["Wilderness trekking", "Bird watching", "Photography", "Camping"],
                "best_time": "October to February",
                "entry_fee": 100,
                "photos": get_curated_photos("Netravati Peak Kudremukh"),
                "hidden_gem": True
            },
            {
                "name": "Pandavar Gudda",
                "district": "Chikmagalur",
                "distance_from_bangalore": 280,
                "coordinates": {"lat": 13.2833, "lon": 75.6167},
                "category": "Trekking",
                "highlights": ["Pandava connection", "Sunrise views", "Coffee plantations", "Less crowded"],
                "description": "A lesser-known peak associated with Pandavas from Mahabharata. Offers excellent sunrise views through coffee plantations.",
                "activities": ["Trekking", "Sunrise viewing", "Plantation walk", "Photography"],
                "best_time": "October to March",
                "entry_fee": 30,
                "photos": get_curated_photos("Pandavar Gudda Chikmagalur"),
                "hidden_gem": True
            },
            {
                "name": "Ettina Bhuja",
                "district": "Chikmagalur",
                "distance_from_bangalore": 300,
                "coordinates": {"lat": 13.3500, "lon": 75.5833},
                "category": "Trekking",
                "highlights": ["Ox shoulder shape", "Challenging trek", "Panoramic views", "Wildlife"],
                "description": "Named for its ox shoulder shape, this challenging trek offers panoramic views of Western Ghats and rich wildlife.",
                "activities": ["Challenging trekking", "Wildlife spotting", "Photography", "Adventure"],
                "best_time": "October to February",
                "entry_fee": 40,
                "photos": get_curated_photos("Ettina Bhuja Trek"),
                "hidden_gem": True
            },
            {
                "name": "Kemmangundi Secret Valleys",
                "district": "Chikmagalur",
                "distance_from_bangalore": 290,
                "coordinates": {"lat": 13.5500, "lon": 75.7667},
                "category": "Hill Station",
                "highlights": ["Hidden valleys", "Rose garden", "Rock garden", "Z point"],
                "description": "Hidden valleys around Kemmangundi with secret viewpoints, rose gardens, and rock formations away from main tourist areas.",
                "activities": ["Valley exploration", "Garden walks", "Photography", "Nature study"],
                "best_time": "September to March",
                "entry_fee": 35,
                "photos": get_curated_photos("Kemmangundi Hidden Valleys"),
                "hidden_gem": True
            }
        ]
    },
    
    # COASTAL KARNATAKA HIDDEN GEMS
    "coastal_karnataka": {
        "region_name": "Coastal Karnataka Secrets",
        "description": "Hidden beaches and coastal wonders",
        "destinations": [
            {
                "name": "Hoode Beach",
                "district": "Udupi",
                "distance_from_bangalore": 420,
                "coordinates": {"lat": 13.0833, "lon": 74.7167},
                "category": "Beach",
                "highlights": ["Pristine beach", "Less crowded", "Fishing village", "Sunset views"],
                "description": "A pristine, less crowded beach near Udupi with traditional fishing village atmosphere and spectacular sunset views.",
                "activities": ["Beach walks", "Fishing", "Sunset viewing", "Photography"],
                "best_time": "October to March",
                "entry_fee": 0,
                "photos": get_curated_photos("Hoode Beach Udupi"),
                "hidden_gem": True
            },
            {
                "name": "Kodi Beach",
                "district": "Udupi",
                "distance_from_bangalore": 430,
                "coordinates": {"lat": 13.2167, "lon": 74.7333},
                "category": "Beach",
                "highlights": ["Secluded beach", "Lighthouse", "Rocky coastline", "Peaceful environment"],
                "description": "A secluded beach with lighthouse and rocky coastline, perfect for peaceful moments away from crowded tourist beaches.",
                "activities": ["Beach exploration", "Lighthouse visit", "Rock climbing", "Solitude"],
                "best_time": "October to March",
                "entry_fee": 10,
                "photos": get_curated_photos("Kodi Beach Lighthouse"),
                "hidden_gem": True
            },
            {
                "name": "Byndoor Beach",
                "district": "Udupi",
                "distance_from_bangalore": 380,
                "coordinates": {"lat": 13.8667, "lon": 74.6333},
                "category": "Beach",
                "highlights": ["Untouched beach", "Someshwara temple", "Natural beauty", "Less commercialized"],
                "description": "An untouched beach with ancient Someshwara temple nearby. Less commercialized and perfect for nature lovers.",
                "activities": ["Beach walks", "Temple visit", "Photography", "Peaceful retreat"],
                "best_time": "October to March",
                "entry_fee": 0,
                "photos": get_curated_photos("Byndoor Beach Karnataka"),
                "hidden_gem": True
            },
            {
                "name": "Trasi Beach",
                "district": "Udupi",
                "distance_from_bangalore": 390,
                "coordinates": {"lat": 13.7167, "lon": 74.6833},
                "category": "Beach",
                "highlights": ["Golden sand", "Coconut groves", "Peaceful atmosphere", "Local culture"],
                "description": "A beautiful beach with golden sand and coconut groves, offering peaceful atmosphere and authentic local coastal culture.",
                "activities": ["Beach relaxation", "Cultural interaction", "Photography", "Coconut climbing"],
                "best_time": "October to March",
                "entry_fee": 0,
                "photos": get_curated_photos("Trasi Beach Udupi"),
                "hidden_gem": True
            }
        ]
    },
    
    # EASTERN KARNATAKA HIDDEN GEMS
    "eastern_karnataka": {
        "region_name": "Eastern Karnataka Treasures",
        "description": "Hidden gems in the eastern districts",
        "destinations": [
            {
                "name": "Kailasagiri Hill & Cave Temple",
                "district": "Chikkaballapur",
                "distance_from_bangalore": 80,
                "coordinates": {"lat": 13.4000, "lon": 78.0500},
                "category": "Spiritual",
                "highlights": ["Ancient cave temple", "Chathurmukhalingeshwara", "Pandava connection", "Bhima Bakasura legend"],
                "description": "Hidden gem near Chintamani featuring man-made cave temple with three shrines. Legend says Pandavas lived here during exile.",
                "activities": ["Cave exploration", "Temple visit", "Trekking", "Spiritual experience"],
                "best_time": "October to March",
                "entry_fee": 0,
                "photos": get_curated_photos("Kailasagiri Cave Temple Chintamani"),
                "hidden_gem": True
            },
            {
                "name": "Avani Betta",
                "district": "Kolar",
                "distance_from_bangalore": 100,
                "coordinates": {"lat": 12.8500, "lon": 78.2167},
                "category": "Heritage",
                "highlights": ["Ramayana connection", "Sita Sarovar", "Ancient temples", "Monkey kingdom"],
                "description": "Associated with Ramayana as the monkey kingdom, features Sita Sarovar and ancient temples with mythological significance.",
                "activities": ["Heritage exploration", "Temple visits", "Mythology study", "Photography"],
                "best_time": "October to March",
                "entry_fee": 20,
                "photos": get_curated_photos("Avani Betta Ramayana"),
                "hidden_gem": True
            },
            {
                "name": "Markandeya Hill",
                "district": "Kolar",
                "distance_from_bangalore": 85,
                "coordinates": {"lat": 13.0833, "lon": 78.1500},
                "category": "Trekking",
                "highlights": ["Ancient temple", "Panoramic views", "Less crowded", "Spiritual significance"],
                "description": "A lesser-known hill with ancient Markandeya temple on top, offering panoramic views and spiritual atmosphere.",
                "activities": ["Trekking", "Temple visit", "Meditation", "Photography"],
                "best_time": "October to March",
                "entry_fee": 15,
                "photos": get_curated_photos("Markandeya Hill Kolar"),
                "hidden_gem": True
            },
            {
                "name": "Kolar Betta",
                "district": "Kolar",
                "distance_from_bangalore": 75,
                "coordinates": {"lat": 13.1167, "lon": 78.1167},
                "category": "Adventure",
                "highlights": ["Rock formations", "Adventure activities", "Sunrise views", "Less explored"],
                "description": "A rocky hill with unique formations, perfect for adventure activities and sunrise views. Less explored compared to other hills.",
                "activities": ["Rock climbing", "Sunrise viewing", "Adventure sports", "Photography"],
                "best_time": "October to March",
                "entry_fee": 25,
                "photos": get_curated_photos("Kolar Betta Adventure"),
                "hidden_gem": True
            }
        ]
    },
    
    # WESTERN KARNATAKA HIDDEN GEMS
    "western_karnataka": {
        "region_name": "Western Karnataka Wonders",
        "description": "Hidden treasures in Western Ghats region",
        "destinations": [
            {
                "name": "Sakleshpur Railway Trek Hidden Tunnels",
                "district": "Hassan",
                "distance_from_bangalore": 220,
                "coordinates": {"lat": 12.9444, "lon": 75.7847},
                "category": "Adventure",
                "highlights": ["Hidden railway tunnels", "Green route", "Coffee plantations", "Abandoned stations"],
                "description": "Hidden sections of the famous railway trek with abandoned tunnels and stations through coffee plantations and forests.",
                "activities": ["Railway trekking", "Tunnel exploration", "Photography", "Heritage study"],
                "best_time": "October to March",
                "entry_fee": 50,
                "photos": get_curated_photos("Sakleshpur Hidden Railway Tunnels"),
                "hidden_gem": True
            },
            {
                "name": "Manjarabad Fort Secret Passages",
                "district": "Hassan",
                "distance_from_bangalore": 230,
                "coordinates": {"lat": 12.9167, "lon": 75.8000},
                "category": "Heritage",
                "highlights": ["Star-shaped fort", "Secret passages", "Tipu Sultan era", "Strategic location"],
                "description": "Hidden passages and chambers in the star-shaped fort built by Tipu Sultan, offering insights into military architecture.",
                "activities": ["Fort exploration", "History study", "Photography", "Architecture appreciation"],
                "best_time": "October to March",
                "entry_fee": 30,
                "photos": get_curated_photos("Manjarabad Fort Secret Passages"),
                "hidden_gem": True
            },
            {
                "name": "Belur Hidden Temples",
                "district": "Hassan",
                "distance_from_bangalore": 220,
                "coordinates": {"lat": 13.1667, "lon": 75.8667},
                "category": "Heritage",
                "highlights": ["Lesser-known Hoysala temples", "Intricate carvings", "Peaceful environment", "Architectural marvels"],
                "description": "Hidden Hoysala temples around Belur with intricate carvings, away from the main Chennakeshava temple crowds.",
                "activities": ["Temple exploration", "Architecture study", "Photography", "Peaceful meditation"],
                "best_time": "October to March",
                "entry_fee": 25,
                "photos": get_curated_photos("Belur Hidden Hoysala Temples"),
                "hidden_gem": True
            }
        ]
    }
}

# Seasonal Hidden Gems Recommendations
SEASONAL_HIDDEN_GEMS = {
    "monsoon": {
        "title": "Monsoon Magic - Hidden Waterfalls",
        "season": "June to September",
        "destinations": ["Barkana Falls", "Onake Abbi Falls", "Magod Falls", "Vibhooti Falls", "Dabbe Falls"],
        "description": "Experience Karnataka's hidden waterfalls at their most spectacular during monsoon season."
    },
    
    "winter": {
        "title": "Winter Wanderlust - Hill Station Secrets",
        "season": "December to February",
        "destinations": ["Netravati Peak", "Ettina Bhuja", "Pandavar Gudda", "Kailasagiri Hill"],
        "description": "Perfect weather for exploring hidden hill stations and trekking destinations."
    },
    
    "summer": {
        "title": "Summer Escapes - Coastal Hidden Gems",
        "season": "March to May",
        "destinations": ["Hoode Beach", "Kodi Beach", "Byndoor Beach", "Trasi Beach"],
        "description": "Beat the heat at Karnataka's hidden coastal treasures and pristine beaches."
    },
    
    "post_monsoon": {
        "title": "Post-Monsoon Paradise - Complete Experience",
        "season": "October to November",
        "destinations": ["Agumbe Rainforest", "Yana Rocks", "Sakleshpur Railway Trek", "Kodachadri Peak"],
        "description": "Best time to explore all types of hidden gems with perfect weather and lush landscapes."
    }
}

# Difficulty-based Hidden Gems
DIFFICULTY_BASED_GEMS = {
    "easy": {
        "title": "Easy Hidden Gems for Families",
        "destinations": ["Kailasagiri Hill", "Hoode Beach", "Belur Hidden Temples", "Avani Betta"],
        "description": "Family-friendly hidden gems that are easily accessible and suitable for all ages."
    },
    
    "moderate": {
        "title": "Moderate Adventures",
        "destinations": ["Agumbe Rainforest", "Pandavar Gudda", "Sakleshpur Railway Trek", "Yana Rocks"],
        "description": "Moderately challenging hidden gems for adventure enthusiasts with some experience."
    },
    
    "difficult": {
        "title": "Challenging Hidden Expeditions",
        "destinations": ["Netravati Peak", "Ettina Bhuja", "Barkana Falls", "Kodachadri Peak"],
        "description": "Challenging hidden gems for experienced trekkers and adventure seekers."
    }
}

# Photography-focused Hidden Gems
PHOTOGRAPHY_GEMS = {
    "landscape": ["Agumbe Sunset", "Yana Rocks", "Netravati Peak", "Kodachadri Peak"],
    "waterfall": ["Barkana Falls", "Onake Abbi Falls", "Magod Falls", "Vibhooti Falls"],
    "heritage": ["Kailasagiri Cave Temple", "Manjarabad Fort", "Belur Hidden Temples", "Avani Betta"],
    "coastal": ["Hoode Beach", "Kodi Beach Lighthouse", "Byndoor Beach", "Trasi Beach"],
    "wildlife": ["Agumbe Rainforest", "Kudremukh Hidden Trails", "Netravati Wilderness", "Kodachadri Biodiversity"]
}