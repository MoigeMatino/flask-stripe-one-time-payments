import os
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

# # Initialize database
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")

    # Initialize database with flask app
    db.init_app(app)

    # register blueprints
    from .routes import routes_bp
    app.register_blueprint(routes_bp)
    


    return app

