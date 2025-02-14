

import numpy as np


# 1-D
x = np.array([1,2,3,4,5,6,7,8])
""" for i in x:
    print(i,end=" ") """
    

# 2-D
y = np.array([[1,2,3,4,5],[6,7,8,9,10]])
""" for i in y:
    print(i) """
    
""" 
for i in y:
    for a in i:
        print(a,end=" ") """
        
        
# 3-D
z = np.array([[[1,2,3],[4,5,6]]])

""" for i in z:
    for j in i:
        for k in j:
            print(k,end=" ") """
            
            
#* -------------->  nditer() function <-----------------

# 3-D

""" for i in np.nditer(z):
    print(i,end=" ") """


# Iterate with different step sizes.

for i in np.nditer(y[:,::2]):
    print(i, end=" ")