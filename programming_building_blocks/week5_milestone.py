# This is an adventure game created by Jerry, week 5 milestone to be completed week 6
# The mission is to protect youself and your sheep without getting killed by the wolf.
# Where the user is given choices and the choices comes with a consequences.

null_value = "Invalid Choice, Try again.!!"

print("As a shephard you are on a field and its all sunny and the weather is very nice.")
print("All of a sudden a wolf attacks ? What will you do ?")
print("PROTECT or RUN ?")
beginner_choice = input("")
if beginner_choice.lower() in ("protect", "run"):
    if beginner_choice.lower() == "protect":
        print("There is a bag beside you and you looked inside, you found a MATCHET and A GUN.")
        print("which will you pick ?")
        print("A MATCHET or A GUN ?")
    else:
        print("You ran and hide behind the tractor, while the wolf attacked, killed and ate all of your sheep.")
        print("GAME OVER.!!") 
else:
    print(null_value)