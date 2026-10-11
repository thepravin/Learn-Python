""" 
a = {key:value, key:value...}

- same key not present multiple times, value get changed.
- mutable (This means you can modify them after creation by adding, updating, or removing key-value pairs.)

- The keys must be immutable (numbers, strings, tuples).
- The values can be mutable (lists, sets, other dicts).

 """

a = {1:1, 'name':'pravin', 2:54 , 5:6}

for i in a:
    print('Keys : ',i,end=" ")
    print('| Values : ',a[i])


a['name'] = 'ganesh'

print(len(a))

print(a.keys())
print(list(a.keys()))

print(a.values())
print(list(a.values()))

print(a.items())  # returns all (key,value) pairs as tuples
print(list(a.items()))

print(a.get("name"))
print(a.update({"city":"pune"})) #inserts the specified items to dictionary
print(a)

#* If you want an immutable dictionary, use MappingProxyType from the types module.

from types import MappingProxyType

original_dict = {'x':10,'y':20}
immutable_dict = MappingProxyType(original_dict)

print(immutable_dict['x']) #10
# immutable_dict['x'] = 100 # TypeError: 'mappingproxy' object does not support item assignment