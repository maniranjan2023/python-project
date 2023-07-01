for i in range(5):
    print(i)

else:      #  Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.
    print("sorry no i")


for i in []:
    print(i)

else:
    print("sorry no i")




for i in range (6):
    print(i)
    if i==4:
        break

else:
    print("sorry no i")


i = 0
while i<7:
    print(i)
    i=i+1

else:
    print("sorry")


for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")