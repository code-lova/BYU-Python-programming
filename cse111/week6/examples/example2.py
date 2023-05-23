#---Passing a Function into another Function---

#Python includes a built-in higher-order function named map that will process all the elements 
# in a list and return a new list that contains the results. THE MAP FUNCTION accepts a function 
# and a list as arguments and contains a loop inside it, so that when a programmer calls the map function, 
# he doesn’t need to write a loop. The map function is a higher-order function because it accepts a function as an argument. 
# Consider the program in example 2 that produces the same results as example 1.

# Example 2

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))

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
    
    
#Notice that example 2, doesn’t contain a for loop. Instead, at line 17, 
# it contains a call to the map function. 
# Remember that the map function has a loop inside it, 
# so that the programmer who calls map, doesn’t have to write the loop. 
# Notice also at line 17 that the first argument to the map function is the name 
# of the cels_from_fahr function. In other words, at line 17, we are passing the cels_from_fahr 
# function into the map function, so that map will call cels_from_fahr for each element in the fahr_temps list.