"""
Prove that you can write a Python program 
that gets input from a user, performs arithmetic,
and displays results for the user to see.
The size of a car tire in the United States is 
represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. 
The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. 
The volume of space inside a tire can be approximated with this formula:

v = π w2 aw a + 2,540 d
    10,000,000,000
"""


"""
EXCEEDING REQUIREMENTS - STRETCH

Find tire prices for four or more tire sizes online. 
Add a set of if … elif … else statements in your program t
hat use the tire width, 
tire aspect ratio, and wheel diameter that the user enters 
to find a price and then print the price.

"""


import math
from datetime import datetime, timedelta

#INITIALIZING VARIABLES HERE 
price = 0
end_prog = 0
start_prog = 1
choice = ""
mobile = "Null"

print("Enter the width of the tire in mm (ex 205):",end=" ")
tire_width = float(input(""))
print("Enter the aspect ratio of the tire (ex 60):",end=" ")
ratio = float(input(""))
print("Enter the diameter of the wheel in inches (ex 15):",end=" ")
diameter = float(input(""))

#Find the price of tire according to the width, ratio and diameter given.
if tire_width <= 185 or ratio <= 65 and diameter == 14:
    price = 43.46
elif tire_width <= 195 or ratio <= 65 and diameter == 15:
    price = 65.18
else: 
    if tire_width >= 205 or ratio < 70:
        if diameter == 16:
            price = 65.18
        else:
            price = 75.60
    else:
        if tire_width >= 205 or ratio == 70:
            price = 75.60
        
#Calculation with inputs of width, ratio and diamater  
pi = math.pi
vol_1 = tire_width * ratio + 2540 * diameter
volume = pi * tire_width**2 * ratio * vol_1
final = volume / 10000000000

print("The approximate volume is {:.2f} liters".format(final))

#While loop here to as if the user wants to buy the tire
while start_prog != end_prog:
    print("Do you want to buy tires with the dimensions that you entered?:", end=" ")
    choice = input("")
    if choice.lower() in "yes":
        print("What is your phone numbe?:", end=" ")
        mobile = int(input(""))
        print("The Total price of the tire is: ${}".format(price))
    else:
        print("The approximate volume is {:.2f} liters".format(final))
        print("The Total price of the tire is: ${}".format(price))
    end_prog += 1


#Delcaring varables here for data to be written to volume.txt file
round_tire_width = math.ceil(tire_width)
round_ratio = math.ceil(ratio)
round_diameter = math.ceil(diameter)

#Getting the  current time from computer with datetime() function
curren_date_time = datetime.now()
print("{:%Y-%m-%d}, {}, {}, {} {:.2f} ".format(curren_date_time, round_tire_width, round_ratio, round_diameter, final))

#Writting data to volume.txt file here...
width_of_the_tire = round_tire_width
aspect_ratio_of_the_tire = round_ratio
diameter_of_the_wheel = round_diameter
volume_of_the_tire = round(final, 2)

with open("volumes.txt", "at") as vol_details:
    
    print(f"{curren_date_time:%Y-%m-%d}, {width_of_the_tire}, {aspect_ratio_of_the_tire}, {diameter_of_the_wheel}, {volume_of_the_tire}, +{mobile}", file=vol_details)
    
    





