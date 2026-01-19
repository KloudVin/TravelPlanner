"""
Photo Service for Karnataka Travel Planner
Integrates with various photo APIs and services
"""

import streamlit as st
import requests
import json
from typing import List, Dict, Optional

class PhotoService:
    """Service to fetch and manage destination photos"""
    
    def __init__(self):
        try:
            self.unsplash_access_key = st.secrets.get("UNSPLASH_ACCESS_KEY", "")
            self.pexels_api_key = st.secrets.get("PEXELS_API_KEY", "")
        except:
            # Handle case when secrets are not available (local testing)
            self.unsplash_access_key = ""
            self.pexels_api_key = ""
        self.cache = {}
    
    def get_destination_photos(self, destination_name: str, count: int = 5) -> List[str]:
        """
        Fetch photos for a destination from multiple sources
        
        Args:
            destination_name: Name of the destination
            count: Number of photos to fetch
            
        Returns:
            List of photo URLs
        """
        
        # Check cache first
        cache_key = f"{destination_name}_{count}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        photos = []
        
        # Try Unsplash first
        if self.unsplash_access_key:
            unsplash_photos = self._fetch_unsplash_photos(destination_name, count)
            photos.extend(unsplash_photos)
        
        # Try Pexels if we need more photos
        if len(photos) < count and self.pexels_api_key:
            remaining = count - len(photos)
            pexels_photos = self._fetch_pexels_photos(destination_name, remaining)
            photos.extend(pexels_photos)
        
        # Fallback to placeholder images
        while len(photos) < count:
            placeholder_url = self._generate_placeholder_image(destination_name, len(photos))
            photos.append(placeholder_url)
        
        # Cache the results
        self.cache[cache_key] = photos[:count]
        return photos[:count]
    
    def _fetch_unsplash_photos(self, query: str, count: int) -> List[str]:
        """Fetch photos from Unsplash API"""
        
        try:
            url = "https://api.unsplash.com/search/photos"
            headers = {"Authorization": f"Client-ID {self.unsplash_access_key}"}
            params = {
                "query": f"{query} Karnataka India",
                "per_page": count,
                "orientation": "landscape"
            }
            
            response = requests.get(url, headers=headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                photos = []
                
                for photo in data.get("results", []):
                    # Use regular size for better loading
                    photo_url = photo["urls"]["regular"]
                    photos.append(photo_url)
                
                return photos
            
        except Exception as e:
            st.error(f"Error fetching Unsplash photos: {e}")
        
        return []
    
    def _fetch_pexels_photos(self, query: str, count: int) -> List[str]:
        """Fetch photos from Pexels API"""
        
        try:
            url = "https://api.pexels.com/v1/search"
            headers = {"Authorization": self.pexels_api_key}
            params = {
                "query": f"{query} Karnataka India",
                "per_page": count,
                "orientation": "landscape"
            }
            
            response = requests.get(url, headers=headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                photos = []
                
                for photo in data.get("photos", []):
                    # Use medium size for better loading
                    photo_url = photo["src"]["medium"]
                    photos.append(photo_url)
                
                return photos
            
        except Exception as e:
            st.error(f"Error fetching Pexels photos: {e}")
        
        return []
    
    def _generate_placeholder_image(self, destination_name: str, index: int) -> str:
        """Generate placeholder image URL"""
        
        # Color palette for different types of destinations
        colors = {
            0: "4CAF50",  # Green for nature
            1: "2196F3",  # Blue for water
            2: "FF9800",  # Orange for heritage
            3: "9C27B0",  # Purple for spiritual
            4: "F44336"   # Red for adventure
        }
        
        color = colors.get(index % 5, "607D8B")
        encoded_name = destination_name.replace(" ", "+")
        
        return f"https://via.placeholder.com/800x600/{color}/FFFFFF?text={encoded_name}"
    
    def get_video_content(self, destination_name: str) -> Optional[str]:
        """
        Get video content for destination (YouTube search)
        
        Args:
            destination_name: Name of the destination
            
        Returns:
            YouTube video embed URL or None
        """
        
        # For now, return a placeholder
        # In production, integrate with YouTube API
        search_query = destination_name.replace(" ", "+")
        return f"https://www.youtube.com/results?search_query={search_query}+Karnataka+tourism"

# Curated photo collections for major destinations
CURATED_PHOTOS = {
    "Hampi": [
        "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800",
        "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800",
        "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800"
    ],
    "Mysore Palace": [
        "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800",
        "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800"
    ],
    "Coorg": [
        "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800"
    ],
    "Jog Falls": [
        "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800"
    ],
    "Gokarna": [
        "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800"
    ]
}

def get_curated_photos(destination_name: str) -> List[str]:
    """Get curated photos for popular destinations"""
    
    # Check if we have curated photos
    for key, photos in CURATED_PHOTOS.items():
        if key.lower() in destination_name.lower():
            return photos
    
    # Fallback to photo service
    photo_service = PhotoService()
    return photo_service.get_destination_photos(destination_name, 3)

# Video content mapping
DESTINATION_VIDEOS = {
    "Hampi": "https://www.youtube.com/embed/dQw4w9WgXcQ",  # Replace with actual video IDs
    "Mysore": "https://www.youtube.com/embed/dQw4w9WgXcQ",
    "Coorg": "https://www.youtube.com/embed/dQw4w9WgXcQ",
    "Jog Falls": "https://www.youtube.com/embed/dQw4w9WgXcQ",
    "Gokarna": "https://www.youtube.com/embed/dQw4w9WgXcQ"
}

def get_destination_video(destination_name: str) -> Optional[str]:
    """Get video content for destination"""
    
    for key, video_url in DESTINATION_VIDEOS.items():
        if key.lower() in destination_name.lower():
            return video_url
    
    return None

# Initialize photo service
photo_service = PhotoService()