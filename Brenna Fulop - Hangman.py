import random
import string
"""
This is a guide of how to make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Hide the word (use *)
4. Reveal letters based on input
5. Create win and lose condition
"""

word_bank = ['forest', 'melancholy', 'pluto', 'strange', 'infinity', 'goodbye', 'river', 'interestingly', 'canada',
             'fascinating']

random_word = random.choice(word_bank)
list_word = list(random_word)
print(list_word)
hidden_word = list("*" * len(list_word))
print(hidden_word)
print("The word is " + str(len(list_word)), "letters long.")
print(string.ascii_lowercase)
user_input = input("Guess a letter >_")
list_word.index(user_input)
