from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    #Creating app configurations
    app.config.from_object(config_options[config_name])
   

    #Registers the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Initializing flask extensions
    db.init_app(app)


    return app