
# Permutaion refers to an arrangment of elements like [3,2,1] is permutaion of [1,2,3] and vice versa.

# numpy random module provide 2 methos : shuffle(), permutation(),

# shuffle() make changes on original array.
# permutaion() make a copy of original array.

from numpy import random
import numpy as np

# now we will randomly suffle elements for the below array:
x = np.array([1,2,3,4,5,6])
random.shuffle(x)
# print(x)

# now generate permutaion of elements for the below array:
x = np.array([1,2,3,4,5,6])
y = random.permutation(x)
print(y)
