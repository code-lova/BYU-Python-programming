#Purpose : Simple meal price calculator

child_meal_price = float(input("What is the price of the child's meal: "))
child_drink = float(input("What is the price of child's drink: "))
adult_meal_price = float(input("what is the price of the adult's meal: "))
adult_drink = float(input("What is the price of adult_drink: "))
num_cuildren = int(input("How many children are there: "))
num_adults = int(input("How many adults are there: "))
tax = float(input("What is the sales tax rate: "))

child_md = child_meal_price * child_drink
child_sub_total = num_cuildren * child_md

adult_md = adult_meal_price * adult_drink
adult_sub_total = num_adults * adult_md

result_sub_total = child_sub_total + adult_sub_total
round_sub_total = round(result_sub_total, 2) #here i am rounding sub total to 2 decimal places
sales_tax = result_sub_total * tax / 100 
round_sales_tax = round(sales_tax, 2) #here i round sales tax to 2 decimal places

total_meal_price = result_sub_total + sales_tax
round_total_meal_price = round(total_meal_price, 2) #here i round sales tax to 2 decimal places

print(f"Subtotal: ${round_sub_total:,}") # adding , to the digits if its in thousands.
print(f"Sales Tax: ${round_sales_tax:,}")
print(f"Total: ${round_total_meal_price:,}")


payment = float(input("What is your payment amount: "))
tip = float(input("How much did you tip: "))
cus_change = payment - total_meal_price - tip
print(f"Change: ${cus_change:,.2f}") #Rouding to 2 decimal precision and adding a comma if the digits is in thousands
#Below is an alternate way to round num to 2 decimal precision and also adding a comma, if digits is in thousands
# round_change = round(cus_change, 2) 
# print(f"Change: ${round_change:,}")


