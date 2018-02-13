world_map = {
    'AIRLOCK': {
        'NAME': 'Airlock',
        'DESCRIPTION': "You are inside of your spaceship's airlock room. You can see three small planets surrounding"
                       " your ship.",
        'PATHS': {
            'NORTH': 'ELANDINGPAD',
            'WEST': 'ALANDINGPAD',
            'EAST': 'CLANDINGPAD',
            'SOUTH': 'COCKPIT'
        }
    },
    'COCKPIT': {
        'NAME': 'Cockpit',
        'DESCRIPTION': "You are inside your ship. In front of you are the controls. The colorful buttons light up the "
                       "room. You can see three moon-sized planets in front of you. There is a small chest to your "
                       "right.",
        'PATHS': {
            'NORTH': 'AIRLOCK',
            'WEST': 'CHEST',
            'EAST': 'CONTROLS'
            }
    },
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
                       ' paths. An old beggar approaches you and asks for water.',
        'PATHS': {
            'WEST': 'ALANDINGPAD',
            'EAST': 'ACIVILPATHN1'
        }

    }
}
