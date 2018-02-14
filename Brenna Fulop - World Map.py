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
        'DESCRIPTION': "You are inside your ship. In front of you are the controls."
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
        'DESCRIPTION': 'You are now on Arrakis, a desert planet. To the east you see civilization. The north shows a'
                       ' long winding path.',
        'PATHS': {
            'EAST': 'ACIVIL',
            'NORTH': 'APATH1',
            'WEST': 'CAVE'
        }
    },
    'ACIVIL': {
        "NAME": 'Civilization',
        'DESCRIPTION': 'You reach the civilization, which seems fairly advanced. Rows of mud and grass houses line the'
                       ' paths. An old beggar in a tan cloak approaches you and asks for water.',
        'PATHS': {
            'WEST': 'ALANDINGPAD',
            'EAST': 'ACIVILPATHN1'
        }

    }
}

current_node = world_map['COCKPIT']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_'.upper())
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
