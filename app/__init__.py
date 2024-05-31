import os
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# # Initialize database
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")

    # Initialize database and migration object with flask app
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from .routes import routes_bp
    app.register_blueprint(routes_bp)

    
    


    return app

