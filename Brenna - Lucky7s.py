import random
player_money = 15
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
correct_roll = 7
player_roll = dice1 + dice2
player_input = input("Roll the dice...if you dare.")

print(player_roll)

while player_money != 0 and correct_roll == False:
    if player_roll == correct_roll:
        print("Alright you got me. you now have %s + 5 dollars. Roll again." % player_money)
        print("Roll again. I'll get you eventually!")
        print(player_roll)
    elif player_roll == < correct_roll:
        print("Ha! I win! Nice try.")