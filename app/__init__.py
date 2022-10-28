from flask import Flask
# Translator from Flask to SQL
from flask_sqlalchemy import SQLAlchemy
# Migrator tool that keeps track of changes to our table (versioning control)
from flask_migrate import Migrate

# DB representation
db = SQLAlchemy()
# Migration representations
migrate = Migrate()
    
def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    
    # Creating our db through our instance of SQLAlchemy
    # Create instances of imports
    # Give us access to the db operations
    
    #where I am listenign for my db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # connects flask to the db and tells flask where to find our db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'
    
    # connects db to migrate to our flask app
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models.dog_model import Dog
    
    from .routes.dogs import dogs_bp
    app.register_blueprint(dogs_bp)

    return app