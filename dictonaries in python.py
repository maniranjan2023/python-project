d={'name':'python','fees':8000,'duration':'2'}
print(type(d))
print(d)

f=d['fees']
print(f)

for n in d:  # this will print key
    print(n)

for n in d:  # this will print value
    print(d[n])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())  # We can print all the values in the dictionary using values() method.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys()) # We can print all the keys in the dictionary using keys() method.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items()) # We can print all the key-value pairs in the dictionary using items() method.

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")


# dictionaries method in python:

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
print(ep1)

ep1.clear()
print(ep1)

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})  #  The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
info.update({'DOB':2001})  # The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear() # The clear() method removes all the items from the list.
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')  #  The pop() method removes the key-value pair whose key is passed as a parameter.
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()  #  The popitem() method removes the last key-value pair from the dictionary.
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']  #  we can also use the del keyword to remove a dictionary item. info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info)

#info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
#del info
#print(info)








