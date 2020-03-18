#http://jsonpickle.github.io/
import jsonpickle

class Cat:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return "Hi I am " + self.name + " born as " + self.breed +". I am " + self.age + " years old."


#Pickle Cat into JSON
conney = Cat('conney','buremse shorthair','5')

with open('frozencat.json','w')as file:
    frozen = jsonpickle.encode(conney)
    file.write(frozen)


# #Unpickle cat from JSON
# with open('frozencat.json','r')as file:
#     contents = file.read()
#     unfrozen = jsonpickle.decode(contents)
#     print(unfrozen)
