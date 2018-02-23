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


cockpit = Room("Cockpit", 'Airlock', None, None, None, None, None, "You are inside your ship, in front of you are the "
                       "controls. You can see three moon-sized planets through the glass in front of you. "
                       "There is a small chest to your right.")
airlock = Room('Airlock', 'elandingpad', 'cockpit', "clandingpad", 'alandingpad', None, None)


current_node = cockpit
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while True:
    print(current_node['name']) # change
    print(current_node['DESCRIPTION']) # change
    command = input('>_').upper()
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            # change
        except KeyError:
            print('You cannot go this way')
    else:
        print("Command not recognized")