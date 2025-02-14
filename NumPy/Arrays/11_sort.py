

import numpy as np


x = np.array([2,4,6,10,5])
y = np.sort(x)
print("x : ",x) # [ 2  4  6 10  5]
print("y : ",y) # [ 2  4  5  6 10]

# string
x = np.array(['banana','mango','apple'])
print(np.sort(x))


# sorting the 2-D array
a = np.array([[3,2,4],[5,0,1]])
print(np.sort(a))