from flask import jsonify, abort, make_response

def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))

def get_record_by_id(cls, id): #cls is a param that will eventually represent the class instance
    # cls is not an OOP param, it's literally just a name tha represents what we pass in
    try:
        id = int(id)
    except ValueError:
        error_message(f"Invalid id {id}", 400)
        
    # check if id exists in db
    model = cls.query.get(id)
            # cls is a variable that can represent dogs or caretakers
            # We can pass classes into fxs as instances
    # get() will either return the object it self (truthy) or None (falsy)
    if model:  
        return model
    
    error_message(f"No model of type Dog with id {id} found")
    '''Refer back to lecture recording for this part to edit'''