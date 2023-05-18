# here i can use my custom made modules 
from modules_scripts import namer
from modules_scripts import add
from modules_scripts import stat_range, get_initials

namer("Jerry")

x = 3
y = 5
print("The answer is {}".format(add(x,y)))

#check the stat_range function in modules_scripts
print(stat_range([1,3,4,5,6,59,30]))

for num in range(5):
    print("{:02d}".format(num), end=" ")
    
print()  
print("Enter a number to add")
print()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The answer is: {}".format(add(num1, num2)))

print()

print("---Enter your first and second name to get initials--")
first_name = str(input("Enter first name: "))
first_name = get_initials(first_name, False)
print("Your initials are: {}".format(first_name))

#secondly working this the get_initials functon 
#we can also assign the values to parameters by name called the named notation
#when you call the function
print()
print("---Enter your first and second name to get initials--")
first_name = str(input("Enter first name: "))
first_name = get_initials(force_uppercase=False, name=first_name)
print("Your initials are: {}".format(first_name))

def myfun(counter=89):
    return counter + 1
print(myfun())
