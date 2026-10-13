'''
Composition : a strong "HAS-A" / "OWNS" relationship.
              The whole CREATES its parts inside itself.
              The parts cannot live without the whole.

Example     : Car has an Engine.
              The Engine is created inside the Car constructor.
              If the Car is deleted, its Engine is deleted too.

UML diagram : (filled diamond ◆ on the owner/whole side)

+----------------------------------+                 +--------------------------+
|               Car                |                 |          Engine          |
+----------------------------------+ 1             1 +--------------------------+
| - brand : str                    |◆----------------| - engine_type : str      |
| - model : str                    |                 | - horsepower : int       |
| - engine : Engine                |                 +--------------------------+
+----------------------------------+                 | + get_details() : str    |
| + get_car_details() : None       |                 | + start() : None         |
| + start_car() : None             |                 +--------------------------+
+----------------------------------+

Read it as : one Car owns exactly one Engine.
    ◆   filled diamond = composition (sits on the Car side)
    1   exactly one
'''

from typing import Optional

class Engine:
    def __init__(self, engine_type, horsepower)->None:
        self.__engine_type = engine_type
        self.__horsepower = horsepower

    def get_details(self)->str:
        return f"{self.__engine_type} Engine ({self.__horsepower} HP)"

    def start(self)->None:
        print(f"{self.__engine_type} engine started...")


class Car:
    def __init__(self, brand, model, engine_type, horsepower)->None:
        self.__brand = brand
        self.__model = model

        # COMPOSITION : Engine is created inside Car constructor
        self.__engine = Engine(engine_type, horsepower)

    def get_car_details(self)->None:
        print(f"\nCar: {self.__brand} {self.__model}")
        print(f"Engine: {self.__engine.get_details()}")

    def start_car(self)->None:
        print(f"\nStarting {self.__brand}{self.__model}...")
        self.__engine.start()
        print("Car is reay to drive!")


my_car = Car("Toyota", "Fortuner", "Diesel", 204)

my_car.get_car_details()

my_car.start_car()


'''
Notes:
1. Engine is created INSIDE Car.__init__ -> Car creates and owns it.
   Outside code never creates the Engine and never sees it directly (self.__engine is private).

2. del my_car -> the Engine goes away with the Car, because nothing else refers to it.

3. One Engine belongs to only ONE Car. It is not shared.

4. Test: "Does the whole create the part, and does the part die with the whole?" -> Yes = composition.

5. Composition vs aggregation:
   Aggregation -> part is created OUTSIDE and passed in, lives on after the whole is deleted
                  (Department ◇- Student)
   Composition -> part is created INSIDE, dies with the whole
                  (Car ◆- Engine)

6. Real-world examples:
   Car    ◆- Engine
   House  ◆- Rooms
   Human  ◆- Heart
   Order  ◆- OrderItems
'''
