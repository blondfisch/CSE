import random
import string
world_map = {
    'R19A': {
        "NAME": "Mr. Weibe's Room",
        'DESCRIPTION': 'The room of despair, where Heisenwiebe reigns supreme. He is omnipotent and can only be killed'
                       'by calling God.',
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
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ["p", "quit", "exit"]:
        playing = False
