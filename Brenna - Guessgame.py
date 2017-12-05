# REMEMBER, INPUTS FROM USERS ARE ALWAYS (!!!)
# OF TYPE STRING!!!!

import random
correct_guess = False

winning_number = random.randint(1,50)
guesses = 5
print(winning_number)


number = int(input("Choose a number between one and fifty."))


while guesses != 0 and correct_guess == False:
    if number == winning_number:
        guesses -= 1
        print("Congrats! You win! The winning number was %d. You had %d guesses left." % (winning_number, guesses))
        correct_guess = True
    elif number > winning_number:
        guesses -= 1
        print("Your guess is too high! You only have %d guesses left!" % guesses)
        number = int(input("Guess again!"))
    elif number < winning_number:
        guesses -= 1
        print("Your guess is too low! You only have %d guesses left!" % guesses)
        number = int(input("Guess again!"))
if guesses == 0:
    print("You lose! Better luck next time!")

