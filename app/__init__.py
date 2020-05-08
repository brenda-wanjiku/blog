from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
   

    #Registers the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Initializing flask extensions
    db.init_app(app)


    return app