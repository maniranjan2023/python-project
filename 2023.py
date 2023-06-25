# Tuples in pythons

tup = (1,2,76,342,32, "green", True)
# tup[0]= 90
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if 342 in tup:
    print("yes 342 is present in this tuple")
else:
    print("342 is not present in this tuple")

tup2= tup[1:4]
print(tup2)

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])

# operation on tuples in pythons:

# to make change in tuple , first we need to change the tuple into list then, make  change in that list and finally change the list into the tuples: for example-
countries = ("Spain", "Italy", "India", "England", "Germany")  #tuple
temp = list(countries) #tuple is converted into list
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
res2 = tuple1.index(3)
res3 = tuple1.index(3, 4, 8)  # tuple.index(element, start, end),   #Note: This method raises a ValueError if the element is not found in the tuple.




















