txt = "For only {price:.2f} dollars!" # 2f means round off the price to two decimal place
print(txt.format(price = 49))

val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.3f} dollars!" # 3f means round off to three decimal place
print(txt)

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

# print(txt.format())
print(type(f"{2 * 30}"))
print(f"{2 * 30}") #it in a single statement as well.
