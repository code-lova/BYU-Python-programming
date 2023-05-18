#Loop a user inpute to compute the area of different shapes 
#Selected by the user from the meu displayed

#WORKING WITH FNCTION WHICH WE IMPORTED FROM module file in same directory

#IMPORTING THE FUNCTION 
from modules import compute_area_square, compute_area_circle, compute_area_rectangle  #Modles for cm
from modules import cal_area_rectangle, cal_area_square, calculate_area_circle   #Modules for m

#Asking for user input

end_prog = 4
value = ""

while value != end_prog:
    print()
    print("Options:")
    print("1. Area of a square in cm^2")
    print("2. Area of a rectangle in cm^2")
    print("3. Area of a circle in cm^2")
    print("4. Quit")
    print()
    print("What would you like to calculate for: ", end="")
    try:
        value = int(input(""))
        if value == 1:
            print("what is the length of a side of the square (in cm)?: ", end="")
            compute_square = float(input(""))
            #cm_result = compute_area_square(compute_square)
            #Calling the Area of Rectangle function to calculate for Area of Square
            cm_result = compute_area_rectangle(lenght=compute_square, width=compute_square)
            print("The area of a square in cm is: {} cm^2".format(cm_result))
            print()
            print("Would you like to compute for meters(m) too? : ",end="")
            choice = str(input(""))
            if choice.lower() in "yes":
                m_result = cal_area_square(compute_square)
                print("The area of a square in meters(m) is: {} m^2".format(m_result))
            else:
                print()
                print("OK")
        elif value == 2:
            print("what is the length of rectangle (in cm): ", end="")
            rectangle_len = float(input(""))
            print("What is the width of rectangle (in cm): ", end="")
            rectangle_width = float(input(""))
            cm_result = compute_area_rectangle(lenght=rectangle_len, width=rectangle_width)
            print("The area of a rectangle in cm is: {} cm^2".format(cm_result))
            print()
            print("Would you like to compute for meters(m) too? : ",end="")
            choice2 = str(input(""))
            if choice2.lower() in "yes":
                m_result = cal_area_rectangle(lenght=rectangle_len, width=rectangle_width)
                print("The area of a rectangle in meters(m) is: {} m^2".format(m_result))
            else:
                print()
                print("OK")
        elif value == 3:
            print("what is the radius of the circle (in cm): ",end="")
            compute_circle = float(input(""))
            cm_result = compute_area_circle(compute_circle)
            print("The area of a circle in cm is: {:.2f} cm^2".format(cm_result))
            print()
            print("Would you like to compute for meters(m) too? : ",end="")
            choice3 = str(input(""))
            if choice3.lower() in "yes":
                m_result = calculate_area_circle(value)
                print("The area of a circle in meters(m) is: {:.2f} m^2".format(m_result))
            else:
                print()
                print("OK..!! What else ?")
        else:
            if value == 4:
                print()
    except:
        print()
        print("Invalid Input..Try again")
    
        
        
        
        
        

        
             
        
        
        

