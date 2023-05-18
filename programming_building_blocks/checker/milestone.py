with open('life-expectancy.csv') as life_expectancy_values:
    next(life_expectancy_values)
    # the next function tells python to skip to the next line of code.

    life_expect_range = []
    for line in life_expectancy_values:
        parts = line.strip()
        parts = line.split(',')
        # print(parts)

        # country = parts[0]
        # code = parts[1]
        # year = parts[2]
        # life_exp = float(parts[3])
        # life_expect_range.append(life_exp)


        life_expect_range.append(parts)


    max_value = -1
    max_vvalue_2 = -1
    max_country = ''
    max_year = ''
    min_value = float(parts[3])
    min_value_2 = float(parts[3])
    min_country = ''
    min_year = ''
    year_to_check = int(input('Enter the year of interest? '))
    average = 0
    average_life_expectancy = 0
    average_list = []
    maximum_year = ''
    maximum_country = ''
    maximum_value = -1
    minimum_value = float(parts[3])
    minimum_country = ''


    for item in life_expect_range:
        country_name = item[0]
        country_code = item[1]
        country_year = int(item[2])
        country_value = float(item[3])

        if country_value > max_value:
        # This is the new max
            max_value = country_value
            max_country = country_name
            max_year = country_year

        if country_value < min_value:
            min_value = country_value
            min_country = country_name
            min_year = country_year
    

        if country_year == year_to_check:
            if country_value > max_value:

            # average_list.append(country_value)
            # for number in average_list(average_list)

            # if country_value > maximum_value:
            #     maximum_value = country_value
            #     maximum_country = country_name
                
            # if country_value < minimum_value:
            #     minimum_value = country_value
            #     minimum_country = country_name







    

    

#     print(f"The maximum life expectancy was in: {max_year} in {max_country}, with {max_value}. ")
#     print()
#     print(f"The minimum life expectancy was in: {min_year} in {min_country}, with {min_value}. ")
#     print()
#     print(f'for the year {year_to_check}: ')
#     print(f'the average for all country is {average_life_expectancy} ')
#     print(f'the country with the maximum life expectancy in 1959 is {maximum_country} with a value of {maximum_value} ')
#     print()
    
#     print(f'the country with the maximum life expectancy in 1959 is {minimum_country} with a value of {minimum_value} ')

# # this can also print the minimum and maximum
#     # print(min(life_expect_range))
#     # print(max(life_expect_range))
            

        