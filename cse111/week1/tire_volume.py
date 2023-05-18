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
import math
from datetime import datetime, timedelta


print("Enter the width of the tire in mm (ex 205):",end=" ")
tire_width = float(input(""))
print("Enter the aspect ratio of the tire (ex 60):",end=" ")
ratio = float(input(""))
print("Enter the diameter of the wheel in inches (ex 15):",end=" ")
diameter = float(input(""))

pi = math.pi
vol_1 = tire_width * ratio + 2540 * diameter
volume = pi * tire_width**2 * ratio * vol_1
final = volume / 10000000000
print("The approximate volume is {:.2f} liters".format(final))

round_tire_width = math.ceil(tire_width)
round_ratio = math.ceil(ratio)
round_diameter = math.ceil(diameter)


curren_date_time = datetime.now()
print("{:%Y-%m-%d}, {}, {}, {} {:.2f} ".format(curren_date_time, round_tire_width, round_ratio, round_diameter, final))


width_of_the_tire = round_tire_width
aspect_ratio_of_the_tire = round_ratio
diameter_of_the_wheel = round_diameter
volume_of_the_tire = round(final, 2)

with open("volumes.txt", "at") as vol_details:
       
    print(f"{curren_date_time:%Y-%m-%d}, {width_of_the_tire}, {aspect_ratio_of_the_tire}, {diameter_of_the_wheel}, {volume_of_the_tire}", file=vol_details)
    
    
    
