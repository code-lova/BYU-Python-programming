#example of week 12, still on file opening system

shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99],
]

#Lets find the max price of the item in the list

max_price = -1
max_product = ""

for item in shopping_cart:
    price = item[1]
    product_name = item[0] #getting the name of the item as well
    if price > max_price:
        max_price = price
        max_product = product_name
        
print("{} Has the maximum price of: {}".format(max_product, max_price))

print()
#lets look at another example add the item name and max num
#Assuming the list is not empty

numbers = [42, 25, 18, 83, 23, 85, 38, 2]
cart_items = ["apple","pear","grape","yam","lemon","orange","onion","ginger"]

largest_num = numbers[-1]
largest_item = ""

for i, number in enumerate(numbers):
    k = cart_items[i]
    if number > largest_num:
        largest_num = number
        largest_item = k
    
print("{} has the largets number of: {}".format(largest_item,largest_num))