str1="AbcDEfghIJ"
print(str1.upper())

str2="AbcDEfghIJ"
print(str2.lower())

str3 = " Silver Spoon "
print(str3.strip())

str4="Hello !!!"
print(str4.rstrip("!"))

str5="silver spoon"
print(str5.replace("sp","M"))
print(str5.replace("sil","oli"))

str6="silver ,spoon are very costly"
print(str6.split(" ,"))
str6="silver ,spoon are very costly"
print(str6.split(" "))

str7="silver spoon are very costly"
print(str7.capitalize())

str8 = "Welcome to the Console"
print(str8.center(40))
print(str8.center(91))
print(str8.center(30))
print(len(str8.center(40)))
print(len(str8.center(91)))
print(len(str8.center(30)))

str9="Welcome"
print(str9.center(10,"!"))
print(str9.center(11,"!"))
print(str9.center(12,"!"))
print(str9.center(15,"!"))

str10= "Abracadabra"
print(str10.count("a"))
print(str10.count("b"))
print(str10.count("da"))
print(str10.count("ra"))
print(str10.count("da"))
print(str10.count("ar"))

str11= "welcome to the console!!!"
print(str11.endswith("console!!!"))
print(str11.endswith("!!!"))
print(str11.endswith("console"))

str12= "welcome to the console!!!"
print(str12.endswith("to",0,10))
print(str12.endswith("to",0,9))
print(str12.endswith("to",3,10))
print(str12.endswith("to",5,10))

str13 = "He's name is Dan. He is an honest man."
print(str13.find("is"))
print(str13.find("an"))
print(str13.find("honest"))
print(str13.find("Daniel"))
print(str13.find("Dan"))

print(str13.index("Dan"))
#print(str13.index("Daniel"))

str14 = "WelcomeToTheConsole"
print(str14.isalnum())
str15 = "Welcome To The Console"
print(str15.isalnum())
str16 = "Welcome To The Console 001"
print(str16.isalnum())

str17="welcome"
print(str17.isalpha())
str18="welcome01"
print(str18.isalpha())

str19="welcome"
print(str19.islower())
str20="Welcome"
print(str20.islower())

str21 = "We wish you a Merry Christmas"
print(str21.isprintable())

str22 = "        "       #using Spacebar
print(str1.isspace())
str23 = "        "       #using Tab
print(str2.isspace())

str24= "World Health Organisation"
print(str24.istitle())
str25= "World health Organisation"
print(str25.istitle())

str26= "Python is a Interpreted Language"
print(str26.startswith("python"))
print(str26.startswith("Python"))

str27= "Python is a Interpreted Language"
print(str27.swapcase())

str28 = "He's name is Dan. Dan is an honest man."
print(str28.title())

a= int(input("Enter your age: "))
print("Your age is:", a)
#conditional operators
# >, <, >=, <=, ==, !=
#>, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
    print("you can drive")
    print("yes")
else:
    print("you cannot drive")
    print("No")
    print("yay!")

applePrice = 210
budget = 200

if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

appleprice= 10
budget=200
if (budget-appleprice >50):
    print("ravi,add 1 kg Apples to the cart.")
else:
    print("ravi,do not add apple to the cart.")

num=int(input("Enter the value of num: "))
if(num < 0 ):
    print("number is negative")
elif (num == 0):
    print("number is zero")
else:
    print("Number is positive")

num = int(input("Enter the digit"))
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("number is between 1-10")
    elif (num > 10 and num <= 20):
        print("number is between 11-20")
    else:
        print ("Number is greater than 20")
else:
    print("Number is zero")







































