

nums = [1, 2, 3, 4, 5, 6]

# Square only even numbers
squared_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(squared_evens)  # Output: [4, 16, 36]
