can_ride = False

first_person_age = int(input("What is the age of the first person: "))
first_person_height = int(input("What is the height of the first person: "))
another_rider = input("Is there a second rider ? Yes or No: ")

if another_rider.lower() in ("YES","yes","Yes"):
    second_person_age = int(input("What is the age of the second person: "))
    second_person_height = int(input("What is the height of the second person: "))
    
    if first_person_height < 36 or second_person_height < 36:
        can_ride = False
    else:
        if first_person_age >= 18 or second_person_age >= 18: #if either of them is 18 yrs they can ride together
            can_ride = True
        else:
            can_ride = False    
else:
    if first_person_age >= 18 and first_person_height >= 62:
        can_ride = True
    else:
        can_ride = False
    

if can_ride:
    print("Welcome to ride. Please be safe and have fun.")
else:
    print("Sorry..!! You may not ride")
    