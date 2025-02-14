

import numpy as np

# generate a random number from 0 to 100
x = np.random.randint(100)
# print(x)

#* import only perticulor function from numpy
from numpy import random

# generate random float
y = random.rand()
# print(y)

# You can also generate random array.
    # generate a 1-D array containing 5 random int from 0 to 100:
z = random.randint(100, size=(4))
# print(z)

 # generate a 2-D array containing  random int from 0 to 100:
z = random.randint(100, size=(4,3))
# print(z)

 # generate a 2-D  array containing random float :
z = random.rand(4,3)
# print(z)


# you can generate random numbers from array
# choice()
x = random.choice([3,5,7,9,1,4,6])
# print(x)

# you can generate random numbers from 2-D array
# choice()
x = random.choice([3,5,7,9,1,4,6],size=(3,5))
print(x)

