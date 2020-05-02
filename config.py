import os

class Config:
    '''
    general configurations here
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cephas:admin121@localhost/pitch_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    '''
    configurations for development process
    '''
    DEBUG = True

class ProdConfig(Config):
    '''
    configs for production/deployment
    '''
    DEBUG = False

config_loader = {
    'development':DevConfig,
    'production':ProdConfig
}