#you will write a Python program named receipt.py 
# that prints to the terminal window a receipt for a customer’s grocery order.
import csv

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
weekday = current_date_and_time.weekday()
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06



def main():
    
    PRODUCT_NUM_INDEX = 0
    QUANTITY_NUM_INDEX = 1
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    
    try:
        product_list = read_dictionary("products.csv", PRODUCT_NUM_INDEX)
        
        #print(product_list)
        
        with open("request.csv", mode="rt") as request_csv:
            
            reader = csv.reader(request_csv)
            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)
            
            #Printing the name of the store
            print()
            print(f"Inkom Emporium")
            print()
            
            # Add the number of credits to the total.
            total = 0
            #Declearing subtotal as 0
            subtotal = 0
            #Declearing Tax as 6%
            tax = 6
            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.        
            for request in reader:
                #assigning varables in request dictionary
                product_num = request[PRODUCT_NUM_INDEX]
                quantity = int(request[QUANTITY_NUM_INDEX])
                
                #finding total number of items ordered
                total += quantity
                
                #Checking if the product number is in the product dictionary
                if product_num in product_list:
                    
                    
                    #if yes then
                    #Match the record with Key to get related Data
                    data = product_list[product_num]
                    
                    #Getting the Product name from the product_list dictionary
                    product_name = data[PRODUCT_NAME_INDEX]
                    
                    #Getting the product price from the product_list dictionay
                    price = float(data[PRODUCT_PRICE_INDEX])
                    
                
                    #printing the Related record from the product_list
                    #after matching the product number from the request csv file
                    #to get product name, quantity and price
                    
                    print("{}: {} @ {} ".format(product_name, quantity, price))
                    
                   
                        
                    
                    #Finding subtotal
                    sum1 = quantity * price
                    subtotal += sum1
                        
                    sales_tax = subtotal * tax / 100 
                    total_amount = sales_tax + subtotal
                    
                    
                    
            print()
            print("Number of Items: {} ".format(total))
            print("Subtotal: ${}".format(round(subtotal, 2)))
            print("Sales Tax: ${}".format(round(sales_tax, 2)))
            print("Total: ${:.2f}".format(total_amount))
            
            print()
            print("Thank You for shopping with Inkom Emporium")
            # Use an f-string to print the current
            # day of the week and the current time.
            print(f"{current_date_and_time:%A %B %d %I:%M:%S%p %Y}")
            print()
            
            if weekday == 1 or weekday == 2:
                discount = round(subtotal * DISC_RATE, 2)
                print(f"Discount amount: ${discount:.2f}")
                subtotal -= discount

                        
                # Compute the sales tax. Notice that we compute the sales tax
                # after computing the discount because the customer does not
                # pay sales tax on the full price but on the discounted price.
                sales_tax = round(subtotal * SALES_TAX_RATE, 2)
                print(f"Sales tax amount: ${sales_tax:.2f}")

                # Compute the total by adding the subtotal and the sales tax.
                total = subtotal + sales_tax

                # Display the total for the user to see.
                print(f"Total: ${total:.2f}")
                print()
                print()
            
            print("Would you like to participate on our online survey,"\
                " so as to make our product and services better  Y/N?:", end=" ")
            answer = input("")
            if answer.lower() == "yes":
                print("Thanks for your participation, please enter your email address:", end=" ")
                email = input("")
                print("Your data has been recorded we will get across to you shortly.")
                print()
            else:
                print("Thanks for shopping with us.GOOD BYE..!!")
                print()
            
            
            
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")
        
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
        print(f"Error: line  {reader.line_num} unknown product ID in the {request_csv.name} file"
                " is formatted incorrectly.")

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
    
    with open(filename, mode="rt") as product_csv:
        
         # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(product_csv)
        
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for products in reader:
            
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(products) != 0:
                
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = products[key_column_index]
                
                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = products
                
    # Return the dictionary.
    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()
