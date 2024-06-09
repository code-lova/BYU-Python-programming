import random

#Load words and store them in a list
word_list = []
word_file = open("words.txt")
for word in word_file:
    word_list.append(word.strip())
    
# print(word_list)
#pick a word from the list
#storing the answer in the variable called answer
answer = random.choice(word_list)
print(answer)
num_of_guesses = 0
guess_correctly = False

while num_of_guesses < 3 and not guess_correctly:
    guess = str(input("What is yor guess: "))
    print("Your guess was not correct.")
    print("You guessed: {}".format(guess))
    guess = guess.lower()
    num_of_guesses += 1
    if guess == answer:
        guess_correctly = True
    else:
        guess_correctly = False
    
if guess_correctly:
    print("Congratulations..!! you guessed the right word")
    print("It took you {} guesses".format(num_of_guesses))
else:
    print("You used all your choices")
    

    
    