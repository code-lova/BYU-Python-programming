# Example 1
#In this week example we are dealing with funcion al programming 
#where we test different means of solving problmes with functions, nexted-function, and lambda
#The Python programming language allows a programmer to pass a function as an argument into 
# another function. A function that accepts other functions in its parameters is known as a 
# higher-order function. Higher-order functions are often used to process the elements in a list. 
# Before seeing an example of using a higher-order function to process a list, 
# first consider the program in example 1 that doesn’t use a higher-order function but instead uses
# a for loop to convert a list of temperatures from Fahrenheit to Celsius.

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = []
    for fahr in fahr_temps:
        cels = cels_from_fahr(fahr)
        cels_temps.append(cels)

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


def cels_from_fahr(fahr):
    """Convert a Fahrenheit temperature to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)


# Call main to start this program.
if __name__ == "__main__":
    main()
    
    
#Writing a for loop like this is the traditional way to 
# process all the elements in a list and doesn’t use higher-order functions.