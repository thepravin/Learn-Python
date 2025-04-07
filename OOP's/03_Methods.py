



class Circle(object):
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi * self.radius * self.radius


c = Circle(2)
print(c.area())