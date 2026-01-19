# 🧪 Local Testing Guide for Karnataka Travel Planner

## Quick Start Testing

### **Method 1: Local Machine Testing**

1. **Clone your repository:**
   ```bash
   git clone https://github.com/yourusername/TravelPlanner.git
   cd TravelPlanner
   ```

2. **Fix any import issues:**
   ```bash
   python fix_imports.py
   ```

3. **Run pre-deployment tests:**
   ```bash
   python test_app.py
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser:**
   - Navigate to `http://localhost:8501`
   - Test all features and navigation

### **Method 2: GitHub Codespaces (Recommended)**

1. **Go to your GitHub repository**
2. **Click "Code" → "Codespaces" → "Create codespace"**
3. **Once loaded, run:**
   ```bash
   python fix_imports.py
   pip install -r requirements.txt
   streamlit run app.py --server.port 8000 --server.address 0.0.0.0
   ```
4. **Codespaces will provide a URL to access your app**

### **Method 3: GitHub Pages (Static Preview)**
*Note: This won't run the Streamlit app but lets you browse the code structure*

1. Go to your repository settings
2. Enable GitHub Pages from main branch
3. Browse the markdown files and code structure

## 🔍 **What to Test**

### **Core Functionality**
- [ ] Home page loads correctly
- [ ] Navigation between different sections works
- [ ] Direction-wise itineraries display properly
- [ ] Hidden gems pages load with content
- [ ] Maps render correctly (may show placeholders locally)
- [ ] Photo galleries display (may show placeholder images)

### **Data Integrity**
- [ ] All destinations load with proper information
- [ ] Kailasagiri Hill appears in Eastern Karnataka section
- [ ] Direction-wise itineraries show correct distances
- [ ] Interactive maps display markers
- [ ] Search and filter functions work

### **User Interface**
- [ ] Responsive design works on different screen sizes
- [ ] Buttons and interactions function properly
- [ ] Color scheme and styling appear correctly
- [ ] Navigation is intuitive and smooth

## 🐛 **Common Issues & Fixes**

### **Import Errors**
```bash
# If you get import errors, run:
python fix_imports.py

# Then try again:
streamlit run app.py
```

### **Missing Dependencies**
```bash
# Install missing packages:
pip install streamlit pandas folium streamlit-folium plotly requests pillow

# Or install from requirements:
pip install -r requirements.txt
```

### **Photo Service Issues**
- Photos may show as placeholders without API keys
- This is normal for local testing
- App will still function with placeholder images

### **Secrets Configuration**
- Create `.streamlit/secrets.toml` for API keys (optional for testing)
- App works without secrets using placeholder content

## 📊 **Testing Checklist**

### **Navigation Testing**
- [ ] Home page → Direction Itineraries
- [ ] Direction Itineraries → All 9 directions work
- [ ] Karnataka Hidden Gems → All 6 regions work
- [ ] Waterfalls, Heritage Sites, Beaches pages load
- [ ] Back navigation works properly

### **Content Testing**
- [ ] Kailasagiri Hill appears in Kolar direction
- [ ] All hidden gems have descriptions and photos
- [ ] Interactive maps show correct locations
- [ ] Distance calculations appear accurate
- [ ] Entry fees and timing information display

### **Functionality Testing**
- [ ] "Add to Trip" buttons work
- [ ] "Get Directions" opens maps
- [ ] Search and filter functions operate
- [ ] Seasonal recommendations display
- [ ] Difficulty-based categorization works

### **Performance Testing**
- [ ] Pages load within reasonable time
- [ ] Large datasets don't cause crashes
- [ ] Memory usage remains stable
- [ ] No console errors in browser

## 🚀 **Pre-Deployment Validation**

### **Run Complete Test Suite**
```bash
# Run all automated tests
python test_app.py

# Expected output:
# ✅ All required modules available
# ✅ destinations.py - X day trips, Y multi-day
# ✅ bangalore_direction_itineraries.py - 9 directions
# ✅ karnataka_hidden_gems.py - 6 regions
# ✅ All components load successfully
# 🎉 All tests passed! Ready for deployment.
```

### **Manual Testing Scenarios**

1. **Tourist Planning Day Trip:**
   - Navigate to "Direction Itineraries"
   - Select "Towards Kolar (Golden Route)"
   - Verify Kailasagiri Hill appears with details
   - Test "Add to Trip" functionality

2. **Explorer Seeking Hidden Gems:**
   - Go to "Karnataka Hidden Gems"
   - Browse different regions
   - Check photo galleries and descriptions
   - Test interactive maps

3. **Adventure Enthusiast:**
   - Use difficulty-based filtering
   - Check seasonal recommendations
   - Verify activity categorization

## 📱 **Mobile Testing**

Test on different screen sizes:
- Desktop (1920x1080)
- Tablet (768x1024) 
- Mobile (375x667)

Verify:
- [ ] Responsive layout adapts properly
- [ ] Touch interactions work on mobile
- [ ] Maps are usable on small screens
- [ ] Text remains readable

## 🔧 **Debug Mode**

For detailed debugging, run with debug flags:
```bash
streamlit run app.py --logger.level=debug
```

This will show detailed logs for troubleshooting.

## ✅ **Ready for Azure Deployment**

Once local testing passes:

1. **All tests pass:** `python test_app.py` shows green checkmarks
2. **Manual testing complete:** All major features work
3. **No console errors:** Browser console is clean
4. **Performance acceptable:** Pages load smoothly

You're ready to deploy to Azure Web App!

## 🆘 **Getting Help**

If you encounter issues:

1. **Check the console:** Browser developer tools → Console tab
2. **Review logs:** Terminal where Streamlit is running
3. **Test individual components:** Import modules separately
4. **Verify file structure:** Ensure all files are in correct locations

---

**Happy Testing! Your Karnataka Travel Planner is ready to showcase the hidden gems of Karnataka! 🏛️✨**