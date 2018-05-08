# ITEMS------------------------------------------------------------------------------------------------------------
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.able_to = True

    def picked_up(self, person, room):
        if self in room.inv:
            if self.able_to is True:
                person.inv.append(self)
                room.inv.remove(self)
                print('You picked up the %s' % self.name)
        else:
            print("You can't pick up the %s, don't be silly." % self.name)

    def dropped(self, person, room):
        if self in person.inv:
            room.inv.append(self)
            person.inv.remove(self)
            print('You have dropped the %s' % self.name)
        else:
            print("You aren't holding the %s, and therefore can't drop it." % self.name)


class Weapon(Item):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name, description)
        self.damage = damage


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
        self.inv = items


class Bottle(Container):
    def __init__(self, name, description, items=None):
        super(Bottle, self).__init__(name, description)
        if items is None:
            items = []
        self.inv = items
        self.full = 3

    def drink(self, person):
        if self.full > 0:
            self.full -= 1
            person.thirst = 0
            print('You drank the water. You have %s drinks left.' % self.full)


class Chest(Container):
    def __init__(self, name, description, items=None):
        super(Chest, self).__init__(name, description)
        self.inv = items
        self.able_to = False


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)
        self.consume = False

    def consumed(self, person):
        self.consume = True
        person.inv.remove(self)


class Food(Consumable):
    def __init__(self, name, description, nutrients):
        super(Food, self).__init__(name, description)
        self.nutrients = nutrients

    def eaten(self, person):
        person.hunger = person.hunger - self.nutrients
        self.consumed(person)


elven_sword = Sword('elven sword', 'An elven sword has been stuck in the ground.', 30)
broken_knife = Knife('broken knife', "The broken knife, it has been snapped, yet it is still sharp.", 15)
crystal_knife = Knife('crystal knife', "a crystal knife glimmers at you from the ground. it has been half-buried.", 25)
sturdy_bow = Bow('sturdy bow', "A sturdy wooden bow with engravings in the handle sits next to you."
                               " A quiver of arrows is next to it and seems to be charmed.", 30, 40)
desert_cloak = Cloak('desert cloak', "a tan and sturdy cloak that will protect you from the forces of the desert.", 10)
shiny_helmet = Helmet('helmet', "you see a shiny helmet shoved into the ground.", 15)
glass_bottle = Bottle('glass bottle', 'an full glass bottle shimmers from on the ground.')
space_food = Food('space food', "There is a packet of space food on the floor.", 100)
dried_meat = Food('dried meat', "On the floor there is some dried meat of unknown origin.", 65)
lembas = Food('lembas', "Kept clean by being wrapped in leaves, there are some lembas on the ground.", 60)
apple = Food('apple', 'You see a shiny red apple.', 15)
orange = Food('orange', 'There is an orange.', 15)
grapefruit = Food('grapefruit', 'There is a grapefruit.', 15)
water_bottle1 = Bottle('water bottle', 'a water bottle filled with water sits on the ground.', [])
water_bottle2 = Bottle('water bottle', 'a water bottle filled with water sits on the ground.', [])
fancy_chest = Chest('chest', 'Next to the control panel there is a wooden chest with gold accents.', [])
pebble = Item('blue pebble', 'A blue pebble glimmers at you.')

water_bottle1.full = 0
# CHARACTERS---------------------------------------------------------------------------------------------------------


class Character(object):
    def __init__(self, name, health, description, dialogue, thirst, hunger, hurt, weapon_equipped=None, items=None):
        if items is None:
            items = []
        self.name = name
        self.health = health
        self.description = description
        self.dialogue = dialogue
        self.dead = False
        self.thirst = thirst
        self.hunger = hunger
        self.hurt = hurt
        self.equipped = False
        self.winning = 0
        self.win = False
        self.weapon_equipped = weapon_equipped
        self.inv = items

    def pick_up(self, thing, room):
        thing.picked_up(self, room)

    def drop(self, thing, room):
        thing.dropped(self, room)

    def attack(self, target):
        if target is player:
            print('The %s attacks %s' % (self.name, target.name))
            target.take_damage(self)
        else:
            print('%s attack the %s' % (self.name, target.name))
            target.take_damage(self)

    def death(self):
        self.dead = True
        if self is player:
            print('You have died.')
            exit(0)
        else:
            print('The %s has died' % self.name)
            current_node.chars.remove(self)
            self.inv.append(current_node)
            pass

    def take_damage(self, enemy):
        self.health -= enemy.hurt
        if self.health >= 1:
            if self is player:
                print('%s have %s health.' % (self.name, self.health))
            else:
                print('The %s has %s health.' % (self.name, self.health))
        else:
            self.death()

    def eat(self, food):
        food.eaten(self)

    def thirsty(self):
        if self.thirst == 100:
            print('You are too thirsty to continue. You must drink water.')
        if self.thirst > 100:
            self.death()

    def hungry(self):
        if self.hunger == 100:
            print('You are too hungry to continue. You must eat something.')
        if self.hunger >= 101:
            self.death()

    def equip(self, thing):
        self.equipped = True
        self.weapon_equipped.append(thing)
        self.hurt = thing.damage + self.hurt

    def un_equip(self, thing):
        if self.equipped:
            self.equipped = False
            self.weapon_equipped.remove(thing)
            self.hurt -= thing.damage
        else:
            print('You must have something equipped to un-equip it.')

    def win(self):
        if self.winning == 2:
            self.win = True
            print('You win!')
            exit(0)


