#write a Python program named students.py 
# that has at least two functions named main and read_dictionary.
# Having a key as I-Number and Names as values 

import csv

def main():
    
    STUDENT_INUM_INDEX = 0
    STUDENT_NAME = 1
    
    new_dictionary = read_dictionary("students.csv", STUDENT_INUM_INDEX)
    
    print(new_dictionary)
    print()
    print("--PLEASE ENTER AN I-NUMBER TO SERACH FOR A STUDENT")
    
    print("Enter I-Number:", end=" ")
    number = input("")
    
    #First, initialize the special character list that needs to be replaced:
    special_char = ['-']
    
    #Next, call the “for” loop and replace the special characters with an empty string. 
    #Then, passes to the “number” integer type variable:
    for i in special_char:
        number = number.replace(i, '')
    
    #declearing variables
    i_number_length = len(number)
    original_length = 9
    
    
    #Checking if the I-Number is present in the dictionary
    #Using I-Number as the Key to get student name
    #Which is the value matching that particular key
    if number in new_dictionary:
        name = new_dictionary[number]
        dd = name[STUDENT_NAME]
        print(dd)
    #If there are too few digits in the I-Number  
    elif i_number_length < original_length:
        print("Invalid I-Number: too few digits") 
    
    #If there are too many digits in the I-Number
    elif i_number_length > original_length:
        print("Invalid I-Number: too many digits")  
    
    elif not number.isdigit():
        print("Invalid I-Number")   
         
    else:
        print("No such student")
    
    pass


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    
    dictionary = {}
    
    with open(filename, mode="rt") as student_csv:
        
            
        reader = csv.reader(student_csv)
            
        next(reader)
            
        for students in reader:
                
            if len(students) != 0:
                    
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = students[key_column_index]
                    
                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = students
   
    # Return the dictionary.                 
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()