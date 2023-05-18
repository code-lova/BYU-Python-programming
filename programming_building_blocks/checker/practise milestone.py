with open('life-expectancy.csv') as life_expectancy_values:
    next(life_expectancy_values)
    life_expect_range = []
    
    for line in life_expectancy_values:
        parts = line.strip()
        parts = line.split(',')
     

        country = parts[0]
        code = parts[1]
        year = parts[2]
        life_exp = float(parts[3])

        life_expect_range.append(life_exp)
     

    max_price = -1
    

    for item in life_expect_range:
        price = item
        

        if price > max_price:
        # This is the new max
            max_price = price
       
        

    print(f"The maximum price is: {max_price} ")
    print(min(life_expect_range))
    #print(max(life_expect_range))
            
