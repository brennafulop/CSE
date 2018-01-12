import random
player_money = 15
player_input = input("To win you gotta roll a seven. Roll the dice ... if you dare")
rolls = 0
top_balance = 15
top_round = 0

while player_money != 1:
    rolls += 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    player_roll = dice1 + dice2
    print(player_roll)
    if player_roll == 7:
        player_money += 5
        print("Alright you got me. you now have %s dollars. Roll again." % player_money)
        print("You've rolled %s times." % rolls)
        if top_balance < player_money:
            top_balance = player_money
            top_round = rolls
    else:
        player_money -= 1
        print("Ha! Nice try! Now you have %s dollars" % player_money)
        print("You've rolled %s times." % rolls)

print(player_roll)
print("Ha ha ha!!! I win, just like I knew I would...loser! I have all your money now!")
print("It took you %s tries just to lose." % rolls)
print("Your top balance was $" + str(top_balance) + " in round " + str(top_round) + ".")

