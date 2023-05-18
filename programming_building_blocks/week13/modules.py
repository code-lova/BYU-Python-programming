#This is a list of modules that does a specify work task as follows
import math
#function that display the user regular message as typed
def display_regular(message):
    return message

#This function displays UpperCase of the user input
def display_uppercase(message):
    upper_case = message.upper()
    return upper_case

#This function displays lowercase of the user input
def display_lowercase(message):
    lower_case = message.lower()
    return lower_case

#This function calculates for the area of a square in cm
def compute_area_square(cm):
    compute = cm * cm
    return compute

#This function calculates for the area of a square in m
def cal_area_square(m):
    compute = m / 10000
    return compute

#This function calculates for the area of a rectangle in cm
def compute_area_rectangle(lenght, width):
    compute = lenght * width
    return compute

#This function calculates for the area of a rectangle in m
def cal_area_rectangle(lenght, width):
    compute = lenght * width
    final_result = compute / 10000
    return final_result

#This function calculates for the area of a circle in cm
def compute_area_circle(cm):
    pi = math.pi
    compute = pi * cm ** 2
    return compute

#This function calculates for the area of a circle in m
def calculate_area_circle(m):
    pi = math.pi
    compute = pi * m ** 2
    final_result = compute / 10000
    return final_result


#stretch challage function goes here...!!!
#New function for area of shapes (contains all area of shares in cm so far)
#We will call other functions in this function
def compute_area(shapes, value, width=0):
    if value == 1 and width == 0:
        result = compute_area_square(shapes)
    else:
        if value == 2 and width == 0:
            result = compute_area_circle(shapes)
        else:
            if value == 3 and width != 0:
                result = compute_area_rectangle(shapes, width)
    return result
       
#This is a seperate fuction containing function to calculate for the 
#Wind chill of a particular temperature at some wind speeed mph
#Getting the temperature from the user
def compute_wind_chill(fahrenheit, value, celcius):
    if value == 1 and celcius == 0:
        compute = fahrenheit * 1.8
        new_result = compute + 32
        
        for i in range(5, 61, 5):
            wc_formula = 35.74 + 0.6215*fahrenheit - 35.75*i**0.16 + 0.4275*fahrenheit*i**0.16
            result = wc_formula
            print("At temperature {}F, and wind {} mph, the windchill is {:.2f}F".format(fahrenheit, i, result))
    else:
        if value == 2 and celcius != 0:
            compute = celcius * 9/5
            new_result = compute + 32
        
            for i in range(5, 61, 5):
                wc_formula = 35.74 + 0.6215*new_result - 35.75*i**0.16 + 0.4275*new_result*i**0.16
                result = wc_formula
                print("At temperature {}F, and wind {} mph, the windchill is {:.2f}F".format(new_result, i, result))
                
    return result
            
        
       

