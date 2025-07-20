'''
Aqui se maneja la comunicacion entre las capas de Presentacion, logica de negocio y persistencia
Intereactua con los repositorios para realizar operaciones CRUD
'''
from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        
    
    def create_user(self,user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    #PLaceholder method for fetching a place by ID
    def get_place(self, place_id):
        #Logic will be implemented in later tasks
        pass

    