""" 
- syntax : map(function, iterable)

- The map() function applies a function to each item in an iterable (like a list) and returns a new iterable.

 """

#*------------- using lambda functions ---------------
nums = [1,2,3,4]
square = list(map(lambda x: x*2, nums))
print(square)

#* --------------- using user define function -----------

def double(x):
    return x*2

nums2 = [1,2,3,4]
square2 = list(map(double,nums2))
print(square2)