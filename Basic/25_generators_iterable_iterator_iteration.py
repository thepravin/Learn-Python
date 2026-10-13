'''
Iteration : going through items one by one (for loop does this).
Iterable  : anything you can loop over -> list, tuple, str, dict, set, range. Has __iter__().
Iterator  : object that gives the next item each time you ask. Has __iter__() and __next__().
            It remembers where it stopped and can be used only once.
Generator : an easy way to make an iterator using a function with `yield`.
'''


# ---------------- 1. Iteration ----------------
nums = [10, 20, 30]
for n in nums:          # iteration
    print(n)


# ---------------- 2. Iterable -> Iterator ----------------
it = iter(nums)         # iter() turns an iterable into an iterator
print(next(it))         # 10
print(next(it))         # 20
print(next(it))         # 30
# print(next(it))       # StopIteration - no items left

'''
What a for loop really does:
    it = iter(nums)
    while True:
        try:
            n = next(it)
        except StopIteration:
            break
        print(n)
'''


# ---------------- 3. Iterator is used only once ----------------
it = iter([1, 2, 3])
print(list(it))         # [1, 2, 3]
print(list(it))         # []  - already finished

nums = [1, 2, 3]        # an iterable can be looped again and again
print(list(nums))       # [1, 2, 3]
print(list(nums))       # [1, 2, 3]


# ---------------- 4. Custom iterator (class) ----------------
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

for n in CountUp(3):
    print(n)            # 1 2 3


# ---------------- 5. Generator (same thing, much shorter) ----------------
def count_up(limit):
    current = 0
    while current < limit:
        current += 1
        yield current   # gives a value and pauses here

for n in count_up(3):
    print(n)            # 1 2 3

g = count_up(2)
print(next(g))          # 1
print(next(g))          # 2
# print(next(g))        # StopIteration


# ---------------- 5.1 return vs yield ----------------
'''
return -> sends a value and ENDS the function.
yield  -> sends a value and PAUSES the function. Next call continues from there.
'''

# return: second return never runs, every call starts fresh
def get_num():
    return 1
    return 2

print(get_num())        # 1
print(get_num())        # 1

# yield: gives values one by one, remembers where it stopped
def get_nums():
    yield 1
    yield 2

g = get_nums()          # nothing runs yet, only a generator is created
print(next(g))          # 1
print(next(g))          # 2

# When does the code run?
def demo():
    print("start")
    yield 1
    print("end")

g = demo()              # prints nothing
print(next(g))          # start -> 1
# next(g)               # end -> StopIteration

# Same task, two ways
def squares_return(n):  # builds the whole list in memory, then returns
    result = []
    for i in range(n):
        result.append(i * i)
    return result

def squares_yield(n):   # gives one value at a time
    for i in range(n):
        yield i * i

print(squares_return(4))        # [0, 1, 4, 9]
print(list(squares_yield(4)))   # [0, 1, 4, 9]

# return inside a generator just stops it
def first_two():
    yield 1
    yield 2
    return
    yield 3             # never runs

print(list(first_two()))        # [1, 2]

'''
| return                               | yield                                    |
|--------------------------------------|------------------------------------------|
| ENDS the function                    | PAUSES the function                      |
| gives one value                      | gives many values, one at a time         |
| local variables are lost             | local variables are kept                 |
| code runs when function is called    | code runs only when next() is called     |
| stores all results in memory         | stores one value at a time               |

Use return -> when you need one result or will use the data many times.
Use yield  -> when data is big, endless, or you only need to loop once.
'''


# ---------------- 6. Generator expression ----------------
squares_list = [x * x for x in range(5)]   # list  -> all values stored in memory
squares_gen = (x * x for x in range(5))    # generator -> values made one at a time
print(squares_list)     # [0, 1, 4, 9, 16]
print(squares_gen)      # <generator object ...>
print(list(squares_gen))  # [0, 1, 4, 9, 16]


# ---------------- 7. Why use generators? Saves memory ----------------
import sys
print(sys.getsizeof([x for x in range(1_000_000)]))  # ~8 MB
print(sys.getsizeof(x for x in range(1_000_000)))    # ~200 bytes

print(sum(x for x in range(1_000_000)))  # works without building a big list


# ---------------- 8. Real-life usage: read a big file line by line ----------------
def read_lines(path):
    with open(path) as f:
        for line in f:          # file object is also an iterator
            yield line.strip()

# for line in read_lines("big_file.txt"):
#     print(line)


'''
Summary:
Iterable  -> can be looped (list, str, range).        iter(obj) gives an iterator.
Iterator  -> gives one item at a time with next().    Used only once.
Generator -> function with yield. Easiest way to make an iterator. Saves memory.
Iteration -> the act of looping through items.
'''
