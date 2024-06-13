from os import environ

class Config:
    STRIPE_PUBLISHABLE_KEY=environ.get("STRIPE_PUBLISHABLE_KEY")
    STRIPE_SECRET_KEY=environ.get("STRIPE_SECRET_KEY")
    STRIPE_ENDPOINT_SECRET=environ.get("STRIPE_ENDPOINT_SECRET") 

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{environ.get('POSTGRES_USER')}:{environ.get('POSTGRES_PASSWORD')}@db/{environ.get('POSTGRES_DEV_DB')}"
    


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{environ.get('POSTGRES_USER')}:{environ.get('POSTGRES_PASSWORD')}@db/{environ.get('POSTGRES_TEST_DB')}"

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
    }

