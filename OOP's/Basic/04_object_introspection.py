# Introspection means examining an object while the program is running: its type, attributes, methods, parents, and so on. Python makes this easy because everything (numbers, functions, classes, modules) is an object.

import inspect


class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    species = "canine"          # class variable

    def __init__(self, name):
        self.name = name        # instance variable

    def bark(self):
        return "Woof"

d = Dog("Rex")


# ---------------- 1. What type is it? ----------------
print(type(d))                  # <class '__main__.Dog'>
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True  - also checks parent classes
print(issubclass(Dog, Animal))  # True
print(d.__class__)              # same as type(d)
print(id(d))                    # unique number for this object


# ---------------- 2. What does it have? ----------------
print(dir(d))                   # all names: own + class + parent + built-in
print(vars(d))                  # {'name': 'Rex'}  - only instance variables
print(d.__dict__)               # same as vars(d)


# ---------------- 3. Work with attributes using their name as a string ----------------
print(hasattr(d, "name"))       # True
print(getattr(d, "name"))       # Rex
print(getattr(d, "age", 0))     # 0  - default value if not found
setattr(d, "age", 3)            # same as d.age = 3
print(d.age)                    # 3
delattr(d, "age")               # same as del d.age

action = "bark"                 # method name decided at runtime
print(getattr(d, action)())     # Woof


# ---------------- 4. Can it be called? ----------------
print(callable(d.bark))         # True  - it's a method
print(callable(d.name))         # False - it's a string
print(callable(Dog))            # True  - classes can be called to make objects


# ---------------- 5. Class family ----------------
print(Dog.__bases__)            # (Animal,)  - direct parents only
print(Dog.__mro__)              # (Dog, Animal, object)  - search order
print(Dog.__name__)             # Dog


# ---------------- 6. inspect module - for deeper details ----------------
print(inspect.signature(Dog.__init__))  # (self, name)
print(inspect.ismethod(d.bark))         # True
print(inspect.isclass(Dog))             # True
print(inspect.getmembers(d))            # list of (name, value) pairs


# ---------------- 7. help() - shows documentation ----------------
# help(Dog)
