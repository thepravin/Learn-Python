
class Student:
    def __init__(self, name):
        self.name= name


s1 = Student("Pravin")
print(s1.name)

del s1
print(s1.name) #NameError: name 's1' is not defined