'''
Configuraciones especificas del entorno de la aplicación HBnB.
Contiene configuraciones como la clave secreta, base de datos y otros parámetros necesarios.
'''
import os

class Config:
    #Contiene las configuraciones comunes de todos los entornos
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
