'''
Comprehension : a short, one-line way to build a list, dict, set or generator from another iterable.

Syntax : [expression for item in iterable if condition]
          expression -> what to put in the result
          item       -> each value from the iterable
          condition  -> (optional) keep only items that pass
'''


# ---------------- 1. List comprehension ----------------
# Normal loop
squares = []
for x in range(5):
    squares.append(x * x)
print(squares)                          # [0, 1, 4, 9, 16]

# Same thing with comprehension
squares = [x * x for x in range(5)]
print(squares)                          # [0, 1, 4, 9, 16]

names = ["pravin", "aditya", "rahul"]
print([n.upper() for n in names])       # ['PRAVIN', 'ADITYA', 'RAHUL']
print([len(n) for n in names])          # [6, 6, 5]


# ---------------- 2. With condition (filter) ----------------
evens = [x for x in range(10) if x % 2 == 0]
print(evens)                            # [0, 2, 4, 6, 8]

long_names = [n for n in names if len(n) > 5]
print(long_names)                       # ['pravin', 'aditya']


# ---------------- 3. With if-else (change value) ----------------
# if-else goes BEFORE for, plain if goes AFTER for
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)                           # ['even', 'odd', 'even', 'odd', 'even']

marks = [35, 80, 20, 60]
result = ["pass" if m >= 40 else "fail" for m in marks]
print(result)                           # ['fail', 'pass', 'fail', 'pass']


# ---------------- 4. Nested loops ----------------
pairs = [(a, b) for a in [1, 2] for b in ["x", "y"]]
print(pairs)                            # [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')]

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [num for row in matrix for num in row]
print(flat)                             # [1, 2, 3, 4, 5, 6]

# Build a 2D list
table = [[r * c for c in range(1, 4)] for r in range(1, 4)]
print(table)                            # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# ---------------- 5. Dict comprehension ----------------
# Syntax : {key: value for item in iterable}
square_dict = {x: x * x for x in range(4)}
print(square_dict)                      # {0: 0, 1: 1, 2: 4, 3: 9}

name_len = {n: len(n) for n in names}
print(name_len)                         # {'pravin': 6, 'aditya': 6, 'rahul': 5}

prices = {"apple": 100, "banana": 40, "mango": 150}
costly = {k: v for k, v in prices.items() if v > 50}
print(costly)                           # {'apple': 100, 'mango': 150}

swapped = {v: k for k, v in prices.items()}
print(swapped)                          # {100: 'apple', 40: 'banana', 150: 'mango'}

keys = ["a", "b", "c"]
values = [1, 2, 3]
print({k: v for k, v in zip(keys, values)})  # {'a': 1, 'b': 2, 'c': 3}


# ---------------- 6. Set comprehension ----------------
# Syntax : {expression for item in iterable}  -> removes duplicates
nums = [1, 2, 2, 3, 3, 3]
print({x * 10 for x in nums})           # {10, 20, 30}

words = ["Hi", "hi", "HI", "Hello"]
print({w.lower() for w in words})       # {'hi', 'hello'}


# ---------------- 7. Generator expression ----------------
# Syntax : (expression for item in iterable)  -> values made one at a time, saves memory
gen = (x * x for x in range(5))
print(gen)                              # <generator object ...>
print(list(gen))                        # [0, 1, 4, 9, 16]

print(sum(x * x for x in range(5)))     # 30  - no extra brackets needed inside a function

# There is NO tuple comprehension. Use tuple() with a generator.
print(tuple(x for x in range(3)))       # (0, 1, 2)


# ---------------- 8. Real-life usage ----------------
# Clean user input
raw = ["  pravin ", "ADITYA", " Rahul  "]
clean = [s.strip().title() for s in raw]
print(clean)                            # ['Pravin', 'Aditya', 'Rahul']

# Pick data from a list of dicts
users = [
    {"name": "Pravin", "age": 25},
    {"name": "Aditya", "age": 17},
    {"name": "Rahul", "age": 30},
]
adults = [u["name"] for u in users if u["age"] >= 18]
print(adults)                           # ['Pravin', 'Rahul']

# Count each character
text = "banana"
print({ch: text.count(ch) for ch in set(text)})  # {'b': 1, 'a': 3, 'n': 2} (order may vary)


# ---------------- 9. When NOT to use ----------------
# Too complex -> hard to read. Use a normal loop instead.
# bad = [x * y for x in range(5) if x > 1 for y in range(5) if y % 2 == 0 if x != y]

# Only for side effects (like print) -> use a normal loop.
# [print(x) for x in range(3)]   # works, but creates a useless list [None, None, None]


'''
Summary:
List      -> [x for x in data]         ordered, allows duplicates
Dict      -> {k: v for k, v in data}   key-value pairs
Set       -> {x for x in data}         unique values
Generator -> (x for x in data)         one at a time, saves memory

Filter    -> [x for x in data if cond]
If-else   -> [a if cond else b for x in data]

Use comprehensions for SHORT and SIMPLE transformations.
For complex logic, a normal for loop is easier to read.
'''
