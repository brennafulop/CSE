class Room(object):
    def __init__(self, items=None):
        self.items = items


class Person(object):
    def __init__(self, items=None):
        self.inventory = items
        self.cloak_slot = None
        self.helm = None

    def pick_up(self, item, room):
        room.items.remove(item)
        self.inventory.append(item)

    def equip(self, item):
        if isinstance(item, Helmet):
            self.helm = item
            item.put_on()
        elif isinstance(item, Cloak):
            self.cloak_slot = item


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def picked_up(self, person, room):
        room.items.remove(self)
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
        super(Sword, self).__init__(name, description, damage)


class Knife(Melee):
    def __init__(self, name, description, damage):
        super(Knife, self).__init__(name, description, damage)


class Ranged(Weapon):
    def __init__(self, name, description, damage, distance):
        super(Ranged, self).__init__(name, description, damage)
        self.distance = distance


class Bow(Ranged):
    def __init__(self, name, description, damage, distance):
        super(Bow, self).__init__(name, description, damage, distance)


class Wearable(Item):
    def __init__(self, name, description):
        super(Wearable, self).__init__(name, description)
        self.wearing = False

    def put_on(self):
        if not self.wearing:
            self.wearing = True
            print("You are wearing the %s" % self.name)
        else:
            self.wearing = False


class Helmet(Wearable):
    def __init__(self, name, description):
        super(Helmet, self).__init__(name, description)
        
        
class Cloak(Wearable):
    def __init__(self, name, description):
        super(Cloak, self).__init__(name, description)


class Container(Item):
    def __init__(self, name, description, items=None):
        super(Container, self).__init__(name, description)
        if items is None:
            items = []
        self.inventory = items


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)


class Food(Consumable):
    def __init__(self, name, description, nutrients):
        super(Food, self).__init__(name, description)
        self.nutrients = nutrients


class Liquid(Consumable):
    def __init__(self, name, description):
        super(Liquid, self).__init__(name, description)


tester = Person([])
desert_cloak = Cloak('Desert Cloak', '8')
tester.cloak_slot = desert_cloak
tester.equip(desert_cloak)

elven_sword = Sword('Elven Sword', 'An expensive looking sword. It is sharp, with jewels in the handle', 20)
tester_room = Room([elven_sword])
print(tester_room.items[0].name)
