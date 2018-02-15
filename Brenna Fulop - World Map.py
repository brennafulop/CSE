world_map = {
    # Spaceship
    'AIRLOCK': {
        'NAME': 'Airlock',
        'DESCRIPTION': "You are inside of your spaceship's airlock room. You can see stars in an otherwise empty sky",
        'PATHS': {
            'NORTH': 'ELANDINGPAD',
            'WEST': 'ALANDINGPAD',
            'EAST': 'CLANDINGPAD',
            'SOUTH': 'COCKPIT'
        }
    },
    'COCKPIT': {
        'NAME': 'Cockpit',
        'DESCRIPTION': "You are inside your ship, in front of you are the controls."
                       " You can see three moon-sized planets through the glass in front of you. "
                       "There is a small chest to your right.",
        'PATHS': {
            'NORTH': 'AIRLOCK',
            'WEST': 'CHEST',
            'EAST': 'CONTROLS'
            }
    },
    # Arrakis
    'ALANDINGPAD': {
        'NAME': 'Arrakis Landing Pad',
        'DESCRIPTION': 'You are on Arrakis, a desert planet. To the east you see civilization. The north shows a'
                       ' long winding path.',
        'PATHS': {
            'EAST': 'ACIVIL',
            'NORTH': 'APATH1',
            'WEST': 'CAVE'
        }
    },
    # Civilization
    'ACIVIL': {
        "NAME": 'Civilization',
        'DESCRIPTION': 'You reach the entrance to the civilization, which is surrounded by a large wall '
                       'Rows of mud and grass houses line the paths. An old beggar in a tan cloak approaches'
                       ' you and asks for water.',
        'PATHS': {
            'WEST': 'ALANDINGPAD',
            'EAST': 'ACIVILPATHN1'
        }
    },
    'ACIVILPATHN1': {
        'NAME': 'Civilization',
        'DESCRIPTION': 'You have reached a crossroads. Houses surround you, but all seem locked.',
        'PATHS': {
            'WEST': 'ACIVIL',
            'NORTH': 'ACIVILWALL1',
            'SOUTH': 'ACIVILBACKWALL1'
        }
    },
    'ACIVILWALL1': {
        'NAME': 'Civilization',
        'DESCRIPTION': 'You have reached the wall. You cannot go any farther. Houses surround you, but they all seem '
                       'locked',
        'PATHS': {
            'SOUTH': 'ACIVILPATHN1'
        }
    },
    'APATH1': {
        'NAME': 'Open Desert',
        'DESCRIPTION': 'You have reached a crossroads. You can see a natural structure in the distance to the west',
        'PATHS': {
            'NORTH': 'DUNES',
            'SOUTH': 'ALANDINGPAD',
            'EAST': 'FREEMAN',
            'WEST': 'APATH2'
        }
    },
    'APATH2': {
        'NAME': 'Open Desert',
        'DESCRIPTION': 'You have reached a crossroads. You see a plateau to the north and a cave to the south.',
        'PATHS': {
            'NORTH': 'PLATEAUBOTTOM',
            'SOUTH': 'CAVEENTRANCE',
            'EAST': 'APATH1'
        }
    },
    'PLATEAUBOTTOM': {
        'NAME': 'Plateau base',
        'DESCRIPTION': 'You are at the base of a plateau, and the wall seems rocky enough to climb. The path stops here.',
        'PATHS': {
            'UP': 'PLATEAU',
            'SOUTH': 'APATH2'
            }
    },
    'PLATEAU': {
        'NAME': 'Plateau',
        'DESCRIPTION': 'You are on top of a tall plateau. You can see a path winding through the desert to the east.'
                       'Farther to the east you see a less advanced civilization. To the south you see a cave.'
                       'South-east reveals a large wall with rows of houses inside. Finally, to the north you can see '
                       'tallest sand dunes you have ever witnessed.'
    }





}

current_node = world_map['COCKPIT']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_').upper()
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node["PATHS"][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('You cannot go this way')
    else:
        print("Command not recognized")
