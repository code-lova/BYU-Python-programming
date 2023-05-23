import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    
    students_list = read_compound_list("pupils.csv")
    
    
    #print(students_list)
    print("THE ORIGINAL LIST UNSORTED")
    print(students_list)
    
    # Define a lambda function that extracts a student's birth date.
    birth_date = lambda new_list: new_list[BIRTHDATE_INDEX]
    
    # Define a lambda function that extracts a student's given name.
    given_name = lambda new_list: new_list[GIVEN_NAME_INDEX]
   
    def extract_month_day(student):
        """Sort a list of students by their birth month and day.
        In other words sort the list by their birthdate but ignore
        the year of their birthdate.

        Args:
            student (list): a list that contains small lists.
            Each small list contains the given name,
            surname, and birthdate of one student.

        Returns:
            list: a new list of students that is sorted by birth
        month and day.
        """
        birth_string = student[BIRTHDATE_INDEX]
        month_and_day = birth_string[5:]
        return month_and_day
        pass
    
    
    
    # Call the sorted function to sort the list
    # of students by their birth date.
    sorted_birth_day = sorted(students_list, key=birth_date)
    
    # Call the sorted function to sort the list
    # of students by their given name.
    sorted_given_name= sorted(students_list, key=given_name)
    
    # # Call the sorted function to sort the list
    # of students by their birth month and day.
    sorted_month_and_day = sorted(students_list, key=extract_month_day)
    
    #PRINTING THE RSULTS as each student data in a seperate line.
    print()
    print("List of pupils sorted by birthdays")
    for each_pupil_birthday in sorted_birth_day:
        print(each_pupil_birthday)
        
    print()
    
    print("List of pupils sorted by Given Name")
    for each_given_names in sorted_given_name:
        print(each_given_names)
        
    print()  
     
    print("List of pupils sorted by month and day")
    for each_month_day in sorted_month_and_day:
        print(each_month_day)
    
    pass

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(pupil_list):
    """print each pupil in the pupil list as an 
    element in a different line

    Args:
        pupil_list (string): list

    Returns:
        string: list
    """
    for pupils in pupil_list:
        print(pupils)


# Call main to start this program.
if __name__ == "__main__":
    main()