#list methods:

colors = ["voilet", "indigo", "blue", "green"]
colors.sort() # This method sorts the list in ascending order.
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
l= max(num)
print(l)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
p= min(num)
print(p)

colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True) # to print the list in descending order.We must give reverse=True as a parameter in the sort method.
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)

colors = ["voilet", "indigo", "blue", "green"]
colors.reverse() #This method reverses the order of the list.
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green")) #This method returns the index of the first occurrence of the list item.

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green")) #Returns the count of the number of items with the given value.

colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy() # Returns copy of the list
print(colors)
print(newlist)

colors = ["voilet", "indigo", "blue"]
colors.append("green") # This method appends items to the end of the existing list
print(colors)

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

# add a list to a list:

colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow) #This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
print(colors)

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2) # You can simply concatenate two lists to join two lists.





















