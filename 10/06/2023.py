print('hey i am a \"good boy\"\nand this viewer is also a good boy/girl')
print('''hey i am a "good boy" and this viewer is also a good boy/girl''')
print("hey",6,7,sep="~",end="009\n")
print("herry")


a=complex(8,2)
a1=9
print(a)
b="harry"

print(b)
print(a+a1)
print("the type of a is",type (a))
print("the type of b is",type (b))
print("the type of a1 is",type (a1))


dict1={"name":"sakshi","age":20,"canvote":True}
print(dict1)

print(17/3)
print(17//3)
print(8%3) #???
print(5**3)

#creating a calculator:
a=50
b=3

print("the value of",a, "+", b, "is",a+b)
print("the value of",a, "-", b, "is",a-b)
print("the value of",a, "*", b, "is",a*b)
print("the value of",a, "/", b, "is",a/b)

a=input("enter your name:")
print("my name is",a)

#a=input("enter the first number")
#b=input("enter the second number")
#print(int(a)+int(b))

name="maniranjan"
friend="rohan"
sentence='''he said hi herry hey i am good 
"i want to eat an apple"'''
print(sentence)

print('He said, "I want to eat an apple".')

symbol='''Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.
Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.
How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience'''
print(symbol)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])


print("let use for a  loop\n")

for character in sentence:
    print(character)

name="Harry,shubham"
print(name[0:4])
print(name[0:5])
print(name[0:3])
print(name[0:2])

fruit="Mango"
length=len(fruit)
print(length)
print(fruit[0:-3])  # this is equal_ print(fruit[0:len(fruit)-3])
print(fruit[-3:-1])

student= "maniranjan"
print(student[-4:-2])




