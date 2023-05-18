#Still working with files 

with open("life-expectancy.csv") as world_data:
    world_data.readline()
    the_life_exp_range = []
    country_name = []
    year_value = []
    
    for i in world_data:
        i = i.strip()
        world_h = i.split(",")
        
        the_life_exp_range.append(world_h)
        
    max_value = -1
    max_vvalue_2 = -1
    max_country = ''
    max_year = ''
    min_value = float(world_h[3])
    min_value_2 = float(world_h[3])
    min_country = ''
    min_year = ''
    year_to_check = int(input('Enter the year of interest? '))
    
    average_list = []
    maximum_year = ''
    maximum_country = ''
    maximum_value = -1
    minimum_value = float(world_h[3])
    minimum_country = ''

    for exp_values in the_life_exp_range:
        country_name = exp_values[0]
        country_code = exp_values[1]
        country_year = int(exp_values[2])
        country_value = float(exp_values[3])
        
        if country_value > max_value:
            max_value = country_value
            max_country = country_name
            max_year = country_year
            
        elif country_value < min_value:
            min_value = country_value
            min_country = country_name
            min_year = country_year
        
        elif year_to_check == country_year:
            average_list.append(country_value)
            for numbers in average_list:
                
                length = len(country_value)
                total = sum(country_value)
                average = total / length
            
            if country_value > maximum_value:
                maximum_value = country_value
                maximum_country = country_name
            else:
                if country_value < minimum_value:
                    minimum_value = country_value
                    minimum_country = country_name
                    
            
            
print("The Overall max life expectany is: {} from {}, in {}. ".format(max_value, max_country, max_year))
print()
print("The Overall min life expectany is: {} from {}, in {}. \n".format(min_value, min_country, min_year))
print("For the year {}".format(year_to_check))
print("The average life expentency accross all countries was {:,.2f}".format(average))
print("The max life expetency was in {} with {:,.2f}".format(maximum_country, maximum_value))
print("The min life expetency was in {} with {}".format(minimum_country, minimum_value))
print()


