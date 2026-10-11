""" 
- self is similar to this

- syntax =>  self.attribute = something

- special method call:
    __init__() => used to initialized the attribute of object.

"""

class Dog(object):

    def __init__(self):
        pass # default constructor

    def __init__(self,breed): # "self" should be the first argument in __init__ mthod
        self.breed = breed
        

obj = Dog(breed="Lab")
print(obj.breed)


# ---------- Methods ------------------------

class Circle(object):
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi * self.radius * self.radius


c = Circle(2)
print(c.area())

# ------------- Methond types ------------------
""" 
- Instance methods have access to the instance of the class.

- Class methods have access to the class (classes are also objects in Python), but not instances. This is similar to the static methods in Java/C#

- Static methods have no access to either instances or classes. They are more like plain functions, just bounded with the class for scoping and don't take self as a argument.

- object attribute > class attribute

- @staticmethod , @classmethod ... => these are decorators, allow us to wrap another function in order to extend the dehaviour of the wrapped function without permanently modifying it

"""

class Student:
    school_name = 'GCE,Karad'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method/variable
    def show(self):
        print(self.name, self.age, Student.school_name, self.__class__.school_name)

    @property  # access this fun as a property/ instance varable
    def details(self):
        print("Name : ",self.name, "Age : ",self.age)

    @classmethod
    def change_School(cls, name):
        cls.school_name = name

    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']
    

pravin = Student('Pravin',21)
ganesh = Student('Ganesh',20)

# instance variable
print(pravin.name)
print(ganesh.name)

# class variable
print(pravin.school_name)
print(ganesh.school_name)

pravin.show()
pravin.details
