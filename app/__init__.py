## Remember our __init__.py file is the spine that connects our project together

from flask import Flask
# Translator from Flask to SQL
from flask_sqlalchemy import SQLAlchemy
# Migrator tool that keeps track of changes to our table (versioning control)
from flask_migrate import Migrate
# dotenv allows us to read env variables
from dotenv import load_dotenv
# os is a package that provides a portable way of reading hidden files such as dotenv files
import os
load_dotenv() # important to invoke this for it to work

# DB representation
db = SQLAlchemy()
# Migration representations
migrate = Migrate()
    
def create_app(test_config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    
    # Connects flask to the db and tells flask where to find our db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")
    
    # Connects db to migrate to our flask app
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models.dog_model import Dog
    from app.models.caretaker import Caretaker
    
    from .routes.dogs import dogs_bp
    app.register_blueprint(dogs_bp)
    
    from .routes.caretaker_routes import caretaker_bp
    app.register_blueprint(caretaker_bp)

    return app