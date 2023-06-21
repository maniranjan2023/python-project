for i in range(0,12):
    print(" 5 X", i+1, "=", 5 * (i+1))
    if(i==9):
        break

print("Loop ko chodkar nikal gaya")

for i in range(0,12):
    if (i == 9):
        break
    print(" 5 X", i+1, "=", 5 * (i+1))

print("Loop ko chodkar nikal gaya")

for i in range(0,12):
    if (i == 9):
        print("skip the iteration")
        continue
    print(" 5 X", i, "=", 5 * i)

i=0  #i=0 is the initial value and always type the the inital value
while True :
    print(i)
    i=i+1
    if(i%100 == 0):
        break

print("end")

i=0   #i=0 is the initial value and always type the the inital value
while True :
    print(i)
    i=i+1
    if(i%100 == 0):
        break

print("end")

# Function in python

def calculategmean(a, b):
    gmean = (a*b)/(a+b)
    print(gmean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greatar or equal")

def isLesser(a, b):
    pass

a= 10
b= 8
isGreater(a, b)
calculategmean(a, b)

c=10
d=15
isGreater(c, d)
calculategmean(c, d)












