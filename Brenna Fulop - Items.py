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

hm = Item("HH", "hh")
HHHHH = Room([hm])
print(HHHHH.items[0].name)