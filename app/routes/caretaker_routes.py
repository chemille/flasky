from app import db
from app.models.caretaker import Caretaker
from app.models.dog_model import Dog
from flask import Blueprint, jsonify, make_response, request

## you could name it all bp, but this is more explicit and descriptive
## you want to observe what your team is doing in terms of naming conventions
caretaker_bp = Blueprint("caretaker_bp", __name__, url_prefix="/caretakers")

@caretaker_bp.route("", methods=["POST"])
def create_caretaker():
    request_body = request.get_json() # we get json from the reqeust body of the post request to the endpoint/caretakers 
    new_caretaker = Caretaker(name=request_body["name"]) # create new instance of caretaker which only takes in name

    db.session.add(new_caretaker) # adds new instance to caretaker table in our db
    db.session.commit()

    return make_response(jsonify(f"Caretaker {new_caretaker.name} successfully created"), 201)

@caretaker_bp.route("", methods=["GET"])
def read_all_caretaker():
    caretakers = Caretaker.query.all() # query all records of our caretaker

    caretaker_response = []
    for caretaker in caretakers:
        caretaker_response.append(
            {
                "id": caretaker.id,
                "name": caretaker.name
            }
        )
    return jsonify(caretaker_response)

# NESTED ROUTES
@caretaker_bp.route("/<id>/dogs", methods=["POST"])
def create_dog(id):
    caretaker = Caretaker.query.get(id)

    request_body = request.get_json()
    new_dog = Dog(
        name=request_body["name"],
        age=request_body["age"],
        gender=request_body["gender"],
        breed=request_body["breed"],
        caretaker=caretaker)

    db.session.add(new_dog)
    db.session.commit()

    return make_response(jsonify(f"Dog {new_dog.name} cared by {caretaker.name} successfully created"), 201)

@caretaker_bp.route("/<id>/dogs", methods=["GET"]) # Here we provide a caretaker id in <id>
def read_dogs_of_caretaker(id):
    caretaker = Caretaker.query.get(id)

    # print(caretaker.dogs)

    # dog_response = []
    # for dog in caretaker.dogs:
    #     dog_response.append(dog.to_dict()) #or dictionary literal

    dog_response = [dog.to_dict() for dog in caretaker.dogs] # list comprehension
    # We use .to_dict() which is an instance method of Dog 

    return(jsonify(dog_response))