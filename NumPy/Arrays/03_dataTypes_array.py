
# data Types in python : string, float, boolean, complex, integer

""" 
* datay types in NumPy :

- i for integer
- b for boolean
- u for unsigned integer
- f for float
- c for complex float
- m for timedelta
- M for datetime
- O for object
- S for string
- U for unicode string
- V for memory

* checking  the data type in numPy array => -dtype

"""

import numpy as np

x = np.array([1,2,3,4,5])
print(x.dtype)

y = np.array(['apple','mango'])
print(y.dtype)


#* creating array with defined data type : 
x = np.array([1,2,3,4,5],dtype='S')
print(x)
print(x.dtype)

#* create array with data type of 4 byte int :
x = np.array([1,2,3,4,5], dtype='i4')
print(x)
print(x.dtype)


# Converting data type in existing array - astype()
x = np.array([1.1,1.2,5.2,6.9])
x2 = x.astype('i') # x.astype(int)
print(x2)
print(x2.dtype)

# Converting data type integer to boolean
x = np.array([1,0,3])
x2 = x.astype(bool) 
print(x2)
print(x2.dtype)