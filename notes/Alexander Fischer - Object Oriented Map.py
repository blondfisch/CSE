class Room(object):
    def __init__(self, name, descrip, north=None, south=None, east=None, west=None, up=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.descrip = descrip


# Option 2 - set all at once, modify controller
DESERT1 = Room("Open Desert", 'The sun beats down on the sandy desert all around you. There are caves to the north'
                              ' inside of the rock, a place of safety from the worms in the desert. On all other sides'
                              ' is the desert.',
               "SIETCH", 'DESERT2', 'DESERT3', 'DESERT4')
SIETCH = Room("Sietch Tabr", 'You walk into a hidden Fremen cave. Inside, you find a Stillsuit folded in a '
                             'corner, as well as paths leading deeper into the chamber'
                             ' to the north and south.',
              None, 'DESERT1', 'SPICE_ROOMS', 'FREMEN_PIT')
SPICE_ROOMS = Room("Spice Rooms", "Spice is stacked in boxes in for ceremonies. You are aware of the power that it can"
                                  " bring from consumption, however the addiction can be fatal. There is only a path"
                                  " to the left leading out of the room.",
                   None, None, None, 'SIETCH')
FREMEN_PIT = Room("Fremen Pit", "A massive room with seating similar to a coliseum. Battle marks from swords line the"
                                " walls of the center pit. There is a staircase descending downwards and a path"
                                " leading east.", None, None, "SIETCH", None, None, "WATER")
WATER = Room("Water Storage", 'The water storage area of the sietch. You see tanks of water containing hundreds of'
                              ' liters kept in storage, all carefully counted for the tribe. The only way out is the'
                              ' staircase leading up.',
             None, None, None, None, "FREMEN_PIT")
DESERT2 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert before the lack of water or Imperials kill you.",
               'DESERT1', None, 'DESERT5')
DESERT3 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert before the lack of water or Imperials kill you.",
               "DESERT6", 'DESERT5', 'DESERT7', 'DESERT1')
DESERT4 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert before the lack of water or Imperials kill you.",
               None, None, "DESERT1", "FUNERAL_PLAIN")
FUNERAL_PLAIN = Room("Funeral Plain", "The expanse of the desert only grows larger as you come across the Funeral"
                                      " Plain, where the Fremen take the dead. You are completely outside the reaches"
                                      " of so,ciety with no clear paths ahead of you.",
                     "GREAT_FLAT", "GREAT_FLAT", "DESERT4", "GREAT_FLAT")
GREAT_FLAT = Room("The Great Flat", "The farthest known point on the western half of the world. The only way out"
                                    " is back through the Funeral Plain.",
                  "FUNERAL_PLAIN", "FUNERAL_PLAIN", "FUNERAL_PLAIN")
DESERT5 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert before the lack of water or Imperials kill you.",
               "DESERT3", None, "DESERT8", "DESERT2")
DESERT6 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert before the lack of water or Imperials kill you.",
               "ROCKFACE", "DESERT3")
ROCKFACE = Room("Cliff side", "You come upon a cliff side in the desert. It is blocking the north and east, but it"
                              " appears scalable.",
                None, "DESERT6", None, "PATROL_STATION", "SIETCH_BALBOA")
SIETCH_BALBOA = Room("Sietch Balboa", "You find a massive door leading to another Sietch aligned with the Fremen."
                                      "The door appears locked and you don't know how to open it.",
                     None, None, None, None, "HEAVEN", "ROCKFACE")
PATROL = Room("Imperial Patrol Station", " As you make your way back to the city, you find an Imperial Patrol Station."
                                         "Imperial soldiers surround the massive stone barracks. As you approach,"
                                         " a guard notices you, and you realize you can only escape to the west",
              None, None, None, "ROCKFACE")
DESERT7 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert before the lack of water or Imperials kill you.",
               "DESERT6", "DESERT8", "STREET1", "DESERT3")
DESERT8 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert before the lack of water or Imperials kill you.",
               "DESERT7", None, None, "DESERT5")
STREET1 = Room("Suburbs of Arrakeen", "Small houses line both sides of the dusty streets. Most of the doors are locked"
                                      " except for one orange house north of you. The street continues to the south.",
               "POPEYES", "STREET2", "MARKET", "DESERT7")
STREET2 = Room("Streets of Arrakeen", "You find a small alley corner. As you enter, you notice Imperial guards on the"
                                      " opposite side looking out for any Fremen. You could continue east or head "
                                      "north",
               "STREET1", None, "MARKET")
