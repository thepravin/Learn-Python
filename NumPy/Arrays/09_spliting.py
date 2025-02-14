
# spliting array means, breaking the array (reverse to joining)

import numpy as np

#* array_split()

x = np.array([1,2,3,4,5,6,7,8])
y = np.array_split(x,3)
""" print(y)
print(y[0])
print(y[1])
print(y[2]) """


# 2-D
a = np.array([[1,2],[3,4],[5,6],[7,8]])
b = np.array_split(a,3)
# print(b)

