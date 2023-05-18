#FINDING THE CURRENT DENTAL OFICE THAT HAS MORE PATIENCE 

import csv

COMPANY_NAME_INDEX = 0
EMPLOYEE_NUM_INDEX = 3
PATIENCE_NUM_INDEX = 4

def main():
    # Open a file named dentists.csv and store a reference
    # to the opened file in a variable named dentist_list.
    with open("dentists.csv", mode="rt") as dentist_list:
    
        # Use the csv module to create a readme variable
        # object that will read from the opened file.
        readme = csv.reader(dentist_list)
    
        # The first row of the CSV file contains column
        # headings and not data about a dental office,
        # so this statement skips the first row of the
        # CSV file.
        next(readme)
        
        number_of_patience = 0
        most_company = ""
        
        # Read each row in the CSV file one at a time.
        # The reader object returns each row as a list.
        for row_list in readme:
            #print(row_list)
            
            # For the current row, retrieve the
            # values in columns 0, 3, and 4.
            company = row_list[COMPANY_NAME_INDEX]
            num_of_employee = int(row_list[EMPLOYEE_NUM_INDEX])
            num_of_patience = int(row_list[PATIENCE_NUM_INDEX])
            
            #print(company, num_of_employee, num_of_patience)
            
            # Compute the number of patients per
            # employee for the current dental office.
            patience_per_empoyee = num_of_patience / num_of_employee
            
            # If the current dental office has more
            # patients per employee than the running
            # maximum, assign number_of_patience and most_company
            # to be the current dental office. 
            
            if patience_per_empoyee > number_of_patience:
                number_of_patience = patience_per_empoyee
                most_company = company
                
        print("{} has {:.1f} patience per emloyee".format(most_company, number_of_patience))
        
if __name__ == "__main__":
    main()  