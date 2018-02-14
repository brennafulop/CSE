world_map = {
    'WESTHOUSE': {
    'NAME': 'West of house',
    'DESCRIPTION':"You are west of a white house.",
    "PATHS": {
        'NORTH': 'NORTHHOUSE',
        'SOUTH': 'SOUTHOUSE'
    }

    },
    'SOUTHHOUSE': {
        "NAME": 'South of house',
        'DESCRIPTION': 'You are south of a white house',
        'PATHS':{
            'WEST': 'WESTHOUSE'
        }
    },
    'NORTHHOUSE': {
        "NAME": 'North of house',
        'DESCRIPTION': 'You are north of a white house',
        'PATHS':{
            'WEST': 'WESTHOUSE'
        }
    }
}

