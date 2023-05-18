"""
A manufacturing company needs a program that will help its employees pack 
manufactured items into boxes for shipping. 
Write a Python program named boxes.py that 
asks the user for two integers:

1. the number of manufactured items
2. the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items. 
This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
    
"""

import math

num_of_items = int(input("Enter the number of items: "))
num_of_items_perbox = int(input("Enter the number of items per box: "))

cal = num_of_items / num_of_items_perbox

#Both math.celi() and round() can both round to what ever precision we set

num_round = math.ceil(cal)
print("For {} items, packing {} items in each box, you will need {} boxes.".format(num_of_items, num_of_items_perbox, num_round))

num_2_ronud = round(num_round, 1)
print("For {} items, packing {} items in each box, you will need {} boxes.".format(num_of_items, num_of_items_perbox, num_2_ronud))
