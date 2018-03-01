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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Spaceship
cockpit = Room("Cockpit", 'airlock', None, None, None, None, None, "You are inside your ship, in front of you are the "
                       "controls. You can see three moon-sized planets through the glass in front of you. "
                       "There is a small chest to your right.")
airlock = Room('Airlock', 'elandingpad', 'cockpit', "clandingpad", 'alandingpad', None, None, "You are inside your"
                        " Spaceship's airlock room. Through the clear wall you can see a planet covered in trees to"
                        " the north, a planet covered in water to the east, and a planet covered in sand to the west")


# Arrakis
alandingpad = Room("Arrakis Landing Pad", 'apath1', None, 'acivil', 'cave', 'airlock', None, 'You are on Arrakis, a desert '
                            'planet. To the east you see civilization, the north shows a long winding path, and far to '
                            ' the west you can barely make out what appears to be a cave.')
acivil = Room('Civilization', None, None, 'ahouse', 'alandingpad', None, None, 'You reach the entrance to the '
                        'civilization, which is surrounded by a large wall '
                        'Rows of houses line the path. Only one appears unlocked. '
                        'An old beggar in a tan cloak approaches you and asks for water.')
ahouse = Room("Arrakis Home", None, None, None, 'acivil', None, None, 'You are in a one room house. There is a table'
                                                                     ' in front of you with an old knife on it. Next '
                                                                     'to the knife there sits a small bottle of water.'
                                                                     ' On the other side of the room there is a cot.')
apath1 = Room("Open Desert", None, 'alandingpad', None, 'apath2', None, None, 'You have reached a crossroads.'
                                                                                      'The path diverges in all '
                                                                                      'directions.')
apath2 = Room('Open Desert', None, 'caveentrance', 'apath1', None, 'plateau', None, 'You have reached a crossroads. '
                                                                                    'You are at the base of a very tall'
                                                                                    ' plateau, and to the south you see'
                                                                                    ' a cave.')
plateau = Room('Plateau', None, None, None, None, None, 'apath2', 'You are on top of a tall plateau. You can see a'
                                                                  ' path winding through the desert to the east.'
                                                                  'To the south you see a cave. South-east reveals a '
                                                                  'large wall with rows of houses inside.')
caveentrance = Room('Cave Entrance', 'apath2', 'maze1', None, None, None, None, 'You are the entrance to a wide cave. '
                                                                                'Inside is pitch black.')
maze1 = Room('Tunnel', 'caveentrance', 'maze2', 'maze3', None, None, None, "You are inside the cave system. You can't "
                                                                           "see anything, but you can feel the walls.")
maze2 = Room('Tunnel', 'maze1', 'maze4', None, None, None, None, "You are inside the cave system You can't "
                                                                 "see anything, but you can feel the walls.")
maze4 = Room('Tunnel', 'maze2', None, None, 'oasis', None, None, 'You are inside the cave system. '
                                                                 'You see light coming from the west.')
maze3 = Room('Tunnel', 'maze2', None, None, 'maze1', None, None, "You are inside the cave system. You can't "
                                                                 "see anything, but you can feel the walls.")
oasis = Room('Oaisis', None, None, "maze4", None, None, "There is a large body of water and a palm tree. The air is"
                                                        " cooler here." )

# Caladan
clandingpad = Room()

# Endore
elandingpad = Room()

current_node = cockpit
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while True:
    print (current_node.name)
    print(current_node.description)
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('You cannot go this way')
    else:
        print("Command not recognized")
