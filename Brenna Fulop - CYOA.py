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
        if person.hunger < 0:
            person.hunger = 0
        self.consumed(person)


class Map(Item):
    def __init__(self, name, description, contents):
        super(Map, self).__init__(name, description)
        self.contents = contents

    def read(self):
        print(self.contents)


elven_sword = Sword('elven sword', 'An elven sword has been stuck in the ground.', 30)
broken_knife = Knife('broken knife', "The broken knife, it has been snapped, yet it is still sharp.", 15)
crystal_knife = Knife('crystal knife', "A crystal knife glimmers at you from the ground. it has been half-buried.", 25)
sturdy_bow = Bow('sturdy bow', "A sturdy wooden bow with engravings in the handle sits next to you."
                               " A quiver of arrows is next to it and seems to be charmed.", 30, 40)
desert_cloak = Cloak('desert cloak', "There is a sturdy desert cloak that will protect you from the forces of the "
                                     "desert.", 10)
silver_helmet = Helmet('silver helmet', "You see a silver helmet shoved into the ground.", 30)
glass_bottle = Bottle('glass bottle', 'A full glass bottle shimmers from on the ground.')
space_food = Food('space food', "There is a packet of space food on the floor.", 35)
dried_meat = Food('dried meat', "On the floor there is some dried meat of unknown origin.", 30)
lembas = Food('lembas', "Kept clean by being wrapped in leaves, there are some lembas on the ground.", 20)
apple = Food('apple', 'You see a shiny red apple.', 5)
orange = Food('orange', 'There is an orange.', 5)
grapefruit = Food('grapefruit', 'There is a grapefruit.', 5)
water_bottle1 = Bottle('water bottle', 'A water bottle filled with water sits on the ground.', [])
water_bottle2 = Bottle('water bottle', 'A water bottle filled with water sits on the ground.', [])
stone = Item('blue stone', 'A blue stone glimmers at you.')
oasismap = Map('map', 'There is a worn map.', 'Map To Oasis: \n1.Enter cave \n2.Go south \n3.Go south \n4.Go east \n5.'
                                              'Go west')

# CHARACTERS---------------------------------------------------------------------------------------------------------


class Character(object):
    def __init__(self, name, health, description, dialogue, thirst, hunger, hurt, armour=None,
                 weapon_equipped=None, items=None):
        if items is None:
            items = []
        self.name = name
        self.health = health
        self.description = description
        self.dialogue = dialogue
        self.dead = False
        self.get_thirsty = True
        self.thirst = thirst
        self.hunger = hunger
        self.hurt = hurt
        self.equipped = False
        self.won = False
        self.winning = 0
        self.armour = armour
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
            print('His things scatter on the floor.')
            for thing in self.inv:
                current_node.inv.append(thing)

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
        if isinstance(thing, Weapon):
            self.equipped = True
            self.weapon_equipped.append(thing)
            self.hurt = thing.damage + self.hurt
        elif isinstance(thing, Wearable):
            self.equipped = True
            self.armour.append(thing)
            self.health = thing.protection + self.health
            if isinstance(thing, Cloak):
                self.get_thirsty = False

    def un_equip(self, thing):
        if self.equipped:
            self.equipped = False
            if isinstance(thing, Weapon):
                self.weapon_equipped.remove(thing)
                self.inv.append(thing)
                self.hurt -= thing.damage
            elif isinstance(thing, Wearable):
                self.inv.append(thing)
                self.armour.remove(thing)
                self.health -= thing.protection
        else:
            print('You must have something equipped to un-equip it.')

    def win(self):
        self.won = True
        print('You win! Congratulations You have saved both of the planets in peril. \nYou fly at warp speed back to'
              ' Earth, satisfied that you completed your mission.')
        exit(0)


strange_man = Character('elven man', 100, 'In the corner there is an elven man '
                                          'in tattered clothing holding a broken knife. He is frightened by '
                                          'you.', 'The elven man looks at you and says, "Please, the stone, return it '
                                                  'to the volcano."', 0, 0, 40,
                        [], [broken_knife], [broken_knife])
