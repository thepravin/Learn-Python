""" 
- duplicate not allowed
- a = {} // syntax
- indexing not support
- mutable (changes allowed)
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


s = {1,[2,3]}
# print(s) # TypeError: unhashable type: 'list'