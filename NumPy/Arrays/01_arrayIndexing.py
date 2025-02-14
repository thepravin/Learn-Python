


import numpy as np

# 1-D
x = np.array([1,2,3,4])
print(x[0]) # 1
print(x[-1]) # 4

# 2-D
y = np.array([[1,2,3],[4,5,6]])
print(y[0,1]) # 2
print(y[1,-1]) # 6

# 3-D
z = np.array([[[1,2,3,4],[5,6,7,8]], [[9,10,11,12],[13,14,15,16]]])
print(z[0,1,2]) # 7