strange_man = Character('strange man', 50, 'In the corner there is a strange man '
                                           'in tattered clothing holding a broken knife. He is frightened by '
                                           'you.', '"Please, the stone, return it to the volcano.', 0, 0, 40,
                        [broken_knife], [])
old_man = Character('old beggar', 100, 'An old beggar wearing a tan cloak approaches you and asks '
                                       'for water. He appears parched.',
                    '"Here, take my cloak."', 0, 0, 20, [desert_cloak], [])
player = Character('you', 100, 'The main character', None, 0, 0, 30, [], [pebble])

# ROOMS-----------------------------------------------------------------------------------------------------------


class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description, items=None, characters=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.visited = False
        self.inv = items
        self.chars = characters
        self.body_of_water = False

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Spaceship
cockpit = Room("Cockpit", 'airlock', None, None, None, None, None, "You are inside your ship, in front of you are the "
               "controls. You can see two moon-sized planets through the glass in front of you. "
               "There is a small chest to your right. There is a door to the North.", [fancy_chest, space_food])
airlock = Room('Airlock', 'elandingpad', 'cockpit', "clandingpad", 'alandingpad', None, None, "You are inside your"
               " Spaceship's airlock room. Through the clear wall you can see a planet covered in trees to"
               " the north and a planet covered in sand to the west")

# Arrakis
alandingpad = Room("Arrakis Landing Pad", 'apath1', None, 'acivil', 'caveentrance', 'airlock', None, 'You are on'
                   ' Arrakis, a desert planet. To the east you see civilization, the north shows a long winding path, '
                   'and far to the west you can barely make out what appears to be a cave.', [], [])
acivil = Room('Civilization', None, None, 'ahouse', 'alandingpad', None, None, 'You reach the entrance to the '
              'civilization, which is surrounded by a large wall '
              'Rows of houses line the path. Only one appears unlocked.', [], [old_man])
ahouse = Room("Arrakis Home", None, None, None, 'acivil', None, None, 'You are in a one room house. There is a table'
              ' in front of you.'
              ' On the other side of the room there is a cot.', [crystal_knife, water_bottle1], [])
apath1 = Room("Open Desert", None, 'alandingpad', None, 'apath2', None, None, 'You have reached a crossroads.'
              'The path diverges to the south and west.', [], [])
apath2 = Room('Open Desert', None, 'caveentrance', 'apath1', None, 'plateau', None, 'You have reached a crossroads. '
                                                                                    'You are at the base of a very tall'
                                                                                    ' plateau, and to the south you see'
                                                                                    ' a cave. The path also diverges '
                                                                                    'to the east.', [], [])
plateau = Room('Plateau', None, None, None, None, None, 'apath2', 'You are on top of a tall plateau. You can see a'
                                                                  ' path winding through the desert to the east.'
                                                                  'To the south you see a cave. South-east reveals a '
                                                                  'large wall with rows of houses inside.', [], [])
caveentrance = Room('Cave Entrance', 'apath2', 'maze1', None, None, None, None, 'You are the entrance to a wide cave. '
                                                                                'Inside is pitch black.', [], [])
maze1 = Room('Maze', 'caveentrance', 'maze2', 'maze5', None, None, None, "You are inside the cave system. You can't "
                                                                         "see anything, but you can feel the walls.",
             [], [])
maze2 = Room('Maze', 'maze1', None, 'maze4', None, None, None, "You are inside the cave system You can't "
                                                               "see anything, but you can feel the walls.", [], [])
maze4 = Room('Mazel', 'maze2', None, None, 'oasis', None, None, 'You are inside the cave system. '
                                                                'You see light coming from the west.', [shiny_helmet],
             [])
