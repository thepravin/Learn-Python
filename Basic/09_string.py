
# support -ve indexing (reverse indexing)

fruit = "Apple"

print(fruit[0]) # A
print(fruit[-1]) # e


#*--------------- slice -> string not change ----------
""" 
s[start : end] ==> start-> include , end->exclude
if start not given bydefault '0'
if end not given bydefault 'size'

"""

print(fruit[1:4])
print(fruit[1:5])
print(fruit[-3:-1]) # pl

#*-------------------------------------

""" 
s[start : end : steps]
if steps not give bydefault '1'
"""
print(fruit[0:5:2])

#*------------- reverse str ----------
print(fruit[::-1])


a = 'abc'
b = 'def'
print(a+b);

print(a*2) # repeat a two times