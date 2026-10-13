'''
Realization : a class IMPLEMENTS an interface (a "contract").
              The interface only says WHAT methods must exist.
              The class decides HOW those methods work.

Interface in Python : Python has no "interface" keyword.
                      We use an abstract class (ABC) with only @abstractmethod methods.

Example     : Payment is the interface -> every payment must have pay().
              UPIPayment and CardPayment realize (implement) it in their own way.

UML diagram : (dashed line with an EMPTY triangle pointing to the interface)

                  +---------------------------+
                  |       <<interface>>       |
                  |          Payment          |
                  +---------------------------+
                  | + pay(amount: float):None |
                  +---------------------------+
                         △             △
                         :             :
                         :             :
        +---------------------------+  +---------------------------+
        |        UPIPayment         |  |        CardPayment        |
        +---------------------------+  +---------------------------+
        | - upi_id : str            |  | - card_no : str           |
        +---------------------------+  +---------------------------+
        | + pay(amount: float):None |  | + pay(amount: float):None |
        +---------------------------+  +---------------------------+

Read it as : UPIPayment and CardPayment realize (implement) Payment.
    <<interface>>   marks the class as an interface
    : (dashed) + △  realization  (class implements interface)
    | (solid)  + △  generalization / inheritance (normal parent -> child)
'''

from abc import ABC, abstractmethod


# Interface : only method names, no real code
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# REALIZATION : these classes implement the Payment interface
class UPIPayment(Payment):
    def __init__(self, upi_id: str) -> None:
        self.__upi_id = upi_id

    def pay(self, amount: float) -> None:
        print(f"Paid Rs.{amount} using UPI ({self.__upi_id})")


class CardPayment(Payment):
    def __init__(self, card_no: str) -> None:
        self.__card_no = card_no

    def pay(self, amount: float) -> None:
        print(f"Paid Rs.{amount} using Card (**** {self.__card_no[-4:]})")


# Works with ANY class that realizes Payment
def checkout(payment: Payment, amount: float) -> None:
    payment.pay(amount)


checkout(UPIPayment("pravin@upi"), 500)
checkout(CardPayment("1234567812345678"), 1200)


# Interface itself cannot be created
# Payment()     # TypeError: Can't instantiate abstract class Payment


# If a class forgets to implement pay(), it cannot be created either
class CashPayment(Payment):
    pass

# CashPayment()  # TypeError: Can't instantiate abstract class CashPayment ... 'pay'


'''
Notes:
1. Interface = list of methods that MUST exist (a contract). No real code inside.
   In Python: class Payment(ABC) + @abstractmethod.

2. A class that implements ALL abstract methods "realizes" the interface.
   If even one method is missing, Python gives TypeError when creating the object.

3. checkout() doesn't care which payment it gets.
   Any class that realizes Payment works -> easy to add new types (WalletPayment, NetBanking)
   without changing checkout().

4. Realization vs inheritance (generalization):
   Inheritance -> child gets REAL code from parent (reuse)       solid line   + △
   Realization -> class only promises to have the methods (rule)  dashed line  + △
   In Python both are written the same way: class UPIPayment(Payment)
   The difference is in the parent: an interface has only abstract methods.

5. Test: "Does the class just follow a contract (must have these methods)?" -> Yes = realization.

6. Real-world examples:
   Payment       <- UPIPayment, CardPayment
   Shape         <- Circle, Square        (must have area())
   Notification  <- EmailNotification, SMSNotification   (must have send())
   Database      <- MySQLDatabase, MongoDatabase         (must have connect())
'''
