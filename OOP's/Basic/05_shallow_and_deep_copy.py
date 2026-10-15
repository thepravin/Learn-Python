'''
Shallow copy vs Deep copy

Assignment (b = a) : NO copy. Both names point to the SAME object.
Shallow copy       : makes a NEW outer object, but the inner objects are SHARED.
Deep copy          : makes a NEW outer object AND new copies of every inner object.

            a = [[1, 2], [3, 4]]

Assignment :  a ----> [ * , * ] <---- b          (same list)

Shallow    :  a ----> [ * , * ]
                        |   |
                      [1,2] [3,4]                (inner lists shared)
                        |   |
              b ----> [ * , * ]

Deep       :  a ----> [ * , * ] ---> [1,2] [3,4]
              b ----> [ * , * ] ---> [1,2] [3,4] (everything new)
'''

import copy


# ---------------- 1. Assignment is NOT a copy ----------------
a = [[1, 2], [3, 4]]
b = a
b.append([5, 6])
print("1.", a)                      # [[1, 2], [3, 4], [5, 6]] -> a changed too
print("   a is b :", a is b)        # True


# ---------------- 2. Shallow copy (built-in ways) ----------------
a = [[1, 2], [3, 4]]

s1 = a.copy()           # list method
s2 = a[:]               # slicing
s3 = list(a)            # constructor
s4 = copy.copy(a)       # copy module (works for any object)
# dict: d.copy(), dict(d)    set: st.copy(), set(st)

s4.append([5, 6])       # change OUTER list -> a is safe
s4[0].append(99)        # change INNER list -> a changes too (shared)

print("2.", a)                              # [[1, 2, 99], [3, 4]]
print("   s4 :", s4)                        # [[1, 2, 99], [3, 4], [5, 6]]
print("   a is s4       :", a is s4)        # False -> new outer list
print("   a[0] is s4[0] :", a[0] is s4[0])  # True  -> inner list shared


# ---------------- 3. Deep copy (built-in) ----------------
a = [[1, 2], [3, 4]]
d = copy.deepcopy(a)

d[0].append(99)
print("3.", a)                              # [[1, 2], [3, 4]] -> a is safe
print("   d :", d)                          # [[1, 2, 99], [3, 4]]
print("   a[0] is d[0]  :", a[0] is d[0])   # False -> inner list also new


# ---------------- 4. Manual shallow copy ----------------
def manual_shallow_copy(obj):
    if isinstance(obj, list):
        return [item for item in obj]               # new list, same items
    if isinstance(obj, dict):
        return {k: v for k, v in obj.items()}       # new dict, same values
    if isinstance(obj, set):
        return {item for item in obj}
    if hasattr(obj, "__dict__"):                    # custom class object
        new_obj = obj.__class__.__new__(obj.__class__)   # create without calling __init__
        new_obj.__dict__.update(obj.__dict__)       # same attribute values (shared)
        return new_obj
    return obj      # int, float, str, bool, None, tuple -> immutable, no need to copy


a = {"name": "Pravin", "marks": [80, 90]}
s = manual_shallow_copy(a)
s["name"] = "Ganesh"            # replace value -> a is safe
s["marks"].append(100)          # change inner list -> a changes too
print("4.", a)                  # {'name': 'Pravin', 'marks': [80, 90, 100]}


# ---------------- 5. Manual deep copy (recursive) ----------------
def manual_deep_copy(obj, memo=None):
    if memo is None:
        memo = {}                       # id(original) -> copy, stops infinite loops
    if id(obj) in memo:
        return memo[id(obj)]

    if isinstance(obj, list):
        new_list = []
        memo[id(obj)] = new_list
        for item in obj:
            new_list.append(manual_deep_copy(item, memo))   # copy every inner item too
        return new_list

    if isinstance(obj, dict):
        new_dict = {}
        memo[id(obj)] = new_dict
        for k, v in obj.items():
            new_dict[manual_deep_copy(k, memo)] = manual_deep_copy(v, memo)
        return new_dict

    if isinstance(obj, set):
        return {manual_deep_copy(item, memo) for item in obj}

    if isinstance(obj, tuple):
        return tuple(manual_deep_copy(item, memo) for item in obj)

    if hasattr(obj, "__dict__"):
        new_obj = obj.__class__.__new__(obj.__class__)
        memo[id(obj)] = new_obj
        for k, v in obj.__dict__.items():
            new_obj.__dict__[k] = manual_deep_copy(v, memo)
        return new_obj

    return obj      # immutable values can be shared safely


