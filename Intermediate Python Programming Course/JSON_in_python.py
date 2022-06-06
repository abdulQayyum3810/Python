#JSON (JavaScript Object Notation) is a lite weight data format, it is used for data exchanging mostly in web applications
import json

#python to JSON (serialization,Encoding)
person={"name":"Jane","age":30,"city":"New York","hasChilderen":False,"titles":["Engineer","Programmer"]}
personJSON=json.dumps(person,indent=4,sort_keys=True)
print(personJSON)
with open("person.json","w") as file:
    json.dump(person,file,indent=4)

#JSON to python (Deserialization,Decoding)
person2=json.loads(personJSON)
print(person2)

with open("example.json","r") as file:
    exampleJSON=json.load(file)
print(exampleJSON)

#Encoding of customized objects
class User:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
def encode_user(o):
    if isinstance(o,User):
        return {"name":o.name,"age":o.age,o.__class__.__name__:True}
    else:
        raise TypeError("Serialization is not supported for")
user1=User("Max",29)
userJSON=json.dumps(user1,default=encode_user)
print(userJSON)

#Alternative for encoding of customized objects
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,User):
            return {"name":o.name,"age":o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
userJSON2=json.dumps(user1,cls=UserEncoder)
print(userJSON2)

#Decoding JSON to customized objects
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"],age=dct["age"])
    return dct
user2=json.loads(userJSON,object_hook=decode_user)
print(user2)