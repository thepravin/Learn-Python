""" 
- Instance methods have access to the instance of the class.

- Class methods have access to the class (classes are also objects in Python), but not instances. This is similar to the static methods in Java/C#

- Static methods have no access to either instances or classes. They are more like plain functions, just bounded with the class for scoping

"""

class Student:
    # class variables
    school_name = 'GCE,Karad'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method/variable
    def show(self):
        print(self.name, self.age, Student.school_name)

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

