
# Create numpy ndarray object


import numpy as np


x = np.array([1,2,3,4,5,6]);
print(x);
print(type(x));



# we can also pass a list, tuple or any array like object with array(). and it will be converted to ndarray.

y = np.array((1,2,3,4));
print(y);
print(type(y))


# Dimensions in Arrays : 

# 0-D arrays - scalars, are the elements in array, each value in an array is a 0-D array.
x = np.array(42)
print(x)

# 1-D arrays
x = np.array([1,2,3,4])
print(x)


# 2-D arrays
x = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(x);

# 3-D arrays : with two 2-D arrays
x = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [1,2,3],
        [4,5,6]
    ]
])
print(x)


# check how many dimensions the array have
a =  np.array(43)
b =  np.array([1,2,3,4,5])
c =  np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

d = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [1,2,3],
        [4,5,6]
    ]
])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

 
 # create array with 5 dimensions
x = np.array([1,2,3,4,5],ndmin=5)
print(x)
print("Dimensions : ",x.ndim)