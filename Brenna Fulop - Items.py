class Room(object):
    def __init__(self, items = None):
        self.items = items


class Person(object):
    def __init__(self, items = None):
        if items is None:
            items = []
        self.inventory = items
        self.cloak_slot = None
        self.helm = None

    def equip(self, item):
        if isinstance(item, Helmet):
            self.helm = item
            item.put_on()
        elif isinstance(item, Cloak):
            self.cloak_slot = item
            item.put_on()


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def picked_up(self, person, room):
        room.inventory.remove(self)
        person.inventory.append(self)


class Pebble(Item):
    def __init__(self, name, description):
        super(Pebble, self).__init__("Pebble", "A small blue pebble. It has a strange gleam to it.")


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
        super(Sword, self).__init__('Sword', 'An old rusted sword, it appears fairly dull.', 15)


class Knife(Melee):
    def __init__(self, name, description, damage):
        super(Knife, self).__init__('Knife', 'A small sharp knife.', 10)


class ElvenSword(Sword):
    def __init__(self, name, description, damage):
        super(ElvenSword, self).__init__('Elven sword', 'A very sharp Elven sword. It has jewels in the handle.', 20)


class Ranged(Weapon):
    def __init__(self, name, description, damage, distance):
        super(Ranged, self).__init__(name, description, damage)


class Bow(Ranged):
    def __init__(self, name, description, damage, distance):
        super(Bow, self).__init__('Bow', 'A wooden bow. It appears to be in pretty good shape.', 15, 30)


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


class Cloak(Wearable):
    def __init__(self, name, description):
        super(Cloak, self).__init__('Desert Cloak', 'A cloak that would protect you from the forces of the desert')


class Helmet(Wearable):
    def __init__(self, name, description):
        super(Helmet, self).__init__('Helmet', 'A slightly rusty helmet, it appears strong despite its wear.')


class Container(Item):
    def __init__(self, name, description, items=None):
        super(Container, self).__init__(name, description)
        if items is None:
            items = []


class Bottle(Container):
    def __init__(self, name, description):
        super(Bottle, self).__init__('Bottle', 'A clear glass bottle')


class Chest(Container):
    def __init__(self, name, description):
        super(Chest, self).__init__('Chest', 'A large wooden chest.')


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
