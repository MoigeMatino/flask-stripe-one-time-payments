import os
from flask import Flask
from dotenv import load_dotenv
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")

    # register blueprints
    from .routes import routes_bp
    app.register_blueprint(routes_bp)
    


    return app