old_man = Character('old beggar', 100, 'There is an old beggar wearing a tan cloak.',
                    ['He looks at you and says, "Thank you so much, my dear child. Here, take my cloak, it will protect'
                     ' you well"', 'The old beggar approaches you and says, "Can you spare some water?"'], 0, 0, 20, [],
                    [], [desert_cloak])
player = Character('you', 100, 'The main character', None, 0, 0, 40, [], [], [water_bottle2])


# ROOMS-----------------------------------------------------------------------------------------------------------


class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description, items, characters=None):
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
cockpit = Room("Cockpit", 'airlock', None, None, None, None, None, "You are inside your ship, in front of you are the\n"
               "controls. You can see two moon-sized planets through the glass in front of you. \n"
               "There is a door to the North.", [space_food, water_bottle2])
airlock = Room('Airlock', 'elandingpad', 'cockpit', "clandingpad", 'alandingpad', None, None, "You are inside your"
               " Spaceship's airlock room.\nThrough the clear wall you can see a planet covered in trees to"
               " the north and a planet covered in sand to the west", [])

# Arrakis
alandingpad = Room("Arrakis Landing Pad", 'apath1', None, 'acivil', 'caveentrance', 'airlock', None, 'You are on'
                   ' Arrakis, a desert planet. \nTo the east you see civilization, the north shows a long winding path,'
                   ' \nand far to the west you can barely make out what appears to be a cave.', [], [])
acivil = Room('Civilization', None, None, 'ahouse', 'alandingpad', None, None, 'You reach the entrance to the '
              'civilization, which is surrounded by a large wall \n'
              'Rows of houses line the path. Only one to the east appears unlocked. There is also a path to the west',
              [], [old_man])
ahouse = Room("Arrakis Home", None, None, None, 'acivil', None, None, 'You are in a one room house. There is a table'
              ' in front of you.\n'
              'On the other side of the room there is a cot.', [crystal_knife, water_bottle1], [])
apath1 = Room("Open Desert", None, 'alandingpad', None, 'apath2', None, None, 'You have reached a crossroads.\n'
              'The path diverges to the south and west.', [], [])
apath2 = Room('Open Desert', None, 'caveentrance', 'apath1', None, 'plateau', None, 'You have reached a crossroads.\n'
                                                                                    'You are at the base of a very tall'
                                                                                    ' plateau, and to the south you see'
                                                                                    '\na cave. The path also diverges '
                                                                                    'to the east.', [], [])
plateau = Room('Plateau', None, None, None, None, None, 'apath2', 'You are on top of a tall plateau. You can see a'
                                                                  ' path winding through the desert to the east.\n'
                                                                  'To the south you see a cave. South-east reveals a '
                                                                  'large wall with rows of houses inside.', [], [])
caveentrance = Room('Cave Entrance', 'apath2', 'maze1', None, None, None, None, 'You are the entrance to a wide cave. '
                                                                                'Inside is pitch black.', [], [])
maze1 = Room('Maze', 'caveentrance', 'maze2', 'maze5', None, None, None, "You are inside the cave system. You can't "
                                                                         "see anything, but you can feel the walls.",
             [], [])
maze2 = Room('Maze', 'maze1', None, 'maze4', None, None, None, "You are inside the cave system You can't "
                                                               "see anything, but you can feel the walls.", [], [])
maze4 = Room('Maze', 'maze2', None, None, 'oasis', None, None, 'You are inside the cave system. '
                                                               'You see light coming from the west.', [silver_helmet],
             [])
maze3 = Room('Maze', 'maze2', None, None, 'maze1', None, None, "You are inside the cave system. You can't "
                                                               "see anything, but you can feel the walls.", [], [])
maze5 = Room('Maze', None, None, None, maze1, None, None, "You are inside the cave system You can't "
                                                          "see anything, but you can feel the walls.", [], [])
