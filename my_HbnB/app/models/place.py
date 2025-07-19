from .base_model import BaseModel
from .user import User
import re

class Place(BaseModel):
    def __init__(self, title: str, price: float, latitude:float, longitude:float, owner:User, description: str = ""):
        super().__init__()
        
        #Validations
        if not title or len(title)> 100:
            raise ValueError("Title is required and must be less than 100 characters")
        if price <= 0:
            raise ValueError("Price must be a positive number")
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude must be between -90 and 90")
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude must be between -180 and 180")
        if not isinstance(owner, User):
            raise ValueError("Owner must be an instance of User")
        
        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.description = ""
        
        #Relationships
        self.reviews = []
        self.amenities = []
        
    def add_review(self, review):
        """Add review to the place"""
        if not hasattr(review, 'place'):
            review.place = self
        elif review.place is not self:
            raise ValueError("Review doesn't belong to this place")
        self.reviews.append(review)
    
    def add_amenity(self, amenity):
        """Add amenity to the place"""
        self.amenities.append(amenity)