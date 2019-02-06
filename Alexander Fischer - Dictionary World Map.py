import random
import string
world_map = {
    'DESERT1': {
        "NAME": "Open Desert",
        'DESCRIPTION': "Open desert. Worms will destroy you if you can't Sandslide. There are caves to the north but"
                       " open desert to the south, east, and west.",
        'PATHS': {
            "NORTH": "SIETCH",
            'EAST': "DESERT2"
        }
    },
    'SIETCH': {
        "NAME": "SIECH TABR",
        'DESCRIPTION': 'The one safe place from the reign of Heisenwiebe. A Stillsuit is in the corner.'
                       'There is a path to the west leading to the '
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
    },
    'PALACE': {
        'NAME': "Royal Chamber",
        'DESCRIPTION': "Chamber of Baron Heisenwiebe. A gold throne stands at the end of the elaborately decorated hall"
                       ". There is a path to the south leading out of the palace, as well as paths to the west and"
                       " east.",
        'PATHS': {
            "SOUTH": "ARRAKEEN MARKET",
            'WEST': "ROYAL BEDROOM",
            'EAST': 'DINING HALL'
        }
    },
    'ARRAKEEN MARKET': {
        'NAME': "Arrakeen Market",
        'DESCRIPTION': "A market outside of the palace. There are stands that sell Stillsuit repairs and food."
                       "You hear chatter about a string a executions conducted by the Baron. To the north is a palace"
                       ", everywhere else goes deeper into the streets.",
        'PATHS': {
            "NORTH": "PALACE",
            'WEST': "STREET1",
            'EAST': 'STREET2'
        }
    },
    'STREET1': {
        'NAME': 'Suburbs of Arrakeen',
        'DESCRIPTION': "Small houses line both sides of the dusty streets. Most of the doors are locked except for one"
                       "orange house north of you. East leads to a market, while west leads into the desert.",
        'PATHS': {
            "NORTH": 'POPEYES',
            'WEST': 'DESERT4',
            'EAST': 'ARRAKEEN MARKET'
}
    },
    'DESERT2': {
        'NAME': "Open desert"
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
