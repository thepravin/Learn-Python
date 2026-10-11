""" 
- duplicate not allowed
- a = set() // syntax of empty set
- a = {1,2,"pravin"}
- indexing not support
- it is unordered
- mutable (changes allowed) but values inside set is immutable
 """

a = {1,2,4,5,5,3,4,5,6,6,1};
a.add(10)
a.remove(2)

print(a)

for element in a:
    print(element*2, end=" ")


""" 
- If you need an immutable version of a set, use frozenset, which does not allow modifications.
 """

fs = frozenset({1,2,3,4});
# fs.add(5) #* AttributeError: 'frozenset' object has no attribute 'add'
print(fs)


""" 
- In Python, sets require their elements to be immutable (unchangeable). This is because sets use a hashing mechanism to store elements efficiently, and mutable objects cannot provide a consistent hash value.
 """

""" 
✅ Allowed Elements:
1 → Integer (Immutable)
(2, 3) → Tuple (Immutable if it contains only immutable elements)
"hello" → String (Immutable)
"""
s = {1, (2, 3), "hello"}  # No error

# These objects never change, so their hash values remain consistent, making them valid set elements.


# s = {1,[2,3]}
# print(s) # TypeError: unhashable type: 'list'


s = {1,2,34,5}

print("len", len(s))

s.add(99)
print(s)

s.remove(34)
print(s)


s.clear() # empties the set

s.pop() # removes a random value


s.union(s2) # combines both set values and returns new
s.intersection(s2) # combine common values and returns new