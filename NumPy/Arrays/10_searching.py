
# search the value and return index

import numpy as np

# -----> where() <---------

x = np.array([1,2,3,4,5,6,7,5,12,34,56,5])
y = np.where(x == 5)
""" print(y)
print(y[0]) """

# find the index where the values are even 
z = np.where(x%2 == 0)
""" print(z)
print(z[0]) """

# find the index where the values are odd
a = np.where(x%2 == 1)
""" print(a)
print(a[0]) """


#* Searchsorted() - perform binary search in array. return index
x = np.array([1,2,3,4,5,6,7])
y = np.searchsorted(x,5)
# print(y)

# search from right side
z = np.searchsorted(x, 5, side='right')
# print(z)


# Search multiple values 
a = np.searchsorted(x,[3,5])
print(a)
