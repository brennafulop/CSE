import random
import sys

deck = {}
deck["ace of spades"] = 1
deck['two of spades'] = 2
deck['three of spades'] = 3
deck['four of spades'] = 4
deck['five of spades'] = 5
deck['six of spades'] = 6
deck['seven of spades'] = 7
deck['eight of spades'] = 8
deck['nine of spades'] = 9
deck['ten of spades'] = 10
deck['eleven of spades'] = 10
deck['twelve of spades'] = 10
deck['thirteen of spades'] = 10
deck['ace of diamonds'] = 1
deck['two of diamonds'] = 2
deck['three of diamonds'] = 3
deck['four of diamonds'] = 4
deck['five of diamonds'] = 5
deck['six of diamonds'] = 6
deck['seven of diamonds'] = 7
deck['eight of diamonds'] = 8
deck['nine of diamonds'] = 9
deck['ten of diamonds'] = 10
deck['eleven of diamonds'] = 10
deck['twelve of diamonds'] = 10
deck['thirteen of diamonds'] = 10
deck['ace of clubs'] = 1
deck['two of clubs'] = 2
deck['three of clubs'] = 3
deck['four of clubs'] = 4
deck['five of clubs'] = 5
deck['six of clubs'] = 6
deck['seven of clubs'] = 7
deck['eight of clubs'] = 8
deck['nine of clubs'] = 9
deck['ten of clubs'] = 10
deck['eleven of clubs'] = 10
deck['twelve of clubs'] = 10
deck['thirteen of clubs'] = 10
deck['ace of hearts'] = 1
deck['two of hearts'] = 2
deck['three of hearts'] = 3
deck['four of hearts'] = 4
deck['five of hearts'] = 5
deck['six of hearts'] = 6
deck['seven of hearts'] = 7
deck['eight of hearts'] = 8
deck['nine of hearts'] = 9
deck['ten of hearts'] = 10
deck['eleven of hearts'] = 10
deck['twelve of hearts'] = 10
deck['thirteen of hearts'] = 10

player_card1 = random.choice(deck.keys())
player_card2 = random.randint(1, 10)
dealer_cards = random.randint(2, 20)
player_cards = player_card1 + player_card2

print("You have 2 cards; a " + str(player_card1), "and a " + str(player_card2), "and they add up to " + str(player_cards))

while player_cards <= 21:
    deck = random.randint(1,10)
    player_input = input("Would you like another card?")
    if player_input == "yes":
        player_cards = player_cards + deck
        print("You pulled a " + str(deck), "that means your cards add up to " + str(player_cards))
    else:
        print("The dealer's cards add up to " + str(dealer_cards))
        if dealer_cards >= player_cards:
            print("You lose")
            sys.exit()
        elif dealer_cards < player_cards:
            print("You win")
            sys.exit()

if player_cards > 21:
    print("You lose!")