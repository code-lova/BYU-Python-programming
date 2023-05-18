child_meal_price = float(input("What is the price of the child's meal: "))
adult_meal_price = float(input("what is the price of the adult's meal: "))
soft_drink_price = float(input("What is the price of drink's bought: "))
num_cuildren = int(input("How many children are there: "))
num_adults = int(input("How many adults are there: "))
tax = float(input("What is the sales tax rate: "))

child_sub_total = num_cuildren * child_meal_price
adult_sub_total = num_adults * adult_meal_price

result_sub_total = child_sub_total + adult_sub_total + soft_drink_price

sales_tax = result_sub_total * tax / 100 

#displaying sub total and sales tax here
print(f"Subtotal: ${result_sub_total}")
print(f"Sales Tax: ${sales_tax}") 
 

