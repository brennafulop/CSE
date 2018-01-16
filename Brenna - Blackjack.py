import random

deck = random.randint(1, 10)
player_cards = random.randint(2, 20)
dealer_cards = 2

if player_cards > 21:
    print ("You lose!")

while player_cards < 21:
    deck = random.randint(1,10)
    print("You have 2 cards, and they add up to " + str(player_cards))
    player_input = input("Would you like another card?")
    if player_input == "Yes":
        player_cards = player_cards + deck
        print("You pulled a " + str(deck), "that means your cards add up to " + str(player_cards))