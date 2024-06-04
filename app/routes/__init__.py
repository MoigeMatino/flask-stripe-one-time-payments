from .api import api_bp
from .stripe import stripe_bp
from .frontend import frontend_bp

def register_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(stripe_bp, url_prefix='/stripe')
    app.register_blueprint(frontend_bp,url_prefix='/')