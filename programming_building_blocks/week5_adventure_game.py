# This is an adventure game created by Jerry 
# The mission is to protect youself and your sheep without getting killed by the wolf.
# Where the user is given choices and the choices comes with a consequences.
# IN the program the user is given 3 chance to try again even if the user
# Input the wrong answer to the question asked 
# After the three chances have been exhasted the game is over and have to start over again

null_value = "Invalid Choice, Try again.!!"
choice_count = 0
choice_limit = 3
out_of_choice = 0


print("As a shephard you are on a field and its all sunny and the weather is very nice.")
print("All of a sudden a wolf attacks ? What will you do ?")
print("PROTECT or RUN ?")
beginner_choice = input("")
while beginner_choice.lower() not in ("protect","run") and out_of_choice == 0: #Loop the user choice for the right answer
    if choice_count < choice_limit:
        print(null_value)
        print("")
        print("As a shephard you are on a field and its all sunny and the weather is very nice", end='.')
        print(" All of a sudden a wolf attacks ? What will you do ?")
        print("PROTECT or RUN ?")
        beginner_choice = input("")
        choice_count = choice_count + 1 # for every wrong aswer add 1 to the choice count
    else:
        out_of_choice = 1 # setting out_of_choice to 1 after user have exhausted choice count
        
if out_of_choice == 1:
    print("Oops..!! You ran out of choice, GAME OVER..!!") # If User out_of_choice is set to 1 GAME OVER !!
else:
    if beginner_choice.lower() == "protect":
        print("There is a bag beside you and you looked inside, you find a MATCHET and A GUN", end='. ')
        print("which will you pick ?")
        print("A MATCHET or A GUN")
        first_decision = input("")
        while first_decision.lower() not in ("a matchet","a gun","matchet","gun") and out_of_choice == 0:
            if choice_count < choice_limit:
                print(null_value)
                print("")
                print("There is a bag beside you and you looked inside, you find a MATCHET and A GUN", end='. ')
                print("which will you pick ?")
                print("A MATCHET or A GUN ?")
                first_decision = input("")
                choice_count = choice_count + 1
            else:
                out_of_choice = 1
        if out_of_choice == 1:
            print("Oops..!! Out of choice, GAME OVER..!!")
        else:
            if first_decision.lower() in ("a gun","gun"):
                print("You picked the gun but there was no bullet inside, you looked inside the bag and", end=' ')
                print("found a bullet, but the wolf was getting closer.")
                print("what will you do ?")
                print("LOAD GUN, RUN or FIGHT ?")
                second_decision = input("")
                while second_decision.lower() not in ("load gun","run","fight") and out_of_choice == 0:
                    if choice_count < choice_limit:
                        print(null_value)
                        print("")
                        print("You picked the gun but there was no bullet inside, you looked inside the bag and",end=' ')
                        print("found a bullet, but the wolf was getting closer.")
                        print("what will you do ?")
                        print("LOAD GUN, RUN or FIGHT ?")
                        second_decision = input("")
                        choice_count = choice_count + 1
                    else:
                        out_of_choice = 1
                if out_of_choice == 1:
                    print("Oops..!! Out of choice, GAME OVER..!!")
                else:
                    if second_decision.lower() == "load gun":
                        print("You about to load the gun but it was too late and the wolf got to you",end=' ')
                        print("before you could load the gun.")
                        print("SORRY..!! GAME OVER.")
                    elif second_decision.lower() == "run":
                        print("You dropped the gun and ran for your life,",end=' ')
                        print("while the wolf attacked and killed your sheep.")
                        print("SORRY..!! GAME OVER.")
                    elif second_decision.lower() == "fight":
                        print("You attacked the wolf with your bare hands, but unfortunately you were severely injured",end=' ')
                        print("and was eventually killed.")
                        print("SORRY..!! GAME OVER.")
                    else:
                        print(null_value)
            else:
                print("You took the matchet from the bag, to attack the wolf, there was a fight",end=' ')
                print("but you were able to overcome the wolf.")
                print("HURRAY..!! YOU WON.")
    else:
        print("You ran and hide behind the tractor, while the wolf attacked, killed and ate all of your sheep.")
        print("GAME OVER.!!")
