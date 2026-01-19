# 🏛️ Karnataka Travel Planner

An interactive travel planning application built with Streamlit for exploring Karnataka tourism, starting from Bangalore. Plan your perfect Karnataka adventure with our intelligent trip planner!

## ✨ Features

### 🎯 Core Features
- **Interactive Trip Planning**: Create customized itineraries for 1-6 day trips
- **Day Trips from Bangalore**: Explore destinations within 100km for day trips
- **Multi-Day Karnataka Tours**: Comprehensive tour packages for 2-6+ days
- **Smart Recommendations**: AI-powered suggestions based on your preferences
- **Interactive Maps**: Visual trip planning with Folium integration
- **Budget Planning**: Real-time cost calculation and optimization
- **Accommodation Options**: 3-5 star hotels, homestays, resorts, heritage properties
- **Transportation Choices**: Sedan, SUV, Tempo Traveller, AC Bus options

### 🚀 Advanced Features
- **Trip Customization**: Personalize every aspect of your journey
- **Route Optimization**: Minimize travel time and maximize sightseeing
- **Weather Integration**: Plan according to weather conditions
- **Expense Tracking**: Monitor your trip expenses in real-time
- **Itinerary Management**: Save, edit, and share your travel plans
- **Mobile Responsive**: Works seamlessly on all devices

### 🎨 User Experience
- **Intuitive Interface**: Easy-to-use drag-and-drop trip builder
- **Visual Planning**: Interactive maps and photo galleries
- **Multi-language Support**: English, Kannada, Hindi
- **Offline Access**: Download itineraries for offline use
- **Social Sharing**: Share your trips with friends and family

## 🏗️ Architecture

```
karnataka-travel-planner/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── data/
│   └── destinations.py         # Tourism data and destinations
├── utils/
│   └── helpers.py             # Utility functions
├── pages/
│   └── advanced_planner.py    # Advanced planning features
├── config/
│   └── azure_config.py        # Azure deployment configuration
├── deployment/
│   ├── startup.sh             # Azure startup script
│   └── azure-pipelines.yml    # CI/CD pipeline
└── README.md                  # Project documentation
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd karnataka-travel-planner
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

### 🌐 Azure Web App Deployment

#### Prerequisites
- Azure CLI installed and configured
- Azure subscription with appropriate permissions
- Git repository set up

#### Deployment Steps

1. **Create Azure Resources**
   ```bash
   # Create resource group
   az group create --name travel-planner-rg --location "Central India"
   
   # Create App Service Plan
   az appservice plan create \
     --name karnataka-travel-planner-plan \
     --resource-group travel-planner-rg \
     --sku B1 \
     --is-linux
   
   # Create Web App
   az webapp create \
     --resource-group travel-planner-rg \
     --plan karnataka-travel-planner-plan \
     --name karnataka-travel-planner \
     --runtime "PYTHON|3.11" \
     --deployment-local-git
   ```

2. **Configure App Settings**
   ```bash
   az webapp config appsettings set \
     --resource-group travel-planner-rg \
     --name karnataka-travel-planner \
     --settings \
       STREAMLIT_SERVER_PORT=8000 \
       STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
       STREAMLIT_SERVER_HEADLESS=true \
       STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
   ```

3. **Set Startup Command**
   ```bash
   az webapp config set \
     --resource-group travel-planner-rg \
     --name karnataka-travel-planner \
     --startup-file "python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0"
   ```

4. **Deploy Code**
   ```bash
   # Add Azure remote
   git remote add azure <deployment-git-url>
   
   # Deploy
   git push azure main
   ```

#### Alternative: GitHub Actions Deployment

Create `.github/workflows/azure-deploy.yml`:

```yaml
name: Deploy to Azure Web App

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Deploy to Azure Web App
      uses: azure/webapps-deploy@v2
      with:
        app-name: 'karnataka-travel-planner'
        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
```

## 📊 Data Structure

### Destinations Data
- **Day Trip Destinations**: 25+ destinations within 100km of Bangalore
- **Multi-Day Destinations**: Major Karnataka tourist spots
- **Categories**: Hill Stations, Heritage Sites, Wildlife, Adventure, Beaches
- **Details**: Coordinates, distances, activities, best times to visit

### Accommodation Data
- **Types**: 3-5 star hotels, heritage properties, homestays, resorts
- **Pricing**: Dynamic pricing based on season and availability
- **Amenities**: Detailed amenity information for each property type

### Transportation Data
- **Vehicle Types**: Sedan, SUV, Tempo Traveller, AC Bus
- **Pricing**: Per kilometer rates with fuel and toll inclusion
- **Capacity**: Passenger and luggage capacity information

## 🎨 Customization

### Adding New Destinations
1. Edit `data/destinations.py`
2. Add destination data with required fields:
   ```python
   {
       "id": unique_id,
       "name": "Destination Name",
       "distance_km": distance_from_bangalore,
       "coordinates": {"lat": latitude, "lon": longitude},
       "category": "Category",
       "highlights": ["highlight1", "highlight2"],
       "activities": ["activity1", "activity2"],
       # ... other fields
   }
   ```

### Customizing UI Theme
1. Modify CSS in `app.py`
2. Update color schemes and styling
3. Add custom components as needed

### Adding New Features
1. Create new pages in `pages/` directory
2. Import and integrate in main `app.py`
3. Update navigation and routing

## 🔧 Configuration

### Environment Variables
```bash
STREAMLIT_SERVER_PORT=8000
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### Azure-Specific Settings
```bash
SCM_DO_BUILD_DURING_DEPLOYMENT=true
ENABLE_ORYX_BUILD=true
```

## 📱 Mobile Optimization

The application is fully responsive and optimized for:
- **Mobile Phones**: Touch-friendly interface
- **Tablets**: Optimized layout for medium screens
- **Desktop**: Full-featured experience

## 🔒 Security Features

- **Input Validation**: All user inputs are validated
- **HTTPS Enforcement**: Secure connections in production
- **Session Management**: Secure session handling
- **Data Privacy**: No sensitive data storage

## 📈 Performance Optimization

- **Caching**: Streamlit caching for improved performance
- **Lazy Loading**: Images and data loaded on demand
- **Compression**: Gzip compression enabled
- **CDN Ready**: Static assets can be served via CDN

## 🧪 Testing

Run tests locally:
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ --cov=.
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team
- Check the documentation wiki

## 🚀 Future Enhancements

- **AI-Powered Recommendations**: Machine learning for personalized suggestions
- **Real-time Booking**: Integration with booking platforms
- **Social Features**: User reviews and ratings
- **Offline Maps**: Downloadable offline maps
- **Multi-language**: Additional regional language support
- **Weather API**: Real-time weather integration
- **Payment Gateway**: Direct booking and payment processing

---

**Built with ❤️ for Karnataka Tourism**

Explore the incredible diversity of Karnataka - from the tech hub of Bangalore to the royal heritage of Mysore, from the coffee plantations of Coorg to the ancient ruins of Hampi. Your perfect Karnataka adventure awaits!