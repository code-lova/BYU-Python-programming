can_ride = False

first_person_age = int(input("What is the age of the first person: "))
first_person_height = int(input("What is the height of the first person: "))

if first_person_age >= 12 and first_person_age < 18:
    gold_ticket1 = input("Does this rider have a golden Passport: Yes or No: ")
    another_rider = input("Is there a second rider ? Yes or No: ")

    if another_rider.lower() in ("YES","yes","Yes"):
        second_person_age = int(input("What is the age of the second person: "))
        second_person_height = int(input("What is the height of the second person: "))
        
        if second_person_age >= 12 and second_person_age < 18:
            gold_ticket2 = input("Does this rider have a golden Passport: Yes or No: ")

            if first_person_height < 36 or second_person_height < 36:
                can_ride = False
            else: #at least one is an adult
                if first_person_age >= 18 or second_person_age >= 18 or gold_ticket1.lower() in ("YES","Yes","yes") or gold_ticket2.lower() in ("YES","Yes","yes"):
                    can_ride = True
                else:
                    #neither is an adult
                    if first_person_age >= 12 and first_person_height >= 52 and second_person_age >= 12 and second_person_height >= 52:
                        can_ride = True
                    elif (first_person_age >= 16 and second_person_age >= 14) or (first_person_age >=14 and second_person_age >= 16):
                        can_ride = True
                    else:
                        can_ride = False        
    else:
        if (first_person_age >= 18 or gold_ticket1.lower() in ("YES","Yes","yes") and first_person_height >= 62):
            can_ride = True
        else:
            can_ride = False

if can_ride:
    print("Welcome to ride. Please be safe and have fun.")
else:
    print("Sorry..!! You may not ride")
    
        