a = {"name": "Pravin", "marks": [80, 90]}
d = manual_deep_copy(a)
d["marks"].append(100)
print("5.", a)                  # {'name': 'Pravin', 'marks': [80, 90]} -> a is safe
print("   d :", d)              # {'name': 'Pravin', 'marks': [80, 90, 100]}

# Self-referencing list: memo prevents an infinite loop
loop = [1, 2]
loop.append(loop)               # loop contains itself
loop_copy = manual_deep_copy(loop)
print("   loop_copy[2] is loop_copy :", loop_copy[2] is loop_copy)   # True


# ---------------- 6. Copying class objects ----------------
class Address:
    def __init__(self, city: str) -> None:
        self.city = city


class Employee:
    def __init__(self, name: str, city: str, skills: list) -> None:
        self.name = name
        self.address = Address(city)    # inner object
        self.skills = skills            # inner list


emp1 = Employee("Pravin", "Pune", ["Python"])

emp2 = copy.copy(emp1)          # shallow
emp3 = copy.deepcopy(emp1)      # deep

emp2.address.city = "Mumbai"    # shared Address -> emp1 changes too
emp3.skills.append("Java")      # own list -> emp1 is safe

print("6. emp1 city   :", emp1.address.city)                 # Mumbai
print("   emp1 skills :", emp1.skills)                       # ['Python']
print("   shallow shares address :", emp1.address is emp2.address)   # True
print("   deep shares address    :", emp1.address is emp3.address)   # False

emp4 = manual_deep_copy(emp1)   # our manual version also works on objects
print("   manual deep shares address :", emp1.address is emp4.address)   # False


# ---------------- 7. Custom copy behaviour: __copy__ and __deepcopy__ ----------------
class Student:
    def __init__(self, name: str, marks: list) -> None:
        self.name = name
        self.marks = marks

    def __copy__(self):                         # called by copy.copy()
        print("   __copy__ called")
        return Student(self.name, self.marks)   # same marks list (shared)

    def __deepcopy__(self, memo):               # called by copy.deepcopy()
        print("   __deepcopy__ called")
        return Student(copy.deepcopy(self.name, memo),
                       copy.deepcopy(self.marks, memo))   # new marks list


st1 = Student("Ganesh", [70, 80])
print("7.")
st2 = copy.copy(st1)
st3 = copy.deepcopy(st1)
print("   shallow shares marks :", st1.marks is st2.marks)   # True
print("   deep shares marks    :", st1.marks is st3.marks)   # False


'''
Notes:
1. b = a       -> no copy, same object (a is b -> True).
   Shallow     -> new outer object, inner objects shared.
   Deep        -> new outer object + new inner objects (fully independent).

2. Built-in shallow copy : list.copy(), list[:], list(x), dict.copy(), dict(x),
                           set.copy(), copy.copy(x)
   Built-in deep copy    : copy.deepcopy(x)

3. Shallow copy is enough when the object holds only immutable values
   (int, float, str, bool, None, tuple of immutables).
   e.g. [1, 2, 3].copy() is safe -> numbers can't be changed in place.

4. Use deep copy when the object holds mutable things (lists, dicts, objects)
   and you want to change the copy without touching the original.

5. Manual shallow copy : make a new container and put the SAME items in it.
   Manual deep copy    : make a new container and RECURSIVELY copy every item.
   memo (dict of id -> copy) avoids copying the same object twice and stops
   infinite loops for objects that refer to themselves.

6. Classes can control copying:
   __copy__(self)            -> used by copy.copy()
   __deepcopy__(self, memo)  -> used by copy.deepcopy()

7. Deep copy is slower and uses more memory, because it copies everything.

8. Real-world uses:
   - Undo / history: save a deep copy of the state before changing it
   - Game: copy a board to test a move without changing the real board
   - Default config: deep copy a settings dict before editing it per user
   - Tests: give each test its own copy of sample data
'''

