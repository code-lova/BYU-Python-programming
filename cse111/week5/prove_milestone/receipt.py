#you will write a Python program named receipt.py 
# that prints to the terminal window a receipt for a customer’s grocery order.
import csv



def main():
    
    PRODUCT_NUM_INDEX = 0
    QUANTITY_NUM_INDEX = 1
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    
    
    product_list = read_dictionary("products.csv", PRODUCT_NUM_INDEX)
    
    print(product_list)
    
    with open("request.csv", mode="rt") as request_csv:
        
        reader = csv.reader(request_csv)
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for request in reader:
            #assigning varables in request dictionary
            product_num = request[PRODUCT_NUM_INDEX]
            quantity = request[QUANTITY_NUM_INDEX]

            #Checking if the product number is in the product dictionary
            if product_num in product_list:
                #if yes then
                #Match the record with Key to get related Data
                data = product_list[product_num]
                #Getting the Product name from the product_list dictionary
                product_name = data[PRODUCT_NAME_INDEX]
                #Getting the product price from the product_list dictionay
                price = data[PRODUCT_PRICE_INDEX]
                #printing the Related record from the product_list
                #after matching the product number from the request csv file
                #to get product name, quantity and price 
                print("{}: {} @ {} ".format(product_name, quantity, price))


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
