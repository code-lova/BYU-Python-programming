#Ask the user for a list of items in a
#shopping list, stop asking for items,
#When the user types "quit".

shopping_cart = []
item = ""
end_program = "quit"

opx = 1
tgg = 0

print()
print("---Enter your Item of the shopping list (type: quit to finish):--")
print()

while item != end_program:
    item = str(input("Item: "))
    item = item.lower()
    if item != "quit": 
        shopping_cart.append(item)
print()
print("The shopping list is:")
for i in shopping_cart:
    print(i)
print()

print("The Shopping list with indexes is: ")
for j, item_list in enumerate(shopping_cart):
    print("{}. {}".format(j, item_list))
print()

while opx > tgg:
    print("Which Item would you like to change? :",end=" ")
    try:
        item_update = int(input(""))
        
        print("What is the new item?:",end=" ")
        new_item = str(input(""))
        #updating the shopping list with the new item added
        shopping_cart[item_update] = new_item
    except:
        print("Invalid item number")
    tgg += 1


print()
print("The shopping list with indexes is: ")
for k, item_lists in enumerate(shopping_cart):
    print("{}. {}".format(k, item_lists))
