import random
import string
world_map = {
    'DESERT1': {
        "NAME": "Open Desert",
        'DESCRIPTION': "Desert surrounds you. Worms will destroy you if you can't Sandslide. There are caves to the north but"
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
    "ROYAL BEDROOM": {
        "NAME": "Royal Bedroom",
        "DESCRIPTION": "Bedchambers of the Baron. There is a massive red wardrobe and shield on one side. Above the"
                       " bed is a head of a bear, believed to have killed a Duke.",
        "PATHS": {
            "EAST": "PALACE"
        }
    },
    'DINING HALL': {
        "NAME": "Dining Hall",
        "DESCRIPTION": "You walk into a massive room. Banners of the ruling Harkonnens line the high ceilings."
                       " A massive wooden table is in the center of the room with food and water laid out.",
        "PATHS": {
            "WEST": "PALACE"
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
            'WEST': 'DESERT6',
            'EAST': 'ARRAKEEN MARKET'
        }
    },
    'DESERT2': {
        'NAME': "Open desert",
        'DESCRIPTION': "Desert surrounds you. Worms will destroy you if you can't Sandslide.",
        'PATHS': {
            "NORTH": "DESERT3",
            'WEST': "DESERT1",
            "EAST": "DESERT4"
        }
    },
    'DESERT3': {
        'NAME': "Open desert",
        'DESCRIPTION': "Desert surrounds you. Worms will destroy you if you can't Sandslide.",
        'PATHS': {
            "SOUTH": "DESERT2",
            'WEST': "DESERT1",
            "EAST": "DESERT5"
        }
    },
    'DESERT4': {
        'NAME': "Open desert",
        'DESCRIPTION': "Desert surrounds you. Worms will destroy you if you can't Sandslide.",
        'PATHS': {
            "NORTH": "DESERT5",
            'WEST': "DESERT2",
            "EAST": "DESERT6"
        }
    },
    'DESERT5': {
        'NAME': "Open desert",
        'DESCRIPTION': "Desert surrounds you. Worms will destroy you if you can't Sandslide.",
        'PATHS': {
            "SOUTH": "DESERT4",
            'WEST': "DESERT3",
            "EAST": "ROCKFACE"
        }
    },
    'DESERT6': {
        'NAME': "Open desert",
        'DESCRIPTION': "The desert vanishes as you see that to the south "
                       "and east, civilization appears. However, Worms will destroy you if you can't Sandslide.",
        'PATHS': {
            "SOUTH": "STREET2",
            'WEST': "DESERT6",
            "EAST": "STREET1"
        }
    },
    'STREET2': {
        "NAME": "Street of Arrakeen",
        "DESCRIPTION": "Houses line both sides of the crowded street. Imperial guards stand on the corner looking for"
                       " any Fremen. The street leads north and east.",
        "PATHS": {
            "NORTH": "DESERT6",
            "EAST": "STREET1"
        }
    },
    "ROCKFACE": {
        "NAME": "Rock face",
        "DESCRIPTION": "You find yourself standing in the desert facing a large sheet of rock blocking the north and "
                       " east. You need to move quickly to avoid any patrols looking to kill you.",
        "PATHS": {
            "UP": "SIETCH BALBOA",
            "WEST": "DESERT5",
            "SOUTH": "PATROL STATION"
        }
    },
    "PATROL STATION": {
        "NAME": "Patrol Station",
        "DESCRIPTION": "Imperial soldiers are all around the massive stone barracks. As you approach, one of the guards"
                       "spots you. You quickly look around and notice that your only escape option is the north.",
        "PATHS": {
            "NORTH": "ROCKFACE"
        }
    },
    "SIETCH BALBOA": {
        "NAME": "Sietch Balboa",
        "DESCRIPTION": "You find yourself at the entrance to another Fremen Sietch. For some unkown reason, the doors"
                       " are closed and it does not appear that they can be opened. However, there are paths up and"
                       " down the cliff.",
        "PATHS": {
            "UP": "POPEYES",
            "DOWN": "ROCKFACE"
        }
    },
    "POPEYES": {
        "NAME": "Popeyes Chicken",
        "DESCRIPTION": "The land of the gods. All around you is chicken stacked to the heavens. You investigate further" 
                       "and notice some sort of computer file. It is in rough condition, but you can see that it"
                       " mentions calling a god. Please just go down.",
        "PATHS": {
            "DOWN": "SIETCH BALBOA"
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
