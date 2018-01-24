import random
import string
import sys

"""

This is a guide of how to make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Take in a letter and add it to a list of letters_guessed
4. Hide and reveal letters
5. Create win and lose condition

"""

word_bank = ['Forest', 'Melancholy', 'Pluto', 'Strange', 'Infinity', 'Goodbye', 'River', 'Interestingly', 'Canada',
             'Fascinating']
guesses_left = 10
random_word = random.choice(word_bank)
list_word = list(random_word)

print('*' * len(random_word))
print("The word is " + str(len(list_word)), "letters long.")
print("You have 10 guesses.")

guesses = []

while guesses_left > 0:
    current_guess = input("Guess a letter >_")
    guesses.append(current_guess)
    if current_guess == 'quit':
        exit(0)
    if current_guess not in random_word:
        guesses_left -= 1
    print("You have %s guesses left" % guesses_left)
    output = []
    for letter in random_word:
        if letter in guesses:
            output.append(letter)
        else:
            output.append('*')
    output = ''.join(output)
    if '*' not in output:
        print('You win! The word was %s' % random_word)
        sys.exit()
    print(output)

print('You lose! The word was %s' % random_word)