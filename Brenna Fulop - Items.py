class Room(object):
    def __init__(self, items = None):
        self.items = items


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


    def sell(self):
        print("You sold the %s" % self.name)

    def pick_up(self, item):



class Weapon(Item):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name, description,)
        self.damage = damage



axe = Weapon("Axe", 'A rusty axe.', 20)
room = Room([axe])
axe.sell()
