import random

"""

This is a guide of how to make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Take in a letter and add it to a list of letters_guessed
4. Hide and reveal letters
5. Create win and lose condition

"""

word_bank = ['Forest', 'Melancholy', 'Pluto', 'Strange', 'Infinity', 'Goodbye', 'Inconceivable', 'Interestingly', 'Canada',
             'Fascinating']
def hangman():

    guesses_left = 10
    random_word = random.choice(word_bank).lower()
    list_word = list(random_word)

    print('*' * len(random_word))
    print("The word is " + str(len(list_word)), "letters long.")
    print("You have 10 guesses.")
    print('Getting too hard for you? Type "quit"')
    guesses = []

    while guesses_left > 0:
        current_guess = input("Guess a letter >_").lower()
        guesses.append(current_guess)
        if current_guess == 'quit':
            quitting = input("Quitting already? Are you sure? (y/n)").lower()
            if quitting == 'y':
                print("The word was %s. You were so close!" % random_word)
                again = input('Would you like to play again?(y/n)').lower()
                if again == 'y':
                    hangman()
                else:
                    exit(0)
            else:
                guesses_left +=1
        if current_guess not in random_word:
            guesses_left -= 1
        print("You have %s guesses left" % guesses_left)
        print("You have already guessed these letters: %s" % guesses)
        output = []
        for letter in random_word:
            if letter in guesses:
                output.append(letter)
            else:
                output.append('*')
        output = ''.join(output)
        if '*' not in output:
            print('You win! The word was %s' % random_word)
            again = input('Would you like to play again?(y/n)').lower()
            if again == 'y':
                hangman()
            else:
                exit(0)
        print(output)

    print('You lose! The word was %s' % random_word)

    again = input('Would you like to play again?(y/n)').lower()
    if again == 'y':
        hangman()
    else:
        exit(0)


hangman()
