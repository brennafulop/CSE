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
alandingpad = Room("Arrakis Landing pad", 'apath1', None, 'acivil', 'cave', None, None, 'You are on Arrakis, a desert '
                            'planet. To the east you see civilization, the north shows a long winding path, and far to '
                            ' the west you can barely make out what appears to be a cave.')
acivil = Room('Civilization', None, None, 'acivilpath1', 'alandingpad', None, None, 'You reach the entrance to the '
                        'civilization, which is surrounded by a large wall '
                        'Rows of mud and grass houses line the paths. An old beggar in a tan cloak approaches'
                        ' you and asks for water.')
acivilpathn1 = Room()
acivilwall = Room()
acivilbackwall = Room()
apath1 = Room()

# Caladan


# Endore


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