import random
import string
world_map = {
    'R19A': {
        "NAME": "Mr. Weibe's Room",
        'DESCRIPTION': 'The room of despair, where Heisenwiebe reigns supreme. He is omnipotent and can only be killed'
                       ' by calling God.',
        'PATHS': {
            "NORTH": "SIETCH"
        }
    },
    'SIETCH': {
        "NAME": "SIECH TABR",
        'DESCRIPTION': 'The one safe place from the reign of Heisenwiebe. Currently headed by Stilgar.',
        'PATHS': {
            "SOUTH": "R19A"
        }
    },
}

# CONTROLLER
playing = True
current_node = world_map['R19A']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
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
