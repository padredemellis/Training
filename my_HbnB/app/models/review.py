from .base_model import BaseModel
from .place import Place
from .user  import User

class Review(BaseModel):
    def __init__(self, text: str, rating: int, place: Place, user: User):
        super().__init__()
        
        # Validations
        if not text or len(text) > 500:
            raise ValueError("Text is required and must be less than 500 characters")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        if not isinstance(place, Place):
            raise ValueError("Place must be an instance of Place")
        if not isinstance(user, User):
            raise ValueError("User must be an instance of User")
        
        self.text = text
        self.rsting = rating
        self.place = place
        self.user = user
        
        place.add_review(self)
        user.reviews.append(self)