# greeting message for user:

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

#x = 4
# x is the variable to match
#match (x):
    # if x is 0
    #case 0:
        #print("x is zero")
    # case with if-condition
    #case 4 if x % 2 == 0:
       # print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
   # case _ if x < 10:
        #print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    #case _:
        #print(x)

name= 'Abhishek'
for i in name:
        print(i, end=", ")

surname= input("\nwhat is your name? ")
for i in surname:
    print(i, end=",")

colors= ["\nRed", "Green", "Blue","yellow"]
for y in colors:
    print(y,end=",")

colors = ["\nRed", "Green", "Blue", "yellow"]
for i in colors:
    print(i)

for k in range(5):
    print(k)
for k in range(1,2001):
    print(k)
for k in range(5):
    print(k+1)
# range automatically write all the number as per given command by user
for k in range(4,15):
    print(k)

for k in range(1,10,13):
    print(k)

count= 5
while (count > 0):
    print(count)
    count= count-1
else:
    print("I am inside else")

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break

#range(5): it means start =0, condition<5, increment=1 so output is 0,1,2,3,4
#range(1,6): it means start=1, condition <6, increment=1 so output is 1,2,3,4,5
#range(1,6,2):it means start =1,condition<6, increment=2, so output is 1, 3 ,5

for n in range (5):
    print(n)

for m in range(5):
    print("welcome")

for p in range(1,6):
    print(p)

for r in range(1,6,2): #forward loop, range(start,end,jump)
    print(r)

for s in range(10,0,-1): #reverse loop , range(start,end, jump)
    print(s)





















