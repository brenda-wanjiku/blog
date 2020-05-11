import os


class Config:
    SECRET_KEY = 'brenda_wanjiku'
    #email configs
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brendawanjiku:brenda@localhost/blog'
    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production'  : ProdConfig
}