class Room(object):
    def __init__(self, items = None):
        self.items = items


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name, description,)
        self.damage = damage


class Food(Item):
    def __init__(self, name, description, nutrition):
        super(Food, self).__init__(name, description)
        self.nutrition = nutrition


class Liquid(Item):
    def __init__(self, name, description, amount):
        super(Liquid, self).__init__(name, description)
        self.amount = amount
        
class Armor(Item):
    def __init__(self, name, description):
        super(Armor, self).__init__(name, description)
