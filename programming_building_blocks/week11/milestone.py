#Still working with files 

#---STEPS IN SOLVING THIS ---- BELOW

# STEP 1. OPENING THE FILE "LIFE-EXPENTENCY.CSV" FIRST WITH A COMMAND OPEN()
# STEP 2. OMMITING THE FIRST LINE IN THE FINE SO WE CAN LOOP THROUHT THE DATA
# STEP 3. LOOPING THROUGH EACH DATA IN THE ITEM
# STEP 4. STRIPING OFF WHITE SPACE OF EACH DATA LOOPED 
# STEP 5. SPLITIG THE DATA INTO SEPERATE LIST OF LOOPED DATA: EXAMPLE BELOW
#         ['Albania', 'ALB', '1974', '68.343']
#         ['Albania', 'ALB', '1975', '68.736']
#         ['Albania', 'ALB', '1976', '69.11']
# STEP 6. SETTING THE DATA INTO DIFFERENT COLUMNS BY SETTING VARABLE TO HOLD THE DATA INDEX
# STEP 7. APPENING THE LOOPED DATA COLUMN OF LIFE_EXP INTO A LIST CALLED: WORLD_RANGE
#         SO WE CAN GET THE MINIMUM DATA AVOIDING ITERATING ERRORS AS MIN() FUNCTION
#         DOES NOT REQUIRE ITERATION(LOOP)
# STEP 8. FINDING THE MAX VALUE: 
#         SETTING MAX VALUE TO -1 OR 0 AS A VARIABLE 
# STEP 9. LOOPING THROUGH THE LIST CALLED WORLD_RANGE THAT HOLDS THE VARIABLE LIFE_EXP COLUMN
#         TO FIND THE MAX VALUE
# STEP 10. PRINT THE RESULTS 
        
print()
print("--METHOD 1--SOLVING")
print()
       
# STEP 1
with open("life-expectancy.csv") as world_data:
# STEP 2
    world_data.readline()
    world_range = []
# STEP 3 
    for data in world_data: 
# STEP 4
        data = data.strip()
# STEP 5
        data = data.split(",")
# STEP 6
        country = data[0]
        code = data[1]
        year = int(data[2])
        life_exp = float(data[3])
# STEP 7.
        #apending life_exp into world_range list to avoid iterating error
        world_range.append(life_exp)
# STEP 8.
    max_num = -1
# STEP 9
    for number in world_range:
        if number > max_num:
            max_num = number
# STEP 10.         
print("The overall max life expectency is: {}".format(max_num))
print("The overall min life expectency is: {}".format(min(world_range)))

#Or 
#print(max(world_range))     

print()
print("---METHOD 2-----BELOW---")
#---A SECOND CODING METHOD TO SOLVE THIS ARRIVING WITH SAME ANSWER---

#Still working with files-----

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
print("The Overall min life expectany is: {}. ".format(min_value))
print()





