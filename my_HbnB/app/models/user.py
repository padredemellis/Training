from base_model import BaseModel
import re

class User(BaseModel):
    '''User model class representing a user in the HBnB application.'''
    def __init__(self, first_name: str = "", last_name: str = "", email: str = "", password: str = "", is_admin: bool = False):
        super().__init__()
        #Validations
        if not first_name or len(first_name) > 50:
            raise ValueError("First name requiered max length 50 characters")
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name requiered max length 50 characters")
        if not email or len(email) > 100 or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format or length exceeds 100 characters")
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        
        #Placeholders for relationships
        self.places = []
        self.reviews = []