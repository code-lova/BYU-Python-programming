# with open("life-expectancy.csv") as life_life:
#     life_list = []
#     for line in life_life:
#         line = line.strip()
#         line = line.split(",")
#         country = line[0]
#         code = line[1]
#         year = line[2]
#         life_exp = float(line[3])
#         life_list.append(life_exp)
#     # print(life_list)
#     print(min(life_list))
#     print(max(life_list))


max_price = -1

for item in shopping_cart:
    price = item[1] # The price is the second part of the item

    if price > max_price:
        # This is the new max
        max_price = price

print(f"The maximum price is: {max_price}")