maze3 = Room('Maze', 'maze2', None, None, 'maze1', None, None, "You are inside the cave system. You can't "
                                                               "see anything, but you can feel the walls.", [], [])
maze5 = Room('Maze', None, None, None, maze1, None, None, "You are inside the cave system You can't "
                                                          "see anything, but you can feel the walls.", [], [])
oasis = Room('Oasis', None, None, "maze4", None, None, None, "There is a large body of water and a palm tree. The air "
                                                             "is cooler here. This appears to be the only source of"
             " above ground water on the entire planet.", [glass_bottle], [])

# Endore
elandingpad = Room('Endore Landing Pad', 'ecivil', None, None, None, 'airlock', None, 'You are on Endore, the forest '
                                                                                      'planet. You smell smoke in the'
                                                                                      ' air.', [], [])
ecivil = Room("Civilization", 'bridge1', 'elandingpad', 'ehouse', None, None, None, 'You have reached the Endore '
                                                                                    'civilization. '
              'The grass and mud huts are few and far between'
              ' and the area seems deserted. Most huts are '
              'crumbled, except one. You think you see '
              'movement inside it.', [], [])
ehouse = Room('Hut', None, None, None, 'ecivil', None, None, 'You are inside of the hut. ', [dried_meat,
                                                                                             lembas], [strange_man])
bridge1 = Room("Wooden bridge", 'forest', 'ecivil', None, None, None, 'river', 'You are on a fancy bridge over a wide '
                                                                               'and fast moving river.', [], [])
river = Room('River', None, None, None, None, 'bridge1', None, 'You are in the river. The water is freezing cold and it'
                                                               ' is difficult to fight the strong current. '
                                                               'This was a bad idea.', [], [])
forest = Room('Forest Path', None, 'bridge1', 'bridge2', None, 'tree', None, 'You are in the forest on a well worn path'
                                                                             '. You see something glimmer at you from'
                                                                             ' the top of a nearby tree.', [], [])
tree = Room('Tree', None, None, None, None, None, 'forest', 'You are in the highest branch of a tree.', [pebble,
                                                                                                         sturdy_bow,
            apple, orange, grapefruit], [])

bridge2 = Room('Rope Bridge', None, None, 'mountains', 'forest', None, 'river', 'You are  on a fragile rope bridge '
                                                                                'above the'
                                                                                ' river. There are a few boards missing'
                                                                                ' and the surface is slippery. It sways'
                                                                                ' as you move across it.', [], [])
mountains = Room('Mountain Range', None, 'volcano', None, 'bridge2', None, None, 'You are in the mountain range. The '
                                                                                 'ground is rocky and uneven. Just past'
                                                                                 ' the range there is a volcano that is'
                                                                                 ' spewing smoke and ash. It seems clos'
                                                                                 'e to eruption.', [], [])
volcano = Room('Base of Volcano', 'mountains', None, None, None, 'volcanotop', None, 'You stand at the base of the '
                                                                                     'volcano. The air is hot and stuff'
                                                                                     'y, and you can barely see through'
                                                                                     ' the smoke. You '
                                                                                     'hear a rumble.', [elven_sword],
               [])
volcanotop = Room('Volcano', None, None, None, None, None, 'volcano', 'You stand at the mouth of the volcano. It is '
                                                                      'unbearably hot and appears as though it might '
                                                                      'erupt.', [], [])

oasis.body_of_water = True
bridge1.body_of_water = True
bridge2.body_of_water = True
river.body_of_water = True

# CONTROLLER ---------------------------------------------------------------------------------------------------
current_node = river
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

print('Welcome player! The goal of this game is to save the two planets from peril. To move use north, south, east, '
      'west, up, and down (or just type the first letter of each of these commands). Good luck!')
