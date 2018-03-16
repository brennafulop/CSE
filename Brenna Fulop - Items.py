class Room(object):
    def __init__(self, items = None):
        self.items = items


class Person(object):
    def __init__(self, items = None):
        if items is None:
            items = []
        self.inventory = items


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def picked_up(self, person, room):
        room.inventory.remove(self)
        person.inventory.append(self)


class Weapon(Item):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name, description)
        self.damage = damage

class Melee(Weapon):
    def __init__(self, name, description, damage):
        super(Melee, self).__init__(name, description, damage)
        self.damage = damage


class Sword(Melee):
    def __init__(self, name, description, damage):
        super(Sword, self).__init__(name, description, 10)


class Knife(Melee):
    def __init__(self, name, description, damage):
        super(Knife, self).__init__(name, description, 10)


class ElvenSword(Sword):
    def __init__(self, name, description, damage):
        super(ElvenSword, self).__init__(name, description, 15)


class Ranged(Weapon):
    def __init__(self, name, description, damage, distance):
        super(Ranged, self).__init__(name, description, damage)


class Bow(Ranged):
    def __init__(self, name, description, damage, distance):
        super(Bow, self).__init__('Bow', description, 15, 30)


class Wearable(Item):
    def __init__(self, name, description):
        super(Wearable, self).__init__(name, description)
        self.wearing = False

    def put_on(self):
        if self.picked_up():
            self.wearing = True


class Container(Item):
    def __init__(self, name, description):
        super(Container, self).__init__(name, description)


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)


class Food(Consumable):
    def __init__(self, name, description, nutrients):
        super(Food, self).__init__(name, description)


class Dried_Meat(Food):
    def __init__(self, name, description, nutrients):
        super(Dried_Meat, self).__init__(name, description, 10)


class Lembas(Food):
    def __init__(self, name, description, nutrients):
        super(Lembas, self).__init__(name, description, 5)


class Liquid(Consumable):
    def __init__(self, name, description):
        super(Liquid, self).__init__(name, description)


class Water(Liquid):
    def __init__(self, name, description):
        super(Water, self).__init__(name, description)
