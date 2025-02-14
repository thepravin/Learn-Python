
# *---------- built in functions --------

# import math as m
# from math import cos # only one function need then, can't access other function


# print(m.pi)
# print(cos(30))


#*------------ User-defined function -----------

def sum(a,b):
    print(a+b)

sum(3,4)

def sum2(a,b):
    sum = a+b
    return sum

a = sum2(3,6)
print(a)


#*------------- Multiple return value ------------
def calc(a,b):
    return a+b, a*b

addition, product = calc(2,3)
print(addition,product) # 5,6


#* ---------- Function Parameters and Arguments -------------

#* 1. Positonal Argument
def greet(name,age):
    return f"{name} and age is {age}"

print(greet('Pravin',25)); #Pravin and age is 25

#* 2. Default Arguments
def defaultArg(name="Guest"):
    return f"Hello, {name}!"

print(defaultArg()) #Hello, Guest!

#* 3. Keyword Arguments
# - Arguments passed by name, allowing different order.
print(greet(age=21, name="Ganesh"))



#* ------------- Variable-Length Arguments  --------------------
#  *args → For multiple positional arguments.
# **kwargs → For multiple keyword arguments.

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10

def info(**kwargs):
    return kwargs

print(info(name="Alice", age=25))  # Output: {'name': 'Alice', 'age': 25}
