from flask import Flask
from flask_restx import Api

def create_app():
    "Instance of Flask app"
    app = Flask(__name__)
    api = Api(app, version='1.0',title='HBnB API', description='HBnB API', doc='/api/v1/')
    #Placeholder for API namespaces(endpoints will be ADDED LATER)
    #Aditional namespaces for places, reviews, and amenities will be added later
    return app

    