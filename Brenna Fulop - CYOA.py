# ITEMS
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.able_to = True

    def picked_up(self, person, room):
        if self.able_to is True:
            room.items.remove(self)
            person.inventory.append(self)
            print('You picked up the %s' % self.name)
        else:
            print("You can't pick up the %s, don't be silly." % self.name)

    def drop(self, person, room):
        if self in person.inventory:
            room.items.append(self)
            person.inventory.remove(self)
            print('You have dropped the %s' % self.name)
        else:
            print("You aren't holding the %s, and therefore can't drop it." % self.name)


class Weapon(Item):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name, description)
        self.damage = damage

    def held(self, person):
        person.damage = self.damage + person.damage


class Melee(Weapon):
    def __init__(self, name, description, damage):
        super(Melee, self).__init__(name, description, damage)


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
        self.inventory = items


class Bottle(Container):
    def __init__(self, name, description, items=None):
        super(Bottle, self).__init__(name, description)
        if items is None:
            items = []
        self.inventory = items


class Chest(Container):
    def __init__(self, name, description, items=None):
        super(Chest, self).__init__(name, description)
        self.items = items
        self.able_to = False


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)
        self.consume = False

    def consumed(self, person):
        self.consume = True
        person.inventory.remove(self)


class Food(Consumable):
    def __init__(self, name, description, nutrients):
        super(Food, self).__init__(name, description)
        self.nutrients = nutrients

    def eaten(self, person):
        person.health = person.health + self.nutrients


class Liquid(Consumable):
    def __init__(self, name, description, amount):
        super(Liquid, self).__init__(name, description)
        self.amount = amount
        self.able_to = False

    def check_for_container(self, person):
        if Bottle in person.inventory:
            self.able_to = True

    def drank(self, person):
        person.health = person.health + self.amount

# CHARACTERS


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


# ROOMS

class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.visited = False

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Spaceship
cockpit = Room("Cockpit", 'airlock', None, None, None, None, None, "You are inside your ship, in front of you are the "
               "controls. You can see two moon-sized planets through the glass in front of you. "
               "There is a small chest to your right. There is a door to the North.")
airlock = Room('Airlock', 'elandingpad', 'cockpit', "clandingpad", 'alandingpad', None, None, "You are inside your"
               " Spaceship's airlock room. Through the clear wall you can see a planet covered in trees to"
               " the north and a planet covered in sand to the west")

# Arrakis
alandingpad = Room("Arrakis Landing Pad", 'apath1', None, 'acivil', 'caveentrance', 'airlock', None, 'You are on'
                   ' Arrakis, a desert planet. To the east you see civilization, the north shows a long winding path, '
                   'and far to the west you can barely make out what appears to be a cave.')
acivil = Room('Civilization', None, None, 'ahouse', 'alandingpad', None, None, 'You reach the entrance to the '
              'civilization, which is surrounded by a large wall '
              'Rows of houses line the path. Only one appears unlocked. '
              'An old beggar in a tan cloak approaches you and asks for water.')
ahouse = Room("Arrakis Home", None, None, None, 'acivil', None, None, 'You are in a one room house. There is a table'
              ' in front of you with an old knife on it. Next '
              'to the knife there sits a small bottle of water.'
              ' On the other side of the room there is a cot.')
apath1 = Room("Open Desert", None, 'alandingpad', None, 'apath2', None, None, 'You have reached a crossroads.'
              'The path diverges to the south and west.')
apath2 = Room('Open Desert', None, 'caveentrance', 'apath1', None, 'plateau', None, 'You have reached a crossroads. '
                                                                                    'You are at the base of a very tall'
                                                                                    ' plateau, and to the south you see'
                                                                                    ' a cave. The path also diverges '
                                                                                    'to the east.')
plateau = Room('Plateau', None, None, None, None, None, 'apath2', 'You are on top of a tall plateau. You can see a'
                                                                  ' path winding through the desert to the east.'
                                                                  'To the south you see a cave. South-east reveals a '
                                                                  'large wall with rows of houses inside.')