oasis = Room('Oasis', None, None, "maze4", None, None, None, "There is a large body of water and a palm tree. The air "
                                                             "is cooler here. \nThis appears to be the only source of"
             " above ground water on the entire planet.", [glass_bottle, oasismap], [])

# Endore
elandingpad = Room('Endore Landing Pad', 'ecivil', None, None, None, 'airlock', None, 'You are on Endore, the forest '
                                                                                      'planet. You smell smoke in the'
                                                                                      ' air. To the north you see '
                                                                                      'civilization', [], [])
ecivil = Room("Civilization", 'bridge1', 'elandingpad', 'ehouse', None, None, None, 'You have reached the Endore '
                                                                                    'civilization. '
              'The grass and mud huts are few and far between'
              ' and the area seems deserted. \nMost huts are '
              'crumbled, except one to the east. You think you see '
              'movement inside it. \nTo the north there is a bridge.', [], [])
ehouse = Room('Hut', None, None, None, 'ecivil', None, None, 'You are inside of the hut. The door is to the west',
                                                             [dried_meat, lembas], [strange_man])
bridge1 = Room("Wooden bridge", 'forest', 'ecivil', None, None, None, 'river', 'You are on a fancy bridge over a wide '
                                                                               'and fast moving river. To the north you'
                                                                               ' see a dense forest. \nTo the south '
                                                                               'there is civilization.', [], [])
river = Room('River', None, None, None, None, 'bridge1', None, 'You are in the river. The water is freezing cold and it'
                                                               ' is difficult to fight the strong current. \n'
                                                               'This was a bad idea.', [], [])
river2 = Room('River', None, None, None, None, 'bridge2', None, 'You are in the river. The water is freezing cold and '
                                                                ' it is difficult to fight the strong current. \n'
                                                                'This was a bad idea.', [], [])
forest = Room('Forest Path', None, 'bridge1', 'bridge2', None, 'tree', None, 'You are in the forest on a well worn path'
                                                                             '. To the south there is a fancy bridge,'
                                                                             ' and to the east there is an '
                                                                             'old rope bridge',
                                                                             [], [])
tree = Room('Tree', None, None, None, None, None, 'forest', 'You are in the highest branch of a tree.', [stone,
                                                                                                         sturdy_bow,
            apple, orange, grapefruit], [])

bridge2 = Room('Rope Bridge', None, None, 'mountains', 'forest', None, 'river', 'You are  on a fragile rope bridge '
                                                                                'above the river. '
                                                                                '\nThere are a few boards missing'
                                                                                ' and the surface is slippery. \nIt '
                                                                                'sways'
                                                                                ' as you move across it. \nThere is a '
                                                                                'mountain range to the east and dense '
                                                                                'forest to the west', [], [])
mountains = Room('Mountain Range', None, 'volcano', None, 'bridge2', None, None, 'You are in the mountain range. The '
                                                                                 'ground is rocky and uneven. \n'
                                                                                 'Just past'
                                                                                 ' the range to the south'
                                                                                 ' there is a volcano. \nThere is a '
                                                                                 'bridge to the west', [], [])
volcano = Room('Base of Volcano', 'mountains', None, None, None, 'volcanotop', None, 'You stand at the base of the '
                                                                                     'volcano. The air is hot and '
                                                                                     'stuffy. \nThe north shows a '
                                                                                     'mountain range, and above you'
                                                                                     ' there is the top of the volcano',
               [elven_sword],
               [])
volcanotop = Room('Volcano', None, None, None, None, None, 'volcano', ['You stand at the mouth of the volcano. It is '
                                                                       'unbearably hot and appears as though it might '
                                                                       'erupt.', 'You stand at the mouth of the volcano'
                                                                                 '.'], [], [])

oasis.body_of_water = True
bridge1.body_of_water = True
bridge2.body_of_water = True
river.body_of_water = True

# CONTROLLER ---------------------------------------------------------------------------------------------------
current_node = cockpit
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

