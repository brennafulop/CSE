# REMEMBER, INPUTS FROM USERS ARE ALWAYS (!!!)
# OF TYPE STRING!!!!

import random


winning_number = random.randint(1,50)
guesses = 5



number = int(input("Choose a number between one and fifty."))
if number == winning_number:
    print("Congrats! You win! The winning number was %d. You had %d guesses left." % (winning_number, guesses))
elif number > winning_number:
    guesses -= 1
    print("Your guess is too high! You only have %d guesses left!" % guesses)
elif number < winning_number:
    guesses -= 1
    print("Your guess is too low! You only have %d guesses left!" % guesses)


