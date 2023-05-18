#Loop a user inpute to compute the area of different shapes 
#Selected by the user from the meu displayed

#WORKING WITH FNCTION WHICH WE IMPORTED FROM module file in same directory

#IMPORTING THE FUNCTION 
#HERE WE DID COMBINE ALL FUNCTIONS TO FIND AREA OF SHARES INTO ONE FUNCTION CALLED
#COMPUTE_AREA, THEN THE PROGRAM DETERMINE WITH FUNCTION TO CALL IN THE COMPUTE_AREA FUNCTION
#DEPENDING ON THE USER PARAMETER INPUTED
from modules import compute_area  #Modles for shapes
from modules import cal_area_rectangle, cal_area_square, calculate_area_circle   #Modules for m



#Asking for user input

end_prog = 4
value = ""

while value != end_prog:
    print()
    print("Options:")
    print("1. Square")
    print("2. Circle")
    print("3. Rectagle")
    print("4. Quit")
    print()
    print("What would you like to calculate for: ", end="")
    try:
        value = int(input(""))
        if value == 1:
            print("what is the length of it's sides (in cm)?: ", end="")
            compute_square = float(input(""))
            result = compute_area(shapes=compute_square, value=1, width=0)
            print("The area of the square is: {} cm^2".format(result))
            print()
            print("Would you like to compute for meters(m) too? : ",end="")
            choice = str(input(""))
            if choice.lower() in "yes":
                m_result = cal_area_square(compute_square)
                print("The area of a square in meters(m) is: {} m^2".format(m_result))
            else:
                print()
                print("OK..!! What else ?")
        elif value == 2:
            print("what is the radius of the circle (in cm): ",end="")
            compute_circle = float(input(""))
            result = compute_area(shapes=compute_circle, value=2, width=0)
            print("The area of a circle in cm is: {:.2f} cm^2".format(result))
            print()
            print("Would you like to compute for meters(m) too? : ",end="")
            choice3 = str(input(""))
            if choice3.lower() in "yes":
                m_result = calculate_area_circle(value)
                print("The area of a circle in meters(m) is: {:.2f} m^2".format(m_result))
            else:
                print()
                print("OK..!! What else ?")
        elif value == 3:
            print("what is the length of rectangle (in cm): ", end="")
            rectangle_len = float(input(""))
            print("What is the width of rectangle (in cm): ", end="")
            rectangle_width = float(input(""))
            result = compute_area(shapes=rectangle_len, value=3, width=rectangle_width)
            print("The area of a rectangle in cm is: {} cm^2".format(result))
            print()
            print("Would you like to compute for meters(m) too? : ",end="")
            choice2 = str(input(""))
            if choice2.lower() in "yes":
                m_result = cal_area_rectangle(lenght=rectangle_len, width=rectangle_width)
                print("The area of a rectangle in meters(m) is: {} m^2".format(m_result))
            else:
                print()
                print("OK")
        
        else:
            if value == 4:
                print()
    except:
        print()
        print("Invalid Input..Try again")
        
        
        
        
        
        
        
    