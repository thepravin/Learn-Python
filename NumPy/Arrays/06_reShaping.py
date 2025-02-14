

# reshaping : chaging the shape of array, like adding or removing the elements.

import numpy as np

# reshaping from 1-D to 2-D
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = x.reshape(4,3) #  4 different arrays divided into 3 elements
# print(y) 


# reshaping from 1-D to 3-D
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b = a.reshape(2,3,2) # first 2 means divide the array into 2 parts. 3 means each part contain 3 rows and each row contain 2 elements.
# print(b)

#* above reshape return copy (or new array)


# Return view (or original array)
c = np.array([1,2,3,4,5,6,7,8])
print(c.reshape(2,4).base)