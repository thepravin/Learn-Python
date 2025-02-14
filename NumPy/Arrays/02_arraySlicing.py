
# slicing array -  slicing in python means taking elements from one given index to another index.

# [start : end] , [start : end : step]  :=> start->include, end->exclude (index)


import numpy as np


# now slice elements from 1 to 5 :
x = np.array([1,2,3,4,5,6,7,8,9]);

print(x[0:5]) # [1 2 3 4 5]
print(x[5:]) #  [ 6  7  8  9]
print(x[:5]) # [1 2 3 4 5]

# negative slicing -
print(x[-3:-1]) #[7 8]


# Step : step value determine the step of slicing

# return every alternative value from index 1 to 5
x = np.array([1,2,3,4,5,6,7,8,9])
print(x[::2])


# Slicing 2-D Array 
y = np.array([[1,2,3],[4,5,6]])
print(y[1,0:2])
print(y[:,::2])