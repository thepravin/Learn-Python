#  hiding the implementation details of class and only showing the essential features to user.
'''
abc : 
The main goal of the abstract base class is to provide a standardized way to test whether an object adheres to a given specification. It can also prevent any attempt to instantiate a subclass that doesn't override a particular method in the superclass. And finally, using an abstract class, a class can derive identity from another class without any object inheritance.
'''

from abc import ABC, abstractmethod

class PaymentMethod(ABC): # Abstract class - cannot be instantiated
    @abstractmethod
    def pay(self, amount: float):
        pass

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} via UPI")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} via Credit Card")

# PaymentMethod() # Error
UPI().pay(500)
