class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner          # PUBLIC - can access anywhere
        self._balance = balance     # PROTECTED - convention: _var = "don't touch outside class/subclass"
        self.__pin = pin            # PRIVATE - name mangling: becomes _BankAccount__pin

acc = BankAccount("Pravin", 10000, 1234)
print(acc.owner)        # OK
print(acc._balance)     # Works but you SHOULDN'T - LLD reviewer will flag this
# print(acc.__pin)      # AttributeError!
print(acc._BankAccount__pin) # This works - proof it's not truly private
print("__dict__",acc.__dict__) # __dict__ : A dictionary that stores all instance attributes of an object at runtime.


# -------- 99% private -----------
class BankAccount:
    __slots__ = ('owner', '__balance', '__pin') # removes __dict__, can't add random attrs. 
    # __slots__ : fixed list of allowed attributes, saving memory and preventing accidental new attributes.

    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.__balance = balance
        self.__pin = pin

    def _validate(self, pin):
        if pin!= self.__pin:
            raise PermissionError("Invalid PIN")

    def get_balance(self, pin):
        self._validate(pin)
        return self.__balance

    def withdraw(self, amount, pin):
        self._validate(pin)
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        return self.__balance

acc = BankAccount("Aditya", 10000, 1234)
# acc.__balance -> AttributeError
# acc._BankAccount__pin -> still works technically, but you have told reviewer
# you used encapsulation + validation. No one will do that in code review.


# ---------------- Python Closure ----------------
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner

        # These are LOCAL variables, not self.__ variables
        # They live in closure, not in object __dict__
        _balance = balance
        _pin = pin

        # Define methods INSIDE __init__ so they close over _balance and _pin
        def get_balance(input_pin: int):
            if input_pin!= _pin:
                raise PermissionError("Wrong PIN")
            return _balance

        def withdraw(amount: int, input_pin: int):
            nonlocal _balance  # nonloacl -  Used inside a nested function to modify a variable from the enclosing (outer) function's scope — not global, not local.
            if input_pin!= _pin:
                raise PermissionError("Wrong PIN")
            if amount > _balance:
                raise ValueError("Insufficient funds")
            _balance -= amount
            return _balance

        def deposit(amount: int):
            nonlocal _balance
            _balance += amount
            return _balance

        # Attach them to instance
        self.get_balance = get_balance
        self.withdraw = withdraw
        self.deposit = deposit

acc = BankAccount("Aditya", 10000, 1234)

print(acc.owner) # OK
print(acc.get_balance(1234)) # 10000
acc.withdraw(2000, 1234)

print(acc.__dict__)
# {'owner': 'Aditya', 'get_balance': <function...>, 'withdraw':..., 'deposit':...}
# NO balance, NO pin anywhere!

# Try to hack:
print(acc._BankAccount__pin) # AttributeError - doesn't exist
print(acc._balance) # AttributeError - doesn't exist
# print(acc.__closure__) -> You can technically get it via function.__closure__[0].cell_contents
# but that's reverse engineering, no normal code will do it.