
""" 
- self is similar to this

- syntax =>  self.attribute = something

- special method call:
    __init__() => used to initialized the attribute of object.

"""

class Dog(object):
    def __init__(self,breed): # "self" should be the first argument in __init__ mthod
        self.breed = breed
        

obj = Dog(breed="Lab")
print(obj.breed)