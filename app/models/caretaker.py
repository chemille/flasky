from app import db

# Create class that is inherited from db.Model from SQLAlchemy
class Caretaker(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    dogs = db.relationship("Dog", back_populates="caretaker")
    ## db.relationship is only a relationship attr
