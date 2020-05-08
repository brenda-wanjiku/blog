import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brendawanjiku:brenda@localhost/blog'
    SECRET_KEY = 'brenda_wanjiku'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production'  : ProdConfig
}