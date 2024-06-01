from .api_routes import api_bp
from .main_routes import routes_bp

def register_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(routes_bp, url_prefix='/')