#WORKING WITH FUNCTION WHICH WE IMPORTED FROM module file in same directory

#IMPORTING THE FUNCTION 
#WIND CHILL CALCULATION IMPORTING THE FORMULAS
from module import compute_wind_chill  #Modles for shapes

print("What is the temperature ?: ",end="")
try:
    value = float(input(""))
    print("Fahrenheit or Celsius (F/C): ",end="")
    choice = str(input(""))
    if choice.lower() in "f":
        compute_wind_chill(fahrenheit=value, value=1, celcius=0)
    else:
        if choice.lower() in "c":
            compute_wind_chill(fahrenheit=0, value=2, celcius=value)
except:
    print("Invalid Input")