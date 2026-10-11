
# Tuples used to create immutable sequences of values

""" 
s = 'pravin'
s[0] = 'n' # error """


a = ['p','r','a'] # list

a = ('p','r','a') # tuple
# tuples are immutable (not chage)
# a[2] = 'n' # error

#* all methods, functions, slicing are same

# if we not added comma in single value tuple then python assume it orignal data-type
b = (1)
print(type(b))

b=(1,)
print(type(b))

b=('p')
print(type(b))

b=('p',)
print(type(b))