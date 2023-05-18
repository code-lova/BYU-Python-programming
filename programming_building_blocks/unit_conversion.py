#Purpose: Convert Degree in Fahrenheit to Celsius

temperature = float(input("What is the Temperature in Fahrenheit: "))
result = temperature - 32
celcius_result = result * 5/9
#Rounding to 1 decimal place of precision
round_celcius = round(celcius_result, 1)
print("The temperature in Celsius is {} degrees.".format(round_celcius)) #This Uses the round() function in python

#Another method to round decimal mumber sin python is
#rounding to 1 decimal place of precision
print(f"The temperature in Celsius is {celcius_result:.1f} degrees.")


