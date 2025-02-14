
# Getting some elements out of an existing array and creating  a new array is called filtering.
# A boolean index list is a list of boolean to indexes in the array.(true and False) array and corresponding

import numpy as np

# create an array from the element on index 0 to 2:
x = np.array([41,42,43,44])
y = [True,False,True,False]
z = x[y]
# print(z)


# create a filter array
    # that will return only values higher than 42
x = np.array([41,42,43,44])
Filter_x = []
for i in x:
    if i>=42:
        Filter_x.append(True)
    else:
        Filter_x.append(False)
        

y = x[Filter_x]
""" print(y) # [42 43 44]
print(Filter_x) # [False, True, True, True] """


#* Create filter directly from array
x = np.array([41,42,43,44])
y = x >= 42
z = x[y]
print(y)
print(z)