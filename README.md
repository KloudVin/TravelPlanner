# 🏛️ Karnataka Travel Planner

A comprehensive interactive travel planning application for exploring Karnataka tourism from Bangalore. Discover hidden gems, plan day trips, and create multi-day adventures across Karnataka's diverse landscapes.

## ✨ Features Overview

### 🎯 Core Travel Planning
- **Day Trips from Bangalore**: 25+ destinations within 100km including hidden gems like Kailasagiri Hill
- **Multi-Day Karnataka Tours**: Comprehensive 2-6+ day packages covering heritage, nature, and adventure
- **Direction-Based Itineraries**: Organized routes in 8 directions from Bangalore (Hosur, Kolar, Kanakapura, Mysore, Magadi, Tumkur, Doddaballapur, Devanahalli)
- **Interactive Maps**: Visual trip planning with Folium integration and location details
- **Budget Planning**: Real-time cost calculation with accommodation and transport options

### 🏞️ Destination Categories
- **Heritage Sites**: UNESCO World Heritage Sites (Hampi, Pattadakal) and hidden temples
- **Hill Stations**: Nandi Hills, Coorg, Chikmagalur, Agumbe, and secret viewpoints
- **Waterfalls**: 10+ waterfalls including Jog Falls, hidden gems like Barkana Falls (259m)
- **Adventure Sports**: Rock climbing, trekking, cave exploration, river rafting
- **Beaches**: Gokarna, Karwar, and pristine coastal hidden gems
- **Spiritual Sites**: Ancient temples, cave temples, and pilgrimage circuits

### 💎 Hidden Gems Database
- **100+ Lesser-Known Destinations**: Carefully curated offbeat locations
- **Regional Coverage**: North, South, Central, Eastern, Western, and Coastal Karnataka
- **Kailasagiri Hill**: Featured hidden gem near Chintamani with ancient cave temple
- **Seasonal Recommendations**: Best hidden gems for each season
- **Difficulty Levels**: Easy, moderate, and challenging hidden expeditions

### 🏨 Accommodation & Transport
- **6 Accommodation Types**: 3-5 star hotels, heritage properties, homestays, resorts
- **4 Transport Options**: AC Sedan (₹12/km), SUV (₹16/km), Tempo Traveller (₹22/km), AC Bus (₹35/km)
- **Dynamic Pricing**: Real-time cost calculation based on distance and preferences
- **Package Customization**: Personalize accommodation, meals, and transport

### 📱 User Experience
- **Mobile Responsive**: Optimized for all devices
- **Interactive Interface**: Easy navigation with sidebar and tabbed content
- **Multimedia Integration**: Curated photos and videos for destinations
- **Itinerary Management**: Save, customize, and share travel plans
- **Fallback Handling**: Graceful degradation when services are unavailable

## 🏗️ Application Architecture

```
├── app.py                     # Main Streamlit application (1,200+ lines)
├── requirements.txt           # Production dependencies (7 packages)
├── startup.sh                # Production startup script
├── verify_deployment.py      # Deployment verification tool
├── data/                     # Comprehensive tourism database
│   ├── destinations.py       # 100+ destinations with multimedia
│   ├── karnataka_hidden_gems.py  # Regional hidden gems database
│   └── bangalore_direction_itineraries.py  # Direction-wise routes
├── components/               # UI and multimedia components
│   └── multimedia.py         # Photo galleries, maps, showcases
├── pages/                    # Application pages
│   └── direction_itineraries.py  # Direction-based trip planning
├── services/                 # External services integration
│   └── photo_service.py      # Photo fetching with API fallbacks
├── utils/                    # Utility functions
│   └── helpers.py            # Common helper functions
├── deployment/               # Azure deployment automation
│   ├── create_azure_resources.sh  # Resource creation script
│   └── get_publish_profile.sh     # Deployment profile script
├── .github/workflows/        # CI/CD automation
│   └── azure-deploy.yml      # GitHub Actions pipeline
└── .streamlit/              # Streamlit configuration
    └── config.toml          # Production-optimized settings
```

## 📊 Data Specifications

