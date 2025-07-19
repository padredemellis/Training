'''
Esta instancia de facade se usará como un singleton para asegurar que solo se cree y use una
instancia de la clase HBnBFacade en toda la aplicación.
'''
from app.services.facade import HBnBFacade

facade = HBnBFacade()