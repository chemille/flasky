from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.dog_model import Dog

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs') # this blueprint allows us to use the endpoint '/dogs'

@dogs_bp.route("", methods=["POST"])
def create_dog():
    request_body = request.get_json()
    
    if "name" not in request_body or "breed" not in request_body:
        return make_response("Invalid Request, Name * Breed Cant Be Empty", 400)
    
    new_dog = Dog(
        name = request_body['name'],
        breed = request_body['breed'],
        age = request_body['age'],
        gender = request_body['gender']
    )
    
    db.session.add(new_dog)
    db.session.commit()
    
    return make_response(f"Dog {new_dog.name} has been successfully created!", 201)
        
@dogs_bp.route("", methods=["GET"])
def get_all_dogs():
    dogs = Dog.query.all()
    dogs_response = []
    for dog in dogs:
        dogs_response.append({
            "name": dog.name,
            "breed": dog.breed,
            "age": dog.age,
            "gender": dog.gender
        }) 
        return jsonify(dogs_response)

# # Hardcode data about dogs using blueprint
# class Dog:
#     def __init__(self, id, name, breed, age, gender):
#         self.id = id
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.gender = gender

# # create list of dog instances (our mini database)    
# DOGS = [
#     Dog(1, 'John Cena', "pug", 34, "Male"),
#     Dog(2, 'Snoop', "hair doberman", 14, "Female"),
#     Dog(3, "Doug 'the Doctor', M.D.", "pompom", 10, "Male")  
# ]

# # now we need to provide a way to allow clients to access this list


# @dogs_bp.route("", methods=['GET']) # decorators extend the functionality of a fx. Always above of fx.
# def get_all_dogs(): 
#     dog_response = [vars(dog) for dog in DOGS] # list comprehension
#     return jsonify(dog_response) 
#     # ^ Refactored ^
    
# def get_all_dogs(): 
    # dog_response = [] # to display each instance of dog in dict form
    # for dog in DOGS:
    #     print(vars(dog))
    #     dog_response.append(vars(dog)) # vars returns instances as dicts (returns dict attributes of objects)
        # dog_response.append({
        #     "id": dog.id,
        #     "name": dog.name,
        #     "age": dog.age,
        #     "breed": dog.breed,
        #     "gender": dog.gender
        # })
    
    # print(DOGS)
    # print(dog_response)    
    # print(dog_response)
    # print(type(jsonify(dog_response)))    
    # return jsonify(dog_response) # jsonify turns any non-dict data type into JSON format #
    
# ''' GET ONE DOG? HOW?'''
# @dogs_bp.route('/<id>', methods=["GET"]) # use blueprint to create our route and define endpoint 
# def get_one_dog(id): # every time/dog/<id> is requested, we're going to take in the id from the url
#     # return dog as a dict    
#     dog = validate_dog(id) # call helper fx
#     return dog

# # Validation fx - helper fx
# def validate_dog(id):
#     # handle if id is not found
#     try:
#         dog_id = int(id)
#     except ValueError: # if the dog id is not an int, return this message
#         return {
#             "message": "Invalid dog id"
#         }, 400
        
#     # handle invalid data types such as non-ints
#     for dog in DOGS:
#         if dog.id == dog_id: # type casting id coming in from url into an integer type
#             return vars(dog)
        
#     abort(make_response(jsonify(description="Resource not found"), 404)) # this creates a json object for us that looks like a dict



# Notes from roundtable lecture:
# Refer to Flask documentation, ctrl + F "jsonify"
    # jsonify turns any data type like a str or list into JSON response that looks like dict form. 
    # Underneath the hood, Flask turns any dict automatically into JSON. Anything else like strs and lists,
    # we do need to use jsonify to turn into dict form. So if it's a str or list, wrap jsonify around it.
# Flask doc, ctrl + F "abort" and "make_response"
    # make sure you're in the correct version of the doc
    # abort can be used to return an error message
    # make_response calls the Response class. By default, make_response returns a text html; however,
    # we're using it for an api so we just want it to return json