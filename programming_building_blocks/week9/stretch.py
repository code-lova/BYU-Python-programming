#A shopping cart program where the user 
#is shown a menu and picks for it 
#Option to add item to cart
#Options to view items in cart 
#Options to remove items from cart 
#option to compute total amount of items in cart


shopping_cart = []
price = []

end_program = "Thank You, Good Bye.!!"
option = 0
cart_item = 1
running_total = 0


while option != cart_item:
    print()
    print("Please select one of the follwoing:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print()
    #First we try to verify if the user enters a digit from the menu using the try block
    try: 
        option = int(input("Please enter an option: "))
        if option == 1:
            print()
            print("What item would you like to add?:",end=" ")
            cart_item = str(input(""))
            print("What is the price of '{}'?:".format(cart_item), end=" ")
            item_price = float(input(""))
            cart_item = cart_item.title()
            shopping_cart.append(cart_item)#Adding item to shopping cart list
            price.append(item_price)# Adding price of item to price list 
            print("'{}' has been added to your cart".format(cart_item))
        else:
            if option == 2:
                if shopping_cart == []:
                    print("Your Cart is empty, add items to cart.")
                else:
                    print("The content of the shopping cart are: ")
                #Looping through the both list (shopping list and item price list)
                #Displaying each item in th shopping list with index number, item and price          
                for index, items_in_cart in enumerate(shopping_cart,1):
                    i = price[index-1]
                    print("{}. {} - ${:,.2f} ".format(index, items_in_cart, i))
                    
            elif option == 3:
                if shopping_cart == []:
                    print("Your Cart is empty.")
                else:
                    print("Which item will you like to remove?:",end=" ")
                    del_item = int(input(""))
                try: #Try to see if item num is on the list or its a digit
                    del shopping_cart[del_item-1]
                    del price[del_item-1]
                    print()
                    print("Item Has Been Removed. Cart Updated")
                except:
                    print()
                    print("Sorry.!! Not a valid item number")
                    
            else:
                if option == 5:
                    print(end_program)
                    break
                else:
                    if option == 4 and running_total < 1:
                        for item_amount in price:
                            running_total += item_amount
                        print("The total price in your shopping cart is: ${:,.2f}".format(running_total))
                        running_total += 1
        if running_total > 0:
            running_total = 0
    except:
        print()
        print("Please enter a digit")
        
                    
        