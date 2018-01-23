import random
import string

"""

This is a guide of how to make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Take in a letter and add it to a list of letters_guessed
4. Hide and reveal letters
5. Create win and lose condition

"""

word_bank = ['forest', 'melancholy', 'pluto', 'strange', 'infinity', 'goodbye', 'river', 'interestingly', 'canada',
             'fascinating']
guesses_left = 10

random_word = random.choice(word_bank)
list_word = list(random_word)
print(list_word)

hidden_word = list("*" * len(list_word))
print(hidden_word)
print("The word is " + str(len(list_word)), "letters long.")
print(string.ascii_lowercase)

guesses = []

while guesses_left > 0:
    current_guess = input("Guess a letter >_")
    guesses.append(current_guess)
    print(guesses)
    output = []
    if current_guess == 'quit':
        exit(0)
    for letter in random_word:
        if letter in guesses:
            output.append(letter)
        else:
            output.append('*')
    print(output)

