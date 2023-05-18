#Still working with files 

with open("life-expectancy.csv") as world_datas:
    world_datas.readline()
    
    #An empty list to place the country_value float numbers so we can find
    #The min and max to avoid looping ordinarily just like that.
    the_life_exp_range = []
    
    for data in world_datas:
        data = data.strip()
        data = data.split(",")
        
        the_life_exp_range.append(data)
        
    max_value = 0    
    min_value = float(data[3])
    

    for exp_values in the_life_exp_range:
        country_name = exp_values[0]
        country_value = float(exp_values[3])
        
        if country_value > max_value:
            max_value = country_value
        else:
            if country_value < min_value:
                min_value = country_value
          
#displaying all the reslts of min and max life expentency
print()         
print("The Overall max life expectany is: {}. ".format(max_value))
print()
print("The Overall min life expectany is: {}. ".format(min_value))





       
