from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        
        # Validations
        if not name or len(name) > 50:
            raise ValueError("Name is required and must be less than 50 characters")
        
        self.name = name