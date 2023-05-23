#Example - Sorting a Compound List

#Python includes a built-in higher-order function named sorted that 
# accepts a list as an argument and returns a new sorted list. 
# Calling the sorted function is straightforward for a simple 
# list such as a list of strings or a list of numbers as shown in example 6 and its output.

# Example 6

def main():
    # Create a list that contains country names
    # and print the list.
    countries = [
        "Canada", "France", "Ghana", "Brazil", "Japan"
    ]
    print(countries)

    # Sort the list. Then print the sorted list.
    sorted_list = sorted(countries)
    print(sorted_list)


# Call main to start this program.
if __name__ == "__main__":
    main()