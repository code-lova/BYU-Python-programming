#A shopping cart program
# a program that stores a list of products in a shopping cart along with their prices. 
# The user should have the ability to add items to the list, 
# remove them, and see the total price of the cart.

print("---A program that stores a list of products in a shopping cart along with their prices.--")
print()

shopping_cart = []
price = []

end_program = "Thank You Good Bye.!!"
option = 0
cart_item = 1

print("Please select one of the follwoing:")
print("1. Add item")
print("2. View cart")
print("3. Remove item")
print("4. Compute total")
print("5. Quit\n")

while option != cart_item:
    option = int(input("Please enter an option: "))
    if option == 1:
        print("What item would you like to add?:",end=" ")
        cart_item = str(input(""))
        cart_item = cart_item.title()
        shopping_cart.append(cart_item)
        print("'{}' has been added to your cart".format(cart_item))
    else:
        if option == 2:
            print("The content of the shopping cart are: ")
            for total_item in shopping_cart:
                print(total_item)
        else:
            if option == 5:
                print(end_program)
                break
        