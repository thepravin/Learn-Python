# methods start & end with __method__ is called Dunder methods ("double underscore" methods)


# https://docs.python.org/3/reference/datamodel.html  => 3.3.8

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"+",self.img,"i")

    # operator overloading
    def __add__(self, num2): # num3 = num1 + num2
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    # def add(self, num2):  num3 = num1.add(num2)
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return Complex(newReal, newImg)
    


num1 = Complex(1,3)
num2 = Complex(2,4)

# num3 = num1.add(num2)
num3 = num1 + num2
num3.showNumber()