print('')
while True:
    print(current_node.name)
    if not current_node.visited:
        print(current_node.description)
        if current_node.chars is not None:
            for stuff in current_node.chars:
                print(stuff.description)
        if current_node.inv is not None:
            for stuff in current_node.inv:
                print(stuff.description)
    print('Your hunger is at %s and your thirst is at %s.' % (player.hunger, player.thirst))
    player.thirsty()
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.visited = True
            current_node.move(command)
            player.thirst += 1
            player.hunger += 1
        except KeyError:
            print('You cannot go this way')
    elif command[:7] == 'pick up':
        item = command[8:]
        for stuff in current_node.inv:
            if item == stuff.name:
                player.pick_up(stuff, current_node)
                if isinstance(stuff, Weapon):
                    command = input('Would you like to equip the %s? >_' % stuff.name)
                    if command == 'yes':
                        if player.equipped:
                            for things in player.weapon_equipped:
                                command = input('You already have an item equipped, would you like to replace it? >_')
                                if command == 'yes':
                                    player.un_equip(things)
                                    player.equip(stuff)
                                    print('You have equipped the %s' % stuff.name)
                                else:
                                    print('You did not equip the new weapon.')
                        else:
                            player.equip(stuff)
                            print('You have equipped the %s' % stuff.name)
                    else:
                        print('You did not equip the weapon.')
    elif command[:4] == 'take':
        item = command[5:]
        for stuff in current_node.inv:
            if item == stuff.name:
                player.pick_up(stuff, current_node)
                if isinstance(stuff, Weapon):
                    command = input('Would you like to equip the %s? >_' % stuff.name)
                    if command == 'yes':
                        if player.equipped:
                            for things in player.weapon_equipped:
                                command = input('You already have an item equipped, would you like to replace it? >_')
                                if command == 'yes':
                                    player.un_equip(things)
                                    player.equip(stuff)
                                    print('You have equipped the %s' % stuff.name)
                                else:
                                    print('You did not equip the new weapon.')
                        else:
                            player.equip(stuff)
                            print('You have equipped the %s' % stuff.name)
                    else:
                        print('You did not equip the weapon.')
    elif command[:4] == 'drop':
        item = command[5:]
        for stuff in player.inv:
            if item == stuff.name:
                player.drop(stuff, current_node)
    elif command[:6] == 'attack':
        human = command[7:]
        for stuff in current_node.chars:
            if human == stuff.name:
                if isinstance(stuff, Character):
                    player.attack(stuff)
                    if stuff.dead:
                        pass
                    else:
                        stuff.attack(player)
                else:
                    print('There is no one here to attack.')
    elif command[:4] == 'fill':
        bottle = command[5:]
        if current_node.body_of_water:
            for stuff in player.inv:
                if bottle == stuff.name:
                    if isinstance(stuff, Bottle):
                        stuff.full = 3
                        print('You filled your water bottle.')
                    elif stuff.full == 3:
                        print('Your bottle is already full')
                    else:
                        print("You don't have a bottle to fill in your inventory.")
        else:
            'There is no water here to put in your bottle.'
    elif 'equip' in command:
        thingy = command[6:]
        for stuff in player.inv:
            if thingy == stuff.name:
                if player.equipped:
                    for things in player.weapon_equipped:
                        command = input('You already have an item equipped, would you like to replace it? >_')
                        if command == 'yes':
                            player.un_equip(things)
                            player.equip(stuff)
                            print('You have equipped the %s' % stuff.name)
                        else:
                            print('You did not equip the new weapon.')
                else:
                    try:
                        player.equip(stuff)
                        print('You have equipped the %s' % stuff.name)
                    except not isinstance(stuff, Weapon):
                        print('You can only equip weapons.')
    elif command == 'drink water':
        for stuff in player.inv:
            if isinstance(stuff, Bottle):
                if stuff.full > 0:
                    player.thirst = 0
                    stuff.full -= 1
                    print('You have cured your thirst.')
                    break
                else:
                    print('Your bottle is empty.')
            else:
                print("You don't have a bottle")
    elif 'eat' in command:
        thingy = command[4:]
        for stuff in player.inv:
            if thingy == stuff.name:
                if isinstance(stuff, Food):
                    player.eat(stuff)
                    print('You have eaten the %s' % stuff.name)
                    break
                else:
                    print('You can only eat food.')
                    break
    elif command == 'description':
        print(current_node.description)
        if current_node.chars is not None:
            for stuff in current_node.chars:
                print(stuff.description)
        if current_node.inv is not None:
            for stuff in current_node.inv:
                print(stuff.description)
    elif command == 'inventory':
        print('You are carrying:')
        for item in player.inv:
            print("> " + item.name)
    elif command == 'beam me up scotty':
        current_node = airlock
    elif command == 'mr stark i dont feel so good':
        player.death()
    elif command == 'damage':
        print(player.hurt)
    elif command == 'weapons':
        for item in player.weapon_equipped:
            print(item.name)
    elif command == 'drop blue pebble':
        if current_node == volcanotop:
            'You have saved the planet!'
            player.winning += 1
    elif current_node == oasis:
        if oasis.visited is False:
            print('Give the directions to the oasis to a member of the town in order to save the planet.')
        else:
            print('Hurry! Give the directions to the town!')
    elif command == 'ssew':
        if current_node == acivil:
            print('You have saved the planet!')
            player.winning += 1
        else:
            print('Tell the town, not me!')
    else:
        print('Command not recognized.')
