'''
==  -> checks VALUE    : do both objects have the same data?
is  -> checks IDENTITY : are both names pointing to the SAME object in memory?

a is b  is the same as  id(a) == id(b)
'''


# ---------------- 1. Basic difference ----------------
a = [1, 2, 3]
b = [1, 2, 3]       # new list with same values
c = a               # c points to the same list as a

print(a == b)       # True  - same values
print(a is b)       # False - two different lists in memory
print(a is c)       # True  - same list
print(id(a), id(b), id(c))   # id(a) == id(c), id(b) is different


# ---------------- 2. Why it matters: changing one changes the other ----------------
c.append(4)
print(a)            # [1, 2, 3, 4]  - a also changed, because a and c are the same object
print(b)            # [1, 2, 3]     - b is separate


# ---------------- 3. Copy makes a new object ----------------
d = a.copy()
print(d == a)       # True  - same values
print(d is a)       # False - new object


# ---------------- 4. Use `is` for None, True, False ----------------
# There is only ONE None object in Python, so `is` is the correct check.
x = None
print(x is None)        # True   (recommended)
print(x is not None)    # False
# x == None             # works, but not recommended (a class can change how == behaves)


# ---------------- 5. Small number caching (tricky!) ----------------
# Python keeps one shared object for small integers -5 to 256.
p = int("100")
q = int("100")
print(p == q, p is q)   # True True   - same cached object

p = int("1000")
q = int("1000")
print(p == q, p is q)   # True False  - two separate objects

# int("...") is used so Python creates the numbers at runtime.
# If you write p = 1000; q = 1000 in a file, Python may reuse one object and `is` gives True.
# That's why `is` must NEVER be used to compare numbers or strings.


# ---------------- 6. Strings (also tricky) ----------------
s1 = "hello"
s2 = "hello"
print(s1 == s2, s1 is s2)   # True True   - Python reuses simple strings (called "interning")

s3 = "".join(["hel", "lo"]) # built at runtime
print(s1 == s3, s1 is s3)   # True False  - same text, different object


# ---------------- 7. Custom class: == can be defined, `is` cannot ----------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):            # decides what == means for this class
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)     # True  - __eq__ compares x and y
print(p1 is p2)     # False - two different objects

# Without __eq__, == falls back to `is` (same object only).


# ---------------- 8. Real-world usage ----------------
def find_user(user_id):
    users = {1: "Pravin"}
    return users.get(user_id)       # returns None if not found

user = find_user(5)
if user is None:                    # correct way to check "not found"
    print("User not found")

# Why not `if not user:` ? -> it also treats "", 0, [] as "not found".
count = 0
print(not count)        # True  - 0 is treated as False
print(count is None)    # False - 0 is a real value, not missing


'''
Notes:
| ==                                  | is                                    |
|-------------------------------------|---------------------------------------|
| compares VALUES                     | compares IDENTITY (same memory object)|
| can be customized with __eq__       | cannot be customized                  |
| use for numbers, strings, lists...  | use for None, True, False             |
| a == b -> True if data is same      | a is b -> True if id(a) == id(b)      |

Rules:
1. Use == to compare values (almost always).
2. Use `is` only for None (and sometimes True/False or checking the exact same object).
3. Never use `is` for numbers or strings. Results depend on Python's internal caching.
4. Opposites: != (not equal value) and `is not` (not the same object).
5. If a is b is True, then a == b is usually True too. The reverse is not always true.
'''
