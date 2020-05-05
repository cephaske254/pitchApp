import os

class Config:
    '''
    general configurations here
    '''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/images/profile'
    
    # SIMPLE MDE CONFIGURATIONS
    SIMPLEMDE_JS_IIFE =True
    SIMPLEMDE_USE_CDN =True

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    '''
    configurations for development process
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cephas:admin121@localhost/pitch_app'

class ProdConfig(Config):
    '''
    configs for production/deployment
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_RED_URL")

config_loader = {
    'development':DevConfig,
    'production':ProdConfig
}