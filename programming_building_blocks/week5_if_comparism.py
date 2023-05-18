#A program to determine which of the number is greatest
first_num = input("Enter first number: ")
second_num = input("Enter Second number: ")
animal = input('Enter your favourite animal: ')

# Working the number comparism here
if first_num > second_num:
    print("First number is greater")
else:
    print("The first number is not greater")
    
if first_num == second_num:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")
    
if second_num > first_num:
    print("The second number is greater")
else:
    print("The second number is not greater")

# String comparism program goes here
if animal.lower() == "lion":
    print("Thats my favourite animal too!")
else:
    print("That one is not my favorite")

    