#Example - Map and Filter

#The checkpoint for lesson 9 required you to write a program that 
# replaced all the occurrences of "AB" in a list with the name "Alberta" and 
# then counted how many times the name "Alberta" appeared in the list.


#Example 5 contains a program that uses the map and filter functions to 
# complete the requirements of the lesson 9 checkpoint. The example program works by doing the following:

#1 .Calling the read_list function at line 39 to read all the provinces from a text file into a list. 
    # (The read_list function is in the preparation content for lesson 9.)
#2 .Calling the map function at line 55 to convert all elements that are "AB" to "Alberta."
#3 .Calling the filter function at line 67 to remove all elements that are not "Alberta."
#4 .Calling the len function at line 75 to count the number of elements that remain in the filtered list.


# Example 5

def main():
    
    #using a nexted function Here: a function inside a function.
    def read_list(filename):
    
        new_list = []
        
        with open(filename, mode="rt") as province_list:
            
            for province in province_list:
                
                province = province.strip()
                
                new_list.append(province)
                
        return new_list
    
    # Read a file that contains a list
    # of Canadian province names.
    provinces_list = read_list("provinces.txt")

    # As a debugging aid, print the entire list.
    print("Original list of provinces:")
    print(provinces_list)
    print()

    # Define a nested function that converts AB to Alberta.
    def alberta_from_ab(province_name):
        if province_name == "AB":
            province_name = "Alberta"
        return province_name

    # Replace all occurrences of "AB" with "Alberta" by
    # calling the map function and passing the ablerta_from_ab
    # function and provinces_list into the map function.
    new_list = list(map(alberta_from_ab, provinces_list))
    print("List of provinces after AB was changed to Alberta:")
    print(new_list)
    print()

    # Define a lambda function that returns True if a
    # province's name is Alberta and returns False otherwise.
    is_alberta = lambda name: name == "Alberta"

    # Filter the new list to only those provinces that
    # are "Alberta" by calling the filter function and
    # passing the is_alberta function and new_list.
    filtered_list = list(filter(is_alberta, new_list))
    print("List filtered to show Alberta only:")
    print(filtered_list)
    print()

    # Because all the elements in filtered_list are
    # "Alberta", we can count how many elements are
    # "Alberta" by simply calling the len function.
    count = len(filtered_list)

    print(f"Alberta occurs {count} times in the modified list.")


# Call main to start this program.
if __name__ == "__main__":
    main()