### 🗺️ Destinations Database
- **Day Trip Destinations**: 25+ locations within 100km
  - Categories: Hill stations, waterfalls, adventure, heritage, spiritual
  - Complete details: coordinates, entry fees, facilities, activities
  - Difficulty levels: Easy to challenging
  - Time requirements: 2-10 hours per destination

- **Multi-Day Destinations**: 15+ major Karnataka attractions
  - UNESCO Sites: Hampi, Pattadakal (World Heritage Sites)
  - Hill Stations: Coorg, Chikmagalur, Agumbe, Kudremukh
  - Beaches: Gokarna, Karwar with pristine coastlines
  - Heritage: Ancient temples, forts, archaeological sites

### 💎 Hidden Gems Collection
- **Regional Distribution**:
  - North Karnataka: Yana Rocks, Sathodi Falls, Magod Falls
  - Central Karnataka: Agumbe Rainforest, Barkana Falls (259m)
  - South Karnataka: Netravati Peak, Ettina Bhuja, Pandavar Gudda
  - Eastern Karnataka: Kailasagiri Hill, Avani Betta, Markandeya Hill
  - Western Karnataka: Secret railway tunnels, hidden Hoysala temples
  - Coastal Karnataka: Hoode Beach, Kodi Beach, pristine coastlines

- **Seasonal Categorization**:
  - Monsoon Magic: Hidden waterfalls at peak flow
  - Winter Wanderlust: Perfect trekking weather destinations
  - Summer Escapes: Coastal gems and hill stations
  - Post-Monsoon Paradise: Complete experience destinations

### 🏨 Accommodation Database
- **6 Categories**: 3-star (₹2K-4K), 4-star (₹4K-8K), 5-star (₹8K-20K)
- **Heritage Properties**: Converted palaces (₹5K-15K)
- **Homestays**: Authentic local experience (₹1.5K-3.5K)
- **Resorts**: All-inclusive facilities (₹6K-18K)

### 🚗 Transportation Matrix
- **AC Sedan**: 4 passengers, ₹12/km (Swift Dzire, Honda Amaze)
- **AC SUV**: 6-7 passengers, ₹16/km (Toyota Innova, Mahindra Xylo)
- **Tempo Traveller**: 12 passengers, ₹22/km (Force Traveller)
- **AC Bus**: 25+ passengers, ₹35/km (Volvo, Mercedes)

## 🚀 Quick Start & Deployment

### 💻 Local Development
```bash
# Clone and setup
git clone <repository-url>
cd karnataka-travel-planner
pip install -r requirements.txt

# Run application
streamlit run app.py
# Access at: http://localhost:8501
```

### ☁️ Azure Production Deployment

#### Prerequisites
- Azure CLI installed and configured
- Azure subscription with App Service permissions
- GitHub repository with Actions enabled

#### 🎯 One-Click Azure Setup
```bash
# Navigate to deployment directory
cd deployment

# Make scripts executable (Linux/Mac)
chmod +x create_azure_resources.sh
chmod +x get_publish_profile.sh

# Create all Azure resources
./create_azure_resources.sh
```

**This creates**:
- Resource Group: `TravelPlanner`
- Web App: `vintekh` (vintekh.azurewebsites.net)
- App Service Plan: `vintekh-plan` (B1 tier)
- All required configurations for Streamlit

#### 🔄 GitHub Actions Deployment
```bash
# Get publish profile for GitHub secrets
./deployment/get_publish_profile.sh

# Add to GitHub repository secrets:
# AZURE_WEBAPP_PUBLISH_PROFILE = <output from above command>

# Push to main branch triggers automatic deployment
git push origin main
```

#### 🌐 Access Points
- **Azure URL**: https://vintekh.azurewebsites.net
- **Custom Domain**: vintekh.com (configure DNS separately)
- **Admin Portal**: Azure Portal → TravelPlanner → vintekh

### 🔧 Production Configuration

