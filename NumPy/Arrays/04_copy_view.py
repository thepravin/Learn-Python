
""" 
* Difference between numPy array copy and view.

- copy create new copy of array and store it, but view crete only logical copy / view copy not sotre it.

- changes done in copy array not affect the original array , but changes done in
view affect on original array.

"""


import numpy as np

x = np.array([1,2,3,4,5,6])
y = x.copy()
x[0] = 10
print(x)
print(y)


# view

a = np.array([1,2,3,4,5,6])
b = a.view()
a[0] = 10
print(a)
print(b)

