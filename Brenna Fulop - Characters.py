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
    def __init__(self, name, description, dialogue, holding, items=None):
        if items is None:
            items = []
        self.name = name
        self.health = 100
        self.description = description
        self.dialogue = dialogue
        self.holding = holding
        self.dead = False
        self.inventory = items

    def pick_up(self):
        if self.holding:
            print(" %s's hands are full." % self.name)
        else:
            print('%s picks up the object.' % self.name)

    def attack(self, target):
        print('%s attacks %s' % (self.name, target.name))
        target.damage()

    def death(self):
        if self.health <= 0:
            self.dead = True
            print('%s has died' % self.name)

    def damage(self):
        self.health -= 1
        if self.health <= 0:
            self.death()
        print('%s has %s health.' % (self.name, self.health))


cap_america = Character('Steve Rogers', 'Large man in a colorful suit holding a round shield.', None, "Shield")
iron_man = Character('Tony Stark', 'Rich man in an iron suit.', None, None)
cap_america.attack(iron_man)
iron_man.attack(cap_america)
