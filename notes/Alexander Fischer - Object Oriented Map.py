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
                              ' is the desert.', "SIETCH", 'DESERT2', 'DESERT3', 'DESERT4')
SIETCH = Room("Sietch Tabr", 'You walk into a hidden Fremen cave. Inside, you find a Stillsuit folded in a '
                             'corner, as well as paths leading deeper into the chamber'
                             ' to the north and south.', None, 'DESERT1', 'SPICE_ROOMS', 'FREMEN_PIT')
SPICE_ROOMS = Room("Spice Rooms", "Spice is stacked in boxes")
