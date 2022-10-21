from flask import Blueprint, jsonify

# For today, hardcode data about dogs using blueprint
class Dog:
    def __init__(self, id, name, breed, age, gender):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender

# create list of dog instances (our database)    
DOGS = [
    Dog(1, 'John Cena', "pug", 34, "Male"),
    Dog(2, 'Snoop', "hair doberman", 14, "Female"),
    Dog(3, "Doug 'the Doctor', M.D.", "pomeranian", 10, "Male")  
]

# now we need to provide a way to allow clients to access this list

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs') # this blueprint allows us to use the endpoint '/dogs'

@dogs_bp.route("", methods=['GET']) # decorators extend the functionality of fx. Always above of fx.
def get_all_dogs(): 
    dog_response = [] # to display each instance of dog in dict form
    for dog in DOGS:
        dog_response.append({
            "id": dog.id,
            "name": dog.name,
            "age": dog.age,
            "breed": dog.breed,
            "gender": dog.gender
        })
    # print(dog_response)
    # print(type(jsonify(dog_response)))    
    return jsonify(dog_response) # jsonify turns any non-dict data type into JSON format
