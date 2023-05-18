numbers = [1,34,56,9,39.4,78,90]

running_total = 0

for total_num in numbers:
    running_total += total_num
    #Or we can say 
    #running_total = running_total + total_num 
    #We will staill get same result
print("The total number is {:,.2f}".format(running_total))