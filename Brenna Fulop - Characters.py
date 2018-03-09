

class Character(object):
    def __init__(self, name, description, dialogue, items=None):
        if items is None:
            items = []
        self.name = name
        self.health = 5
        self.description = description
        self.dialogue = dialogue
        self.dead = False
        self.inventory = items

    def attack(self, target):
        print('%s attacks %s' % (self.name, target.name))
        target.damage()

    def death(self):
        if self.health <= 0:
            self.dead = True
            print('%s has died' % self.name)

    def damage(self):
        self.health -= 1
        if self.health >= 1:
            print('%s has %s health.' % (self.name, self.health))
        else:
            self.death()


cap_america = Character('Steve Rogers', 'Large man in a colorful suit holding a round shield.', '"You chose the wrong'
                                                                                                ' side."', 'shield')
iron_man = Character('Tony Stark', 'Rich man in an iron suit.', None, None)
print(cap_america.description)
print(iron_man.description)
print('Captain America is holding a %s' % cap_america.inventory)
print('Captain America says, %s ' % cap_america.dialogue)
cap_america.attack(iron_man)
iron_man.attack(cap_america)
cap_america.attack(iron_man)
cap_america.attack(iron_man)
cap_america.attack(iron_man)
cap_america.attack(iron_man)
