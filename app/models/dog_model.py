# We need access to SQLAlchemy
from app import db 

# Create class that is inherited from db.Model from SQLAlchemy
class Dog(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    breed = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String, default = "non-binary")
    caretaker_id = db.Column(db.Integer, db.ForeignKey('caretaker.id'))
    caretaker = db.relationship("Caretaker", back_populates="dogs")
    ## db.relationship isa fx that adds on a attr to our dog model and returns the caretaker instance for that dog
    ## back_populates="dogs" attr will be associated with caretaker

    ## helper fx
    def to_dict(self):
        # this will build out the individual dog dict for us
        # Audrey recommends this since it's cleaner
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "gender": self.gender,
        }