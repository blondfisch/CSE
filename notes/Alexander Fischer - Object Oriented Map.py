class Room(object):
    def __init__(self, name, desc, north=None, south=None, east=None, west=None, up=None, down=None, characters=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.desc = desc
        self.characters = characters


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []
        self.sandslide = False

    def move(self, new_location):
        """ This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room to see if a room exists in that direction.

        :param direction: The direction that you want to move to
        :return: The room object if it exists, or none if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


class Enemy(object):
    def __init__(self, health=10, desc=None, shield=False):
        self.health = health
        self.desc = desc
        self.items = []
        self.shield = shield


# Option 2 - set all at once, modify controller
# Rooms
DESERT1 = Room("Open Desert", 'The sun beats down on the sandy desert all around you. There are caves to the north'
                              ' inside of the rock, a place of safety from the worms in the desert.\n On all other '
                              'sides'
                              ' is the desert.',
               "SIETCH", 'DESERT2', 'DESERT3', 'DESERT4')
SIETCH = Room("Sietch Tabr", 'You walk into a hidden Fremen cave. Inside, you find a Stillsuit folded in a '
                             'corner, as well as paths leading deeper into the chamber'
                             ' to the north and south.',
              None, 'DESERT1', 'SPICE_ROOMS', 'FREMEN_PIT')
SPICE_ROOMS = Room("Spice Rooms", "Spice is stacked in boxes in for ceremonies. You are aware of the power that it can"
                                  " bring from consumption, however the addiction can be fatal.\n There is only a path"
                                  " to the left leading out of the room.",
                   None, None, None, 'SIETCH')
FREMEN_PIT = Room("Fremen Pit", "A massive room with seating similar to a coliseum. Battle marks from swords line the"
                                " walls of the center pit.\n There is a staircase descending downwards and a path"
                                " leading east.", None, None, "SIETCH", None, None, "WATER")
WATER = Room("Water Storage", 'The water storage area of the sietch. You see tanks of water containing hundreds of'
                              ' liters kept in storage, all carefully counted for the tribe. The only way out is the'
                              ' staircase leading up.',
             None, None, None, None, "FREMEN_PIT")
DESERT2 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               'DESERT1', None, 'DESERT5')
DESERT3 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT6", 'DESERT5', 'DESERT7', 'DESERT1')
DESERT4 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               None, None, "DESERT1", "FUNERAL_PLAIN")
FUNERAL_PLAIN = Room("Funeral Plain", "The expanse of the desert only grows larger as you come across the Funeral"
                                      " Plain,\n where the Fremen take the dead. You are completely outside the reaches"
                                      " of so,ciety with no clear paths ahead of you.",
                     "GREAT_FLAT", "GREAT_FLAT", "DESERT4", "GREAT_FLAT")
GREAT_FLAT = Room("The Great Flat", "The farthest known point on the western half of the world. The only way out"
                                    " is back through the Funeral Plain.",
                  "FUNERAL_PLAIN", "FUNERAL_PLAIN", "FUNERAL_PLAIN")
DESERT5 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT3", None, "DESERT8", "DESERT2")
DESERT6 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "ROCKFACE", "DESERT3")
ROCKFACE = Room("Cliff side", "You come upon a cliff side in the desert. It is blocking the north and east, but it"
                              " appears scalable.",
                None, "DESERT6", None, "PATROL_STATION", "SIETCH_BALBOA")
SIETCH_BALBOA = Room("Sietch Balboa", "You find a massive door leading to another Sietch aligned with the Fremen."
                                      "The door appears locked and you don't know how to open it.",
                     None, None, None, None, "HEAVEN", "ROCKFACE")
PATROL_STATION = Room("Imperial Patrol Station", " As you make your way back to the city, you find an Imperial"
                                                 " Patrol Station."
                                                 "Imperial soldiers surround the massive stone barracks.\n"
                                                 " As you approach,"
                                                 "a guard notices you, and you realize you can only escape to the west",
                      None, None, None, "ROCKFACE", None, None, ["IMPERIAL1", "IMPERIAL2"])
DESERT7 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT6", "DESERT8", "STREET1", "DESERT3")
DESERT8 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT7", None, None, "DESERT5")
STREET1 = Room("Suburbs of Arrakeen", "Small houses line both sides of the dusty streets. Most of the doors are locked"
                                      " except for one orange house north of you. The street continues to the south.",
               "POPEYES", "STREET2", "MARKET", "DESERT7")
STREET2 = Room("Streets of Arrakeen", "You find a small alley corner. As you enter, you notice Imperial guards on the"
                                      " opposite side looking out for any Fremen. You could continue east or head "
                                      "north",
               "STREET1", None, "MARKET")
MARKET = Room("Arrakeen Market", "You find yourself at the central market of Arrakeen. There are shops selling food,"
                                 " water, and Stillsuit repairs.\n Looking to the north you see the entrance to the"
                                 " palace. The street continues to the south and west while the shield wall is on the "
                                 "east.",
              "PALACE", "STREET2", "SHIELD_WALL", "STREET1")
PALACE = Room("Palace Entrance", "You approach the massive palace. The massive gold throne and large, red banners"
                                 " hang down. The floor is velvet red carpet\n with the crest of the Harkonnens. "
                                 "The Council appears to meet the west and dine in a room to the east.",
              None, "MARKET", "DINE", "COUNCIL")
DINE = Room("Dining Hall", "The room is filled with a massive wooden table with food still sitting out, "
                           "accompanied by beautiful red decorations.\n"
                           "The massive banners hanging down symbol Imperial power. Above the head of the table is "
                           "the head of the bear that killed the old Duke.\n The entrance to the palace is to the west"
                           " and the private quarters are to the east.",
            None, None, "BEDROOM", "PALACE")
BEDROOM = Room("Private Quarters", "This is the private quarters of the Imperial. The walls are lined with swords and "
                                   "shields,\n which can be used in the training area north of the room. The only exit"
                                   " leading towards the center of the palace is west.",
               "TRAIN", None, None, "DINE")
TRAIN = Room("Training Room", " You enter a room of complete white. The only thing there is a small training dummy"
                              " with a sword in the center of the room.",
             None, "BEDROOM")
COUNCIL = Room("Council", "The location where all of the official government business takes place. The room is bland,"
                          " with only a round table.\n There appears to be something hidden on the underside of the"
                          " table. The only way out is to the east.",
               None, None, "PALACE", None, None, "WORM")
WORM = Room("Cellar", "You descend the hidden stairs to reveal a cellar. In the middle is a worm chained to the floor."
                      " \nIt appears that the Water of Life is being extracted from it and stored in containers along"
                      " with spice.",
            None, None, None, None, "COUNCIL")
HEAVEN = Room("Heaven", "You've found Heaven. Here, anything is possible as stacks of fried chicken and weapons are"
                        " everywhere.\n However, you search around and notice a small USB drive that appears to say "
                        "'call god'.",
              None, None, None, None, None, "SIETCH_BALBOA", ["Jack"])
SHIELD_WALL = Room("The shield wall is the eastern boundary of the city. Venturing beyond is too dangerous.",
                   None, None, None, "MARKET")
# Characters
player = Player(DESERT1)
IMPERIAL1 = Enemy(10, "The guard appears to be poorly trained, standing awkwardly with his sword. From the faint"
                      "glare you can tell that he is wearing a shield.", True)
Jack = Enemy(1, "Eldritch God", True)
IMPERIAL2 = Enemy(15, "An Imperial Captain")
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
while playing:
    print(player.current_location.name)
    print(player.current_location.desc)
    command = input(">_")
    if command.lower() in short_directions:
        index = short_directions.index(command.lower())
        command = directions[index]

    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command.lower())
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Found")
