a = [4,8,7,1,2,9,6,3,0]
print(a)

a.append(4) # insert 4 at end
print(a)


a.insert(1,1.5) # (position , value)
print(a)

a.sort()
print(a)


print(a.count(4)) # 2
a.pop() # remove last
a.clear()
a.reverse()


fruit = ['apple','mango','banana']
print(fruit.index('mango'))