class Item(object):
    def __init__(self, name):
        self.name = name

    def sell(self):
        print("You sold the %s" % self.name)


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


axe = Weapon("Axe", 20)
axe.sell()