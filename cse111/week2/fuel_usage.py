#This is a python program that have a main function that handles
#user input and print function 
#wihin the main are two other functions that performes 
#calculations and return the value for the main function to print.

def main():
    x_miles = float(input("Enter the first odometer reading (miles): "))
    y_miles = float(input("Enter the second odometer reading (miles):"))
    z_amount = float(input("Enter the amount of fuel used (gallons): "))
    
    final = miles_per_gallon(start_miles=x_miles, end_miles=y_miles, gallon_amount=z_amount)
    print("{:.1f} miles per gallon".format(final))
    next_final = lp100k_from_mpg(calculation=final)
    print("{:.2f} liters per 100 kilometers".format(next_final))

def miles_per_gallon(start_miles, end_miles, gallon_amount):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Args:
        start_miles (float): An odometer value in miles
        end_miles (float): Another odometer value in miles
        gallon_amount (float): A fel amount in U.S gallons

    Returns:
        value: Fuel efficiency in miles per gallon.
    """
    mpg_value = abs(end_miles - start_miles) / gallon_amount
    calculation = mpg_value
    return calculation



def lp100k_from_mpg(calculation):
    """Converts miles per gallon to liters per 100
    kilometer and return the converted value.

    Args:
        calculation (float): a value in miles per gallon

    Returns:
        Result: The converted value in liters per 100km
    """
    result = 235.215 / calculation
    return result


main()