#### Environment Variables (Auto-configured)
```bash
STREAMLIT_SERVER_PORT=8000
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
WEBSITES_PORT=8000
SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

#### Optional API Keys (for enhanced photos)
```bash
# Add to Azure App Settings for better photo quality
UNSPLASH_ACCESS_KEY=your_unsplash_key
PEXELS_API_KEY=your_pexels_key
# App works with placeholder images if not provided
```

## 🎯 Application Features Deep Dive

### 📍 Direction-Based Trip Planning
**8 Curated Routes from Bangalore**:

1. **Inside Bangalore** (50-80km): Hidden city gems
   - Turahalli Forest (rock climbing, mountain biking)
   - Big Banyan Tree (400-year-old natural wonder)
   - Nrityagram Cultural Village (dance performances)

2. **Towards Hosur** (120-150km): Tamil Nadu border treasures
   - Kelavarapalli Dam (boating, fishing)
   - Ancient Dravidian temples with unique architecture

3. **Towards Kolar** (140-180km): Gold mining heritage
   - Antaragange Caves (volcanic rock formations)
   - Kotilingeshwara Temple (10 million Shiva lingas)
   - KGF Heritage (historic gold mines, movie locations)

4. **Towards Kanakapura** (160-200km): Natural wonders
   - Chunchi Falls (50-foot cascade with natural pools)
   - Bilikal Rangaswamy Betta (temple under granite rock)
   - Mekedatu (spectacular river gorge)

5. **Towards Mysore** (120-160km): Royal heritage route
   - Muthyala Maduvu (Pearl Valley waterfall)
   - Kanva Reservoir (serene boating destination)

6. **Towards Magadi** (100-140km): Rocky landscapes
   - Savandurga (Asia's largest monolith)
   - Manchanabele Dam (adventure sports hub)

7. **Towards Tumkur** (120-150km): Spiritual heights
   - Devarayanadurga (hill station with temples)
   - Madhugiri Fort (Asia's second-largest monolith)

8. **Towards Doddaballapur** (80-120km): Hills and heritage
   - Nandi Hills (sunrise point, paragliding)
   - Ghati Subramanya Temple (serpent curse remedies)

### 🏛️ Heritage & Culture
- **UNESCO World Heritage Sites**: Hampi (Vijayanagara Empire), Pattadakal (Chalukya temples)
- **Architectural Styles**: Dravidian, Nagara, Hoysala, Vijayanagara, Chalukyan
- **Hidden Heritage**: Aihole (125+ temples), Halebidu (intricate Hoysala carvings)
- **Cave Temples**: Badami rock-cut caves, Kailasagiri cave temple complex

### 💧 Waterfall Adventures
- **Major Waterfalls**: Jog Falls (253m, 2nd highest in India)
- **Hidden Cascades**: Barkana Falls (259m, 10th highest in India)
- **Seasonal Spectacles**: Best during monsoon (June-September)
- **Adventure Activities**: Trekking, photography, natural pool swimming

### 🏖️ Coastal Experiences
- **Sacred Beaches**: Gokarna (Om Beach, spiritual significance)
- **Pristine Coastlines**: Karwar, Hoode Beach, Kodi Beach
- **Activities**: Beach trekking, water sports, dolphin spotting
- **Hidden Gems**: Byndoor Beach, Trasi Beach (less commercialized)

### 🎒 Adventure Sports Hub
- **Rock Climbing**: Savandurga, Ramanagara, Turahalli Forest
- **Cave Exploration**: Antaragange, Yana Rocks limestone formations
- **Water Sports**: Manchanabele Dam (kayaking, rappelling)
- **Trekking**: Skandagiri night trek, Kudremukh peak, Netravati wilderness

### 📱 Smart Features
- **Multimedia Integration**: Curated photos from Unsplash API with fallbacks
- **Interactive Maps**: Folium-powered maps with destination markers
- **Budget Calculator**: Real-time cost estimation with customizable parameters
- **Seasonal Recommendations**: AI-powered suggestions based on current season
- **Difficulty Filtering**: Easy/moderate/challenging options for all fitness levels

## 🔍 Technical Specifications

### 🛠️ Technology Stack
- **Frontend**: Streamlit 1.28.1 (Python web framework)
- **Mapping**: Folium 0.15.0 + Streamlit-Folium integration
- **Data Visualization**: Plotly 5.17.0 (interactive charts)
- **Data Processing**: Pandas 2.1.3 (destination data management)
- **Image Handling**: Pillow 10.1.0 + requests for API integration
- **Deployment**: Azure App Service with Python 3.11 runtime

### 📊 Performance Optimizations
- **Caching**: Streamlit native caching for destination data
- **Lazy Loading**: Images loaded on-demand to reduce initial load time
- **Fallback Systems**: Graceful degradation when external APIs unavailable
- **Responsive Design**: Mobile-first approach with adaptive layouts
- **Production Config**: Optimized for cloud deployment with proper error handling

## 🎨 Sample Itineraries

### 🏃‍♂️ Adventure Seeker's Paradise (2 Days)
**Day 1**: Antaragange Cave Complex → Rock climbing and cave exploration
**Day 2**: Savandurga Monolith → Manchanabele Dam water sports
**Activities**: Cave exploration, rock climbing, kayaking, rappelling
**Budget**: ₹4,500 per person (transport + activities + basic accommodation)

### 🙏 Spiritual Circuit (2 Days)
**Day 1**: Kotilingeshwara Temple → Devarayanadurga hill temples
**Day 2**: Ghati Subramanya Temple → Bilikal Rangaswamy Betta
**Activities**: Temple visits, meditation, spiritual trekking, sacred spring visit
**Budget**: ₹3,200 per person (transport + accommodation + meals)

### 📸 Nature Photography Trail (3 Days)
**Day 1**: Chunchi Falls → Muthyala Maduvu (Pearl Valley)
**Day 2**: Nandi Hills sunrise → Hesaraghatta Lake bird photography
**Day 3**: Agumbe Rainforest → Sunset point photography
**Activities**: Waterfall photography, sunrise/sunset shots, bird photography, landscape shots
**Budget**: ₹6,800 per person (transport + accommodation + equipment)

### 🏛️ Heritage Explorer (4 Days)
**Day 1**: Bangalore → Hampi (UNESCO World Heritage Site)
**Day 2**: Hampi full day → Vittala Temple, Royal Enclosure
**Day 3**: Hampi → Badami Cave Temples → Aihole
**Day 4**: Pattadakal UNESCO site → Return to Bangalore
**Activities**: Heritage walks, architecture study, cultural immersion, photography
**Budget**: ₹12,500 per person (transport + heritage hotels + guide + meals)

### 💎 Hidden Gems Discovery (3 Days)
**Day 1**: Kailasagiri Cave Temple → Antaragange Caves
**Day 2**: Yana Rocks → Agumbe Rainforest
**Day 3**: Barkana Falls → Onake Abbi Falls
**Activities**: Cave exploration, unique rock formations, rainforest trekking, hidden waterfalls
**Budget**: ₹8,200 per person (transport + eco-stays + trekking gear + meals)

## 🌟 Why Choose Karnataka Travel Planner?

### ✅ Comprehensive Coverage
- **100+ Destinations**: From famous attractions to hidden gems
- **All Categories**: Heritage, nature, adventure, spiritual, beaches
- **Complete Information**: Photos, videos, activities, facilities, pricing
- **Real Reviews**: Authentic experiences and recommendations

### ✅ Smart Planning Tools
- **Interactive Maps**: Visual trip planning with route optimization
- **Budget Calculator**: Real-time cost estimation with customization
- **Seasonal Recommendations**: Best destinations for current weather
- **Difficulty Levels**: Options for all fitness and experience levels

### ✅ Local Expertise
- **Hidden Gems Focus**: Destinations most tourists miss
- **Cultural Insights**: Local customs, festivals, and traditions
- **Practical Tips**: Best times to visit, what to carry, local contacts
- **Authentic Experiences**: Homestays, local guides, cultural immersion

### ✅ Production Ready
- **Cloud Deployed**: Accessible from anywhere on any device
- **Mobile Optimized**: Perfect experience on phones and tablets
- **Fast Loading**: Optimized for quick access and smooth navigation
- **Reliable**: Fallback systems ensure app works even with limited connectivity

## 🔧 Configuration & Environment

### Environment Variables (Auto-configured)
```bash
STREAMLIT_SERVER_PORT=8000
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
WEBSITES_PORT=8000
SCM_DO_BUILD_DURING_DEPLOYMENT=true
ENABLE_ORYX_BUILD=true
```

### Optional API Keys (Enhanced Features)
```bash
# Add to Azure App Settings for better photo quality
UNSPLASH_ACCESS_KEY=your_unsplash_key_here
PEXELS_API_KEY=your_pexels_key_here
YOUTUBE_API_KEY=your_youtube_key_here
# App works perfectly with placeholder images if not provided
```

### Azure Resource Configuration
- **Resource Group**: TravelPlanner
- **Web App Name**: vintekh
- **Runtime Stack**: Python 3.11
- **Location**: Central India
- **Pricing Tier**: B1 (Basic, scalable to higher tiers)

## 🚀 Future Enhancements

### 🔮 Planned Features
- **AI Trip Planner**: Machine learning recommendations based on preferences
- **Real-time Booking**: Direct integration with hotels and transport providers
- **Weather Integration**: Live weather data for better trip planning
- **Social Features**: User reviews, photo sharing, trip recommendations
- **Offline Mode**: Download itineraries and maps for offline access
- **Multi-language**: Kannada, Hindi, and other regional languages
- **Payment Gateway**: Direct booking and payment processing
- **Live Chat**: Real-time support and local guide connections

### 📱 Mobile App Development
- **Native Apps**: iOS and Android versions with enhanced features
- **GPS Navigation**: Turn-by-turn directions to destinations
- **Augmented Reality**: AR features for heritage sites and landmarks
- **Push Notifications**: Weather alerts, festival updates, special offers

## 🧪 Testing & Quality Assurance

### ✅ Pre-deployment Verification
```bash
# Run comprehensive tests
python verify_deployment.py

