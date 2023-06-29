def average (a=9, b=1):
    print("the average is ", (a+b)/2)
average(4,6)
average(b=9)
average(b=9,a=21)

def average (a=9, b=1, c=6):
    print("the average is ", (a+b+c)/3)
average(4,6,5)

# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     sum= sum + i
#     print("Average is :", sum/len(numbers))

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
#
# name("Peter", "Quill")

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")











