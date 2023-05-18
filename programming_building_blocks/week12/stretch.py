#Still working with files
#Prove assignment opeing files

#Declearing empty strings
country_list = []
country_code_list = []
year_list = []
value_list = []

with open("life-expectancy.csv") as world:
    world.readline()
    for world_data in world:
        world_data = world_data.split(",")
        #print(world_data)
        
        country = str(world_data[0].strip())
        code = str(world_data[1].strip())
        year = int(world_data[2].strip())
        value = float(world_data[3].strip())
        #print(value)
        
        country_list.append(country)
        country_code_list.append(code)
        year_list.append(year)
        value_list.append(value)
        

max_exp = -1
max_country = ""
max_year = ""

min_exp = value
min_country = ""
min_year = ""

for i, exp_value in enumerate(value_list):
    the_country_name = country_list[i]
    the_country_year = year_list[i]
    if exp_value > max_exp:
        max_exp = exp_value
        max_country = the_country_name
        max_year = the_country_year
    else:
        if exp_value < min_exp:
            min_exp = exp_value
            min_country = the_country_name
            min_year = the_country_year
        
print()
print("The overall max life expentency is: {} from {} in {}".format(max_exp,max_country,max_year))
print("The overall min life expentency is: {} from {} in {}".format(min_exp,min_country,min_year))
print()

max_exp2 = -1
max_country2 = ""
max_year2 = ""

min_exp2 = value
min_country2 = ""
min_year2 = ""

avg_list = []

empty = ""
choice = ""

#while the user choice is not empty do this bollod of code else loop
while choice == empty:
    try:
        print("Enter a year of interest: ",end="")
        choice = int(input(""))
    
        for j, any_year in enumerate(year_list):
            the_country_name = country_list[j]
            the_country_year = year_list[j]
            the_country_value = value_list[j]
            #checking if the user input is with the year.
            if any_year == choice:
                if the_country_value > max_exp2:
                    max_exp2 = the_country_value
                    max_country2 = the_country_name
                    max_year2 = the_country_year
                else:
                    if the_country_value < min_exp2:
                        min_exp2 = the_country_value
                        min_country2 = the_country_name
                        min_year2 = the_country_year
                #finding the average life expentency in that year 
                avg_list.append(the_country_value) #appending the country value in a list first 
                length = len(avg_list)
                total = sum(avg_list)
                avg = total / length

        print()
        print("The average life expentency across all countries was {:,.2f}".format(avg))
        print("The max life expentency was in {} with {}".format(max_country2,max_exp2))
        print("The min life expentency was in {} with {}".format(min_country2,min_exp2))
    except:
        print()
        print("Not a valid year or value")
        print()
print()

print()


max_exp3 = -1
max_country3 = ""
max_year3 = ""

min_exp3 = value
min_country3 = ""
min_year3 = ""

average = []
avgg = ""
that_country = ""

empty = ""
country_choice = ""

#while the user choice is not empty do this bollod of code else loop
while country_choice == empty:
    try:
        print("Enter a country of interest: ",end="")
        country_choice = str(input(""))
        country_choice = country_choice.lower()

        for k, any_country in enumerate(country_list):
            any_country = any_country.lower()
            the_country_name = country_list[k]
            the_country_value = value_list[k]
            the_country_year = year_list[k]

            
            #checking if the user input is with the year.

            if any_country == country_choice:
                that_country = any_country.title()
                if the_country_value > max_exp3:
                    max_exp3 = the_country_value
                    max_country3 = the_country_name
                    max_year3 = the_country_year
                else:
                    if the_country_value < min_exp3:
                        min_exp3 = the_country_value
                        min_country3 = the_country_name
                        min_year3 = the_country_year
                            
                #finding the average life expentency in that year 
                average.append(the_country_value) #appending the country value in a list first 
                length = len(average)
                total = sum(average)
                avgg = total / length
        
        print()
        print("The average life expentency across {} was {:,.2f}".format(that_country, avgg))
        print("The max life expentency in {} with {}".format(max_country3,max_exp3))
        print("The min life expentency in {} with {}".format(min_country3,min_exp3))

    except:
        print("Sorry..!! Not a valid country")

print()


        
        
        