print('Welcome player! The goal of this game is to save the two planets from peril. \n')
instructions = input('Would you like some instructions? >_')
if instructions == 'yes':
    print("To move use north, south, east, west, up, and down(or just the first letter of each of these commands)."
          "\nTo pick something up use 'pick up (item's full name)' or 'take (item's full name)'. For example, \nif an"
          " item is described as 'elven sword' say 'pick up elven sword'. \nTo drop an item, it's exactly the same, "
          "just say 'drop (item's full name)'. \nTo eat, say 'eat (item's full name)'."
          "\nTo drink, just say 'drink water' and if you have a bottle in your inventory you will \ndrink 1/3 of the"
          " water in the bottle."
          "\nTo fill an empty water bottle, go to a room that contains water and type 'fill (item's name)'"
          "\nTo attack someone type 'attack (person's full name)'. \nTo give someone something type 'give"
          " (person's full name)' and hit enter. \nThe game should then ask what to give to them, so just type the item"
          "'s full name and hit enter. \nWhen you pick up a weapon the game will ask if you would like to equip it."
          "\nYou can equip any weapon or wearable at any time by typing 'equip (item name)' \nIf you have an item "
          "that you think you should be able to read, type 'read (item name)' \nIf you need the description of a room,"
          " type 'look'. \nTo see your current stats type 'stats'."
          " \nTo get back to your ship from any location, type 'beam me up scotty'. \nTo see this message"
          " again, type '?'. \nFinally, to quit the game at any point type 'quit'")
elif instructions == 'no':
    print("Brave choice! If you get confused type '?' at any point for the instructions")
