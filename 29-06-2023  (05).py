# string format in python:

#named indexes:
txt1= "welcome to {fname} {lname}".format(fname="wscube",lname="tech")

#numbered indexes:
txt2= "welcome to {0} {1}".format("wscube","tech")

#empty placeholder:
txt3= "welcome to {} {}".format("wscube","tech")

print(txt1)
print(txt2)
print(txt3)

txt4= "welcome to {b:10} to {a}".format(a=30,b=40)
print(txt4)

txt5= "welcome to {b:<10} to {a}".format(a=30,b=40)
print(txt5)

txt6= "welcome to {b:>10} to {a}".format(a=30,b=40)
print(txt6)

txt7= "welcome to {b:^10} to {a}".format(a=30,b=40)
print(txt7)
