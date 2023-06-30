s={10,20,30,40}
print(s)

for a in s:
    print(a)

l =[10,20,30,40]
s=set(l) # set() used to convert the list or string into set
print(s)

s={10,20,30,40}
s.remove(20) # remove() function is used to remove the element that we assigned inside the curly bracket ().
print(s)

s={10,20,30,40}
s.discard(20)  # discard() have same function as that of remove()
print(s)

s={10,20,30,40}
s.pop() # this function randomy delete any element from the sets
print(s.pop()) # this is used to display which element is deleted
print(s)

s={10,20,30,40}
s.clear() # used to clear all the element of the sets
print(s)

s={10,20,30,40}
s.add(60) # used to add an element in sets
print(s)

l=[15,25.35,75]
s={10,20,30,40}
s.update(l) # this means update l inside  s
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

















