import uuid
from datetime import datetime

class BaseModel:
    """Base model class for all models in the application."""
    def __init__(self):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.crated_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
    
    def update(self, data):    
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()