while True:
    print('\n'+current_node.name+'\n')
    if not current_node.visited:
        if current_node == volcanotop:
            for stuff in volcanotop.inv:
                if stuff is stone:
                    print(volcanotop.description[1])
                else:
                    print(volcanotop.description[0])
        else:
            print(current_node.description)
            if current_node.chars is not None:
                for stuff in current_node.chars:
                    print(stuff.description)
            if current_node.inv is not None:
                for stuff in current_node.inv:
                    print(stuff.description)
            if current_node == acivil:
                for stuff in old_man.inv:
                    if isinstance(stuff, Bottle):
                        break
                    else:
                        print(old_man.dialogue[1])
            if current_node == forest:
                for stuff in tree.inv:
                    if stuff is stone:
                        print('You see something glimmer at you from the top of a nearby tree.')
    if current_node == oasis:
        if oasis.visited is False:
            print('Give the map to a member of the town in order to save the planet.')
        else:
            print('Hurry! Give the directions to the town!')
    if current_node == ehouse:
        for people in ehouse.chars:
            print(people.dialogue)
    player.thirsty()
    player.hungry()
    print('Your hunger is at %s and your thirst is at %s.' % (player.hunger, player.thirst))
    command = input('>_').lower().strip()
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.visited = True
            current_node.move(command)
            if player.get_thirsty is True:
                player.thirst += 10
            player.hunger += 5
        except KeyError:
            print('You cannot go this way')
    elif command == 'quit':
        command = input("Are you sure you want to quit? >_")
        if command == 'yes':
            exit(0)
        elif command == 'no':
            print("Perseverance is key")
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
                if stuff.name == 'blue stone':
                    if current_node is volcanotop:
                        player.drop(stuff, current_node)
                        print('You have saved the planet!')
                        player.winning += 50
                        if player.winning == 100:
                            player.win()
                else:
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
    elif 'give' in command:
        human = command[5:]
        for stuff in current_node.chars:
            if human == stuff.name:
                if isinstance(stuff, Character):
                    command = input('What you you like to give the %s? >_' % stuff.name)
                    stuffs = command
                    for thingy in player.inv:
                        if stuffs == thingy.name:
                            if human == 'old beggar':
                                if stuffs == 'map':
                                    print('You give the %s to the %s' % (stuffs, human))
                                    player.inv.remove(thingy)
                                    stuff.inv.append(thingy)
                                    print('Congratulations! You have saved Arrakis by providing water to the town!')
                                    player.winning += 50
                                    if player.winning == 100:
                                        player.win()
                                elif isinstance(thingy, Bottle):
                                    if thingy.full > 0:
                                        print('You give the %s to the %s' % (thingy.name, human))
                                        stuff.inv.append(thingy)
                                        player.inv.remove(thingy)
                                        if desert_cloak in stuff.inv:
                                            print(stuff.dialogue[0])
                                            player.inv.append(desert_cloak)
                                            stuff.inv.remove(desert_cloak)
                                            print('He gives you the %s.' % desert_cloak.name)
                                else:
                                    print('You give the %s to the %s' % (stuffs, human))
                                    player.inv.remove(thingy)
                                    stuff.inv.append(thingy)
                            else:
                                print('You give the %s to the %s' % (stuffs, human))
                                player.inv.remove(thingy)
                                stuff.inv.append(thingy)
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
                if isinstance(stuff, Weapon):
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
                elif isinstance(stuff, Wearable):
                    player.equip(stuff)
                    print('You have equipped the %s' % stuff.name)
    elif command == 'drink water':
        for stuff in player.inv:
            if isinstance(stuff, Bottle):
                if stuff.full > 0:
                    player.thirst = 0
                    stuff.full -= 1
                    print('You have cured your thirst.')
                    break
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
    elif 'read' in command:
        thingy = command[5:]
        for stuff in player.inv:
            if thingy == stuff.name:
                if isinstance(stuff, Map):
                    print('The %s reads:' % stuff.name)
                    stuff.read()
    elif command == 'look':
        print(current_node.description)
        if current_node.chars is not None:
            for stuff in current_node.chars:
                print(stuff.description)
        if current_node.inv is not None:
            for stuff in current_node.inv:
                print(stuff.description)
        if current_node == acivil:
            for stuff in old_man.inv:
                if isinstance(stuff, Bottle):
                    break
                else:
                    print(old_man.dialogue[1])
        if current_node == forest:
            for stuff in tree.inv:
                if stuff is stone:
                    print('You see something glimmer at you from the top of a nearby tree.')
    elif command == 'inventory':
        if player.inv is not None:
            print('You are carrying:')
            for item in player.inv:
                print("> " + item.name)
        elif player.inv is None:
            print("You don't seem to be carrying anything")
    elif command == 'beam me up scotty':
        current_node = airlock
    elif command == 'mr stark i dont feel so good':
        player.death()
    elif command == 'stats':
        print('Health: %s \nDamage: %s \nWeapon equipped: %s \nCurrent score (out of 100): %s' % (player.health,
              player.hurt, player.weapon_equipped[0].name, player.winning))
    elif command == '?':
        print("To move use north, south, east, west, up, and down(or just the first letter of each of these commands)."
              "\nTo pick something up use 'pick up (item's full name)' or 'take (item's full name)'. For example, "
              "\nif an"
              " item is described as 'elven sword' say 'pick up elven sword'. \nTo drop an item, it's "
              "exactly the same, "
              "just say 'drop (item's full name)'. \nTo eat, say 'eat (item's full name)'."
              "\nTo drink, just say 'drink water' and if you have a bottle in your inventory you will "
              "\ndrink 1/3 of the"
              " water in the bottle."
              "\nTo fill an empty water bottle, go to a room that contains water and type 'fill (item's name)'"
              "\nTo attack someone type 'attack (person's full name)'. \nTo give someone something type 'give"
              " (person's full name)' and hit enter. \nThe game should then ask what to give to them, so "
              "just type the item"
              "'s full name and hit enter. \nWhen you pick up a weapon the game will ask if you would like to equip it."
              "\nYou can equip any weapon or wearable at any time by typing 'equip (item name)' \nIf you have an item "
              "that you think you should be able to read, type 'read (item name)' \nIf you need the "
              "description of a room,"
              " type 'look'. \nTo see your current stats type 'stats'."
              " \nTo get back to your ship from any location, type 'beam me up scotty'. \nTo see this message"
              " again, type '?'. \nFinally, to quit the game at any point type 'quit'")
    else:
        print('Command not recognized.')
