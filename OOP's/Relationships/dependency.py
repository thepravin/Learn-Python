'''
Dependency : the weakest "USES-A" relationship.
             One class uses another class only for a SHORT time (inside a method),
             and does NOT keep it as an attribute.

Example    : Driver drives a Car.
             The Car is passed to drive() only when needed.
             After drive() finishes, the Driver doesn't remember the Car.

UML diagram : (dashed arrow - - -> pointing to the class that is used)

+-----------------------------+                 +---------------------+
|           Driver            |                 |         Car         |
+-----------------------------+                 +---------------------+
| - name : str                |      uses       | - model : str       |
+-----------------------------+- - - - - - - - >+---------------------+
| + drive(car: Car) : None    |                 | + move() : None     |
+-----------------------------+                 +---------------------+

Read it as : Driver depends on (uses) Car.
    - - ->   dashed arrow = dependency
    Arrow points FROM the user (Driver) TO the used class (Car).
'''


class Car:
    def __init__(self, model: str) -> None:
        self.__model = model

    def move(self) -> None:
        print(f"{self.__model} is moving...")


class Driver:
    def __init__(self, name: str) -> None:
        self.__name = name          # no Car stored here

    def drive(self, car: Car) -> None:
        # DEPENDENCY : Car is used only inside this method
        print(f"{self.__name} is driving")
        car.move()


driver1 = Driver("Pravin")

car1 = Car("Fortuner")
car2 = Car("Creta")

driver1.drive(car1)     # uses car1 now
driver1.drive(car2)     # uses a different car next time

del car1                # driver1 still exists and works
driver1.drive(car2)


# ---------------- Other common forms of dependency ----------------
# 1. Creating an object inside a method and throwing it away after
class Mechanic:
    def test_drive(self) -> None:
        test_car = Car("Test-Car")      # temporary object, gone after the method ends
        test_car.move()

Mechanic().test_drive()

# 2. Calling a module / function from another class
import math

class Circle:
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    def area(self) -> float:
        return math.pi * self.__radius ** 2     # Circle depends on the math module

print(Circle(2).area())     # 12.566...


'''
Notes:
1. Driver does NOT store the Car (no self.car). It only gets the Car as a method argument.
   That short-term use is what makes it dependency.

2. Driver and Car are fully independent. Deleting one doesn't affect the other.
   The Driver just needs a Car object when drive() is called.

3. Test: "Is the other class used only inside a method and not kept?" -> Yes = dependency.

4. Dependency vs association:
   Dependency  -> used for a short time (method argument / local variable)   - - ->
   Association -> kept as an attribute, long-term link (self.students = [...]) ------>

5. Real-world examples:
   Driver   - - -> Car          (drives it)
   Customer - - -> Payment      (pays using it)
   Chef     - - -> Knife        (cuts with it)
   Order    - - -> EmailService (sends a confirmation email)

Order of strength (weakest -> strongest):
   Dependency  - - ->   uses for a moment
   Association ------   linked, no ownership
   Aggregation ◇-----   has-a, part lives on its own
   Composition ◆-----   owns, part dies with the whole
'''
