'''
instance varible in current class> instance variable in parent class > class var in current class> class var in parent class 

'''


class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car): # ---- single inheritance ----
    def __init__(self, brand,type):
        super().__init__(type)
        self.brand = brand
        super().start()

car1 = ToyotaCar("fortuner", "diesel")
car1.start()
# print(car1.type)

class Fortuner(ToyotaCar):  # ---- multi-level ----
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
# car1.start()


#---------------------------------------------
# multiple

class A:
    varA = "a"

class B:
    varB = "b"

class C(A,B):
    varC = "c"

c1 = C()
# print(c1.varC, c1.varA, c1.varB)



#  Diamond Shape Problem In Multiple Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C): # order matters : first check in B then C
    pass

D().show()  
print(D.__mro__) #  MRO (Method Resolution Order)

'''
MRO use C3 rules linearization :
child comes before its parents.
Parents keep the order you wrote them:  D(B, C)  puts  B  before  C .
Each class appears only once, so  A  comes after both  B  and  C .
'''