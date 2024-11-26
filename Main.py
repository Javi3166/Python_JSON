import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

print("\nIt is possible to convert a dict to a json file which is known as serialization or encoding.")

# .dumpS is for a string, it will be regular .dump if for a file
personJSON = json.dumps(person, indent=4, sort_keys=True) # It is possible to change the separators, but it's preferred to use the defaults
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

print("\nIt is possible to convert a json file to a dict which is known as deserialization or decoding.")
person = json.loads(personJSON)
print(person)

with open('person.json', 'r') as file:
    json.load(file)
    print(person)

print("\nIt is also possible to convert custom classes to json using several methods.")

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

print("\nThe first method is using a custom encoder.")
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable.')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

print("\nThe second method is making a class of the JSON encoder.")
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

print("\nIt is also possible to use a different format for calling the encoder.")
userJSON = UserEncoder().encode(user)
print(userJSON)

print("\nIt is possible to decode the JSON file back to a dictionary or user class.")

print("\nUsing json.loads() just converts the json file to a dictionary.")
user = json.loads(userJSON)
print(user)

print("\nIn order to decode it json file to a user class, a custom decoder will be needed.")
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)