caveentrance = Room('Cave Entrance', 'apath2', 'maze1', None, None, None, None, 'You are the entrance to a wide cave. '
                                                                                'Inside is pitch black.')
maze1 = Room('Tunnel', 'caveentrance', 'maze2', 'maze3', None, None, None, "You are inside the cave system. You can't "
                                                                           "see anything, but you can feel the walls.")
maze2 = Room('Tunnel', 'maze1', None, 'maze4', None, None, None, "You are inside the cave system You can't "
                                                                 "see anything, but you can feel the walls.")
maze4 = Room('Tunnel', 'maze2', None, None, 'oasis', None, None, 'You are inside the cave system. '
                                                                 'You see light coming from the west.')
maze3 = Room('Tunnel', 'maze2', None, None, 'maze1', None, None, "You are inside the cave system. You can't "
                                                                 "see anything, but you can feel the walls.")
oasis = Room('Oaisis', None, None, "maze4", None, None, None, "There is a large body of water and a palm tree. The air "
                                                              "is cooler here. This appears to be the only source of"
                                                              " above ground water on the entire planet.")

# Endore
elandingpad = Room('Endore Landing Pad', 'ecivil', None, None, None, 'airlock', None, 'You are on Endore, the forest '
                                                                                      'planet. You smell smoke in the'
                                                                                      ' air.')
ecivil = Room("Civilization", 'bridge1', 'elandingpad', 'ehouse', None, None, None, 'You have reached the Endore '
                                                                                    'civilization. '
              'The grass and mud huts are few and far between'
              ' and the area seems deserted. Most huts are '
              'crumbled, except one. You think you see '
              'movement inside it.')
ehouse = Room('Hut', None, None, None, 'ecivil', None, None, 'You are inside of the hut. A strange looking man with a '
                                                             'knife stands in a defensive pose in one corner, a stack'
                                                             'of dried meat sits next to him. He seems to be chanting '
                                                             'to himself under his breath, '
                                                             '"You must put the stone in the volcano."')
bridge1 = Room("Wooden bridge", 'forest', 'ecivil', None, None, None, 'river', 'You are on a fancy bridge over a wide '
                                                                               'and fast moving river.')
river = Room('River', None, None, None, None, 'bridge1', None, 'You are in the river. The water is freezing cold and it'
                                                               ' is difficult to fight the strong current. '
                                                               'This was a bad idea.')
forest = Room('Forest Path', None, 'bridge1', 'bridge2', None, 'tree', None, 'You are in the forest on a well worn path'
                                                                             '. You see something glimmer at you from'
                                                                             ' the top of a nearby tree.')
tree = Room('Tree', None, None, None, None, None, 'forest', 'You are in the highest branch of a tree. There is a '
                                                            'glimmering blue stone on the branch next to you.')
bridge2 = Room('Rope Bridge', None, None, 'mountains', 'forest', None, 'river', 'You are  on a fragile rope bridge '
                                                                                'above the'
                                                                                ' river. There are a few boards missing'
                                                                                ' and the surface is slippery. It sways'
                                                                                ' as you move across it.')
mountains = Room('Mountain Range', None, 'volcano', None, 'bridge2', None, None, 'You are in the mountain range. The '
                                                                                 'ground is rocky and uneven. Just past'
                                                                                 ' the range there is a volcano that is'
                                                                                 ' spewing smoke and ash. It seems clos'
                                                                                 'e to eruption.')
volcano = Room('Base of Volcano', 'mountains', None, None, None, 'volcanotop', None, 'You stand at the base of the '
                                                                                     'volcano. The air is hot and stuff'
                                                                                     'y, and you can barely see through'
                                                                                     ' the smoke. You hear a rumble.')
volcanotop = Room('Volcano', None, None, None, None, None, 'volcano', 'You stand at the mouth of the volcano. It is '
                                                                      'unbearably hot.')

