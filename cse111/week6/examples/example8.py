#Consider the compound list named students that contains data about 
# various students in example 8. Within the list, each student’s given name 
# and surname are stored separately. 
# It is common for a user to want such a list to be sorted by surname and then by given name.
# A simple way to do that is to write a key function that combines the surname and given name 
# elements and returns the combined name as the key that the sorted function will use for sorting.

#Lines 21–22 in example 8 contain a lambda function that combines a student’s 
# surname and given name into a string that is used as the key by the sorted 
# function at line 25. Notice in the output from example 8 that the students 
# are sorted by surname and then by given name.


# Example 8

def main():
    # Create a list that contains data about young students.
    students = [
        # [given_name, surname, reading_level]
        ["Robert", "Smith", 6.7],
        ["Annie", "Smith", 6.2],
        ["Robert", "Lopez", 7.1],
        ["Sean", "Li", 5.6],
        ["Sofia", "Lopez", 5.3],
        ["Lily", "Harris", 6.7],
        ["Alex", "Harris", 5.8]
    ]

    GIVEN_INDEX = 0
    SURNAME_INDEX = 1
    
    print()
    #PRINTING ORIGINAL STUDENT LIST
    print("ORIGINAL: original student list")
    for the_student in students:
        print(the_student)
        
    print()
    
    # Define a lambda function that combines
    # a student's surname and given name.
    combine_names = lambda student_list: \
         f"{student_list[SURNAME_INDEX]}, {student_list[GIVEN_INDEX]}"
    
    # Sort the list by the combined key of surname, given_name.
    sorted_list = sorted(students, key=combine_names)
    
    print("SORTED: The new sorted list")
    # # Print the list.
    for each_student in sorted_list:
        print(each_student)
    print()
    
    #OR WE CAN USE THE BELOW CLODE TOO
    #PRINT SAME RESULT 
    
    # GIVEN_INDEX = 0
    # SURNAME_INDEX = 1

    # # Define a lambda function that combines
    # # a student's surname and given name.
    # combine_names = lambda student_list: \
    #     f"{student_list[SURNAME_INDEX]}, {student_list[GIVEN_INDEX]}"

    # # Sort the list by the combined key of surname, given_name.
    # sorted_list = sorted(students, key=combine_names)

    # # Print the list.
    # for student in sorted_list:
    #     print(student)
        
        


# Call main to start this program.
if __name__ == "__main__":
    main()