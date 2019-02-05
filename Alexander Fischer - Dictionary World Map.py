import random
import string
world_map = {
    'DESERT1': {
        "NAME": "Open Desert",
        'DESCRIPTION': "Open desert. Worms will destroy you if you can't Sandslide. There are caves to the north but"
                       " open desert to the south, east, and west.",
        'PATHS': {
            "NORTH": "SIETCH"
        }
    },
    'SIETCH': {
        "NAME": "SIECH TABR",
        'DESCRIPTION': 'The one safe place from the reign of Heisenweibe. There is a path to the west leading to the '
                       'pit. North leads to the spice rooms.',
        'PATHS': {
            "SOUTH": "DESERT1",
            'WEST': 'FREMEN PIT',
            'NORTH': "SPICE ROOMS"
        }
    },
    'SPICE ROOMS': {
        'NAME': 'Spice Rooms',
        "DESCRIPTION": "Spice is stacked in boxes all across the room. The only way out is the way you came in.",
        'PATHS': {
            'SOUTH': 'SIETCH'
        }
    },
    'FREMEN PIT': {
        'NAME': "Fighting Pit",
        'DESCRIPTION': 'Gathering area during tribal meetings and ritual combat. There is a path to the east and a'
                       ' staircase leading downwards.',
        'PATHS': {
            'DOWN': 'WATER'
        }
    }
}

# CONTROLLER
playing = True
current_node = world_map['DESERT1']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
sandslide = False
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in short_directions:
        index = short_directions.index(command.lower())
        command = directions[index]

    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Found")
