
# global : Points to a variable at the module level (the top of the file). IF not present then create new variable

def fun1():
    x = 20
    def fun2():
        global x # global level x is not present so, create it with 100
        x = 100

    print("Before calling fun2() : ", x) # use fun1 scope
    fun2()
    print("After calling fun2() : ",x) # use fun1 scope


fun1();
print(x);
''' Output :
Before calling fun2() :  20
After calling fun2() :  20
100

'''

# nonlocal : Points to a variable in the enclosing function (one function nested inside another).

def fun3():
    y = 200
    def fun4():
        nonlocal y 
        y = 1000

    print("Before calling fun2() : ", y) 
    fun4()
    print("After calling fun2() : ",y) 


fun3(); 
'''
Before calling fun2() :  200
After calling fun2() :  1000
'''
# print(y); Error : NameError: name 'y' is not defined

# Mutable objects don't need  nonlocal  because you modify the object without reassigning the name:
def collector():
    items = []
    def add(x):
        items.append(x)   # no reassignment, so no nonlocal needed
        return items
    return add

c = collector()
print(c(11))
print(c(12))
print(c(13))



# globals()  and  locals()  built-in functions. These return list of the variables currently in scope.

x = 10
def f():
    y = 20
    print(locals())   # {'y': 20}
f()
print(globals())  
print(globals()['x'])  # 10


# Closure : An inner function remembers variables from its enclosing function, even after the outer function has finished. This is where  nonlocal  is most useful.
'''
Three conditions for a closure : 
There is a nested function (a function inside a function).
The inner function uses a variable from the outer function.
The outer function returns the inner function (or passes it somewhere else).
If any of these is missing, it's just a nested function, not a closure.
'''
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = counter()
print(c(), c())  # 1 2