# Check for:
# - All required files present
# - Python dependencies available
# - App structure integrity
# - Azure configuration correctness
```

### 🔍 Monitoring & Analytics
- **Application Insights**: Performance monitoring and error tracking
- **User Analytics**: Usage patterns and popular destinations
- **Performance Metrics**: Load times, user engagement, conversion rates
- **Error Handling**: Graceful fallbacks and user-friendly error messages

## 📞 Support & Community

### 🤝 Getting Help
- **GitHub Issues**: Report bugs and request features
- **Documentation**: Comprehensive guides and FAQs available
- **Community Forum**: Join our traveler community for tips and experiences
- **Email Support**: Direct support for deployment and technical issues

### 🌐 Important Links
- **Live Application**: https://vintekh.azurewebsites.net
- **GitHub Repository**: [Your Repository URL]
- **Azure Portal**: TravelPlanner Resource Group
- **Custom Domain**: vintekh.com (DNS configuration required)

### 📊 Usage Statistics
- **Destinations Covered**: 100+ locations across Karnataka
- **Hidden Gems**: 50+ lesser-known destinations
- **Photo Gallery**: 500+ curated images with API integration
- **Route Options**: 8 direction-based itineraries from Bangalore
- **Budget Range**: ₹1,000 to ₹30,000+ per person options

---

## 🏆 Achievements & Recognition

### 🌟 Key Highlights
- **Comprehensive Database**: Most extensive Karnataka tourism data collection
- **Hidden Gems Focus**: Unique emphasis on offbeat destinations
- **Production Ready**: Fully deployed and scalable cloud application
- **Mobile Optimized**: Perfect experience across all devices
- **Local Expertise**: Authentic insights from Karnataka tourism experts

### 🎯 Impact Goals
- **Promote Sustainable Tourism**: Encourage responsible travel practices
- **Support Local Communities**: Highlight homestays and local guides
- **Preserve Heritage**: Document and promote Karnataka's cultural treasures
- **Environmental Awareness**: Promote eco-friendly travel options

---

**🏛️ Built with ❤️ for Karnataka Tourism**

*Discover the incredible diversity of Karnataka - from the tech hub of Bangalore to the royal heritage of Mysore, from the coffee plantations of Coorg to the ancient ruins of Hampi, from the pristine beaches of Gokarna to the hidden waterfalls of Western Ghats. Your perfect Karnataka adventure starts here!*

**🎯 Mission**: Make Karnataka's hidden treasures accessible to every traveler while promoting sustainable and responsible tourism.

**🌟 Vision**: Become the most comprehensive and trusted platform for Karnataka tourism, connecting travelers with authentic local experiences and hidden gems.

**📧 Contact**: For partnerships, suggestions, or support - reach out through GitHub issues or Azure portal.

---

*Last Updated: January 2026 | Version: 2.0 Production | Deployment: Azure App Service*