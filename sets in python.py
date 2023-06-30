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

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2) #The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2) # update() method adds item into the existing set from another set.
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2) # The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)  # intersection_update() method updates into the existing set from another set.
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)  # The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)  # symmetric_difference_update() method updates into the existing set from another set.
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2) # The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}  
print(cities.difference(cities2)) 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))  # The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3)) # The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities)) # The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities  # del is not a method, rather it is a keyword which deletes the set entirely.
print(cities) 

info = {"Carla", 19, False, 5.9}  #  check if an item exists in the set or not.
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")


















