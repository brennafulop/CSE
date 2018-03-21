class Room(object):
    def __init__(self, items=None):
        self.items = items


class Person(object):
    def __init__(self, health, damage, thirsty, items=None):
        self.inventory = items
        self.cloak_slot = None
        self.helm = None
        self.health = health
        self.damage = damage
        self.thirsty = thirsty

    def pick_up(self, item, room):
        room.items.remove(item)
        self.inventory.append(item)

    def equip(self, item):
        if isinstance(item, Wearable):
            self.helm = item
            item.put_on()
        elif isinstance(item, Wearable):
            self.cloak_slot = item
            item.put_on()

    def attack(self, target):
        target.health = target.health - self.damage
        print(target.health)


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

    def held(self, person):
        person.damage = self.damage + person.damage


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
    def __init__(self, name, description, protection):
        super(Wearable, self).__init__(name, description)
        self.wearing = False
        self.protection = protection

    def put_on(self):
        if not self.wearing:
            self.wearing = True
            print("You are wearing the %s" % self.name)
        else:
            self.wearing = False

    def protecting(self, person):
        if self.wearing:
            person.health = person.health + self.protection

class Cloak(Wearable):
    def __init__(self, name, description, protection):
        super(Cloak, self).__init__(name, description, protection)


class Helmet(Wearable):
    def __init__(self, name, description, protection):
        super(Helmet, self).__init__(name, description, protection)


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

    def eaten(self, person):
        person.health = person.health + self.nutrients

class Liquid(Consumable):
    def __init__(self, name, description):
        super(Liquid, self).__init__(name, description)


elven_sword = Sword('Elven Sword', 'An expensive looking sword. It is sharp, with jewels in the handle', 20)
tester = Person(50, 10, [elven_sword])
tester2 = Person(50, 10, [])
lembas = Food('Lembas', 'Dry, but filling', 20)
desert_cloak = Wearable('Desert Cloak', '8', 20)
tester.wearable_slot1 = desert_cloak
tester.equip(desert_cloak)
tester_room = Room([])
print(tester.damage)
elven_sword.held(tester)
print(tester.damage)
tester.attack(tester2)
lembas.eaten(tester2)
print(tester2.health)
print(tester.health)
print(desert_cloak.wearing)
