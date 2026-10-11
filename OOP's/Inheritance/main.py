
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
print(car1.type)

class Fortuner(ToyotaCar):  # ---- multi-level ----
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()


#---------------------------------------------
# multiple

class A:
    varA = "a"

class B:
    varB = "b"

class C(A,B):
    varC = "c"

c1 = C()
print(c1.varC, c1.varA, c1.varB)