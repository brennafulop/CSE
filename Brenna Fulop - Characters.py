'''
Needs:
    Name
    health
    pick up items
    move
    attack
    death
    dialogue
    perform action
    description
    status effect
    take damage
'''
class Character(object):
    def __init__(self, name, health, description, dialogue):
        self.name = name
        self.health = health
        self.description = description
        self.dialogue = dialogue
        self.holding = False
        self.death = False

    def pick_up(self):
        if self.holding:
            print('Your hands are full.')
        else:
            print('You pick up the object.')

    def attack(self):
        print('You attack.')

    def death(self):
        if self.health < 1:
            self.death = True

    def damage(self):
        self.health -= 1

cap_america = Character('Steve Rogers', 100, 'Large man in a colorful suit holding a round shield.', None)
cap_america.attack()
