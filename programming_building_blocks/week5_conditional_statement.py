price = 2
if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)

#String comprisim
country = "CANADA"
if country.lower() == "canada":
    print("Oh you are from canada")
else:
    print("You are not from canada")

#Using as user input for conditional statement
# cost = float(input("How much did you pay: "))
# if cost >= 1.00:
#     tax = 0.7
# else:
#     tax = 0
# print("your tax value is {}".format(tax))

# #Using Multiple IF statement
# province = input("Enter the province you live in: ")
# tax = 0
# if province == "Alberta":
#     tax = 0.05
# if province == "Nunavut":
#     tax = 0.05
# if province == "Ontario":
#     tax = 0.13
# print(tax)

# #Using ELIF with one if conditonal statement
# province = input("Enter the province you live in: ")
# tax = 0
# if province == "Alberta":
#     tax = 0.05
# elif province == "Nunavut":
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)


# #using OR with conditonal statement
# province = input("Enter the province you live in: ")
# tax = 0
# if province == "Alberta" or province == "Nunavut":
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)

#Using IN with multiple conditonal statement instead of OR
province = input("Enter the province you live in: ")
tax = 0
if province in ("Alberta", "Yukon", "Nunavut"):
    tax = 0.05
elif province == "Ontario":
    tax = 0.13
else:
    tax = 0.15
print(tax)


    