from flask import Flask
from flask_restful import Resource, Api
from .contact.form import HelloWorld

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(HelloWorld,'/')
    return app
