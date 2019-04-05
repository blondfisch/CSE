import random
import Objects


class Room(object):
    def __init__(self, name, desc, north=None, south=None, east=None, west=None, up=None, down=None,
                 items=None, characters=None, indoor=False):
        if characters is None:
            characters = []
        if items is None:
            items = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.desc = desc
        self.items = items
        self.characters = characters
        self.indoor = indoor


class Player(object):
    def __init__(self, starting_location, suit=None, weapon=None, wallet=0, defense=0):
        self.current_location = starting_location
        self.inventory = []
        self.sandslide = False
        self.suit = suit
        self.weapon = weapon
        self.wallet = wallet
        self.health = 200
        self.defense = defense

    def degrade(self):
        if self.suit.health > 0 and self.current_location.indoor is False:
            if self.current_location.indoor is False:
                self.suit.health -= 10
                if self.suit.health <= 0:
                    self.health -= 10
                    if self.health <= 0:
                        print("You died.")

    def take_damage(self, damage: int):
        if self.defense > damage:
            print("No damage taken")
        else:
            self.health -= damage - self.defense
            if self.health <= 0:
                self.health = 0
            print("You have %d health left" % self.health)

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


# Option 2 - set all at once, modify controller
# Objects
# Weapons
rapier1 = Objects.Rapier()
dullsword1 = Objects.DullSword()
broadsword1 = Objects.BroadSword()
crysknife1 = Objects.CrysKnife()
half_shield1 = Objects.HalfShield()
quart_shield1 = Objects.QuartShield()
rapier2 = Objects.Rapier()
dummy1 = Objects.Dummy()
spice1 = Objects.Spice()
full_shield1 = Objects.FullShield()
life1 = Objects.Life()
atomic1 = Objects.Bow()
lasgun1 = Objects.Lasgun()
needle1 = Objects.Needle()
crysknife2 = Objects.CrysKnife()
broadsword2 = Objects.BroadSword()
dullsword2 = Objects.DullSword()
wood_sword1 = Objects.WoodSword()
rapier3 = Objects.Rapier()
tooth1 = Objects.Tooth
# Armor

# Food
chicken1 = Objects.Chicken()
chicken2 = Objects.Chicken()
chicken3 = Objects.Chicken()
chicken4 = Objects.Chicken()
chicken5 = Objects.Chicken()
chicken6 = Objects.Chicken()
chicken7 = Objects.Chicken()
chicken8 = Objects.Chicken()
rice1 = Objects.Rice()
water1 = Objects.Water()
bread1 = Objects.Bread()
herb1 = Objects.Herb()
# Characters
gi1 = Objects.BaseSoldier()
gi2 = Objects.Sardaukar2()
worm1 = Objects.Worm()
fremen1 = Objects.Fremen()
captain = Objects.Captain
sard1 = Objects.Sardaukar1
sard2 = Objects.Sardaukar2

# Rooms
# Region 1 - The Desert
DESERT1 = Room("Open Desert", 'The sun beats down on the sandy desert all around you. There are caves to the north'
                              ' inside of the rock, a place of safety from the worms in the desert.\n On all other '
                              'sides is the desert.',
               "SIETCH", 'DESERT2', 'DESERT3', 'DESERT4')

SIETCH = Room("Sietch Tabr", 'You walk into a hidden Fremen cave. Inside, you find paths leading deeper into the'
                             ' chamber to the north and south.',
              None, 'DESERT1', 'SPICE_ROOMS', 'FREMEN_PIT', None, None, [quart_shield1, dullsword1])

SPICE_ROOMS = Room("Spice Rooms", "Spice is stacked in boxes in for ceremonies. You are aware of the power that it can"
                                  " bring from consumption, however the addiction can be fatal.\n There is only a path"
                                  " to the left leading out of the room.",
                   None, None, None, 'SIETCH', None, None, [spice1])

FREMEN_PIT = Room("Fremen Pit", "A massive room with seating similar to a coliseum. Battle marks from swords line the"
                                " walls of the center pit.\n There is a staircase descending downwards and a path"
                                " leading east.", None, None, "SIETCH", None, None, "WATER", [fremen1])

WATER = Room("Water Storage", 'The water storage area of the sietch. You see tanks of water containing hundreds of'
                              ' liters kept in storage, all carefully counted for the tribe.\n The only way out is the'
                              ' staircase leading up.',
             None, None, None, None, "FREMEN_PIT", None, [water1])

DESERT2 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you. This time, however, there"
                              " is a lonely Imperial Guard out on patrol.",
               'DESERT1', None, 'DESERT5', None, None, None, [rapier1], [gi1])

DESERT3 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT6", 'DESERT5', 'DESERT7', 'DESERT1', None, None, [], [])

DESERT4 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               None, None, "DESERT1", "FUNERAL_PLAIN", )

FUNERAL_PLAIN = Room("Funeral Plain", "The expanse of the desert only grows larger as you come across the Funeral"
                                      " Plain,\n where the Fremen take the dead. You are completely outside the reaches"
                                      " of society with no clear paths ahead of you.",
                     "GREAT_FLAT", "GREAT_FLAT", "DESERT4", "GREAT_FLAT", None, None, [], [fremen1])

GREAT_FLAT = Room("The Great Flat", "The farthest known point on the western half of the world. The only way out"
                                    " is back through the Funeral Plain. While here, a massive worm "
                                    "appears out of the ground.",
                  "FUNERAL_PLAIN", "FUNERAL_PLAIN", "FUNERAL_PLAIN", None, None, None, [], [worm1])

DESERT5 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT3", None, "DESERT8", "DESERT2", None, None, [], [])

DESERT6 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "ROCKFACE", "DESERT3", None, None, None, None, [], [fremen1])

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
                      None, None, None, "ROCKFACE", None, None, [], [gi1, captain])

DESERT7 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT6", "DESERT8", "STREET1", "DESERT3", None, None, [], [])

DESERT8 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT7", None, None, "DESERT5", None, None, [], [])

# Region 2 - The City

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

SHIELD_WALL = Room("Shield Wall",
                   "The shield wall is the eastern boundary of the city. Venturing beyond is too dangerous.",
                   None, None, None, "MARKET", None, None, [], [gi1, gi2])
# Region 3 - The Palace

PALACE = Room("Palace Entrance", "You approach the massive palace. The massive gold throne and large, red banners"
                                 " hang down. The floor is velvet red carpet\n with the crest of the Harkonnens. "
                                 "The Council appears to meet the west and dine in a room to the east.",
              None, "MARKET", "DINE", "COUNCIL", None, None, [], [], True)

DINE = Room("Dining Hall", "The room is filled with a massive wooden table with food still sitting out, "
                           "accompanied by beautiful red decorations.\n"
                           "The massive banners hanging down symbol Imperial power. Above the head of the table is "
                           "the head of the bear that killed the old Duke.\n The entrance to the palace is to the west"
                           " and the private quarters are to the east.",
            None, None, "BEDROOM", "PALACE", None, None, [], [], True)

BEDROOM = Room("Private Quarters", "This is the private quarters of the Imperial. The walls are lined with swords and "
                                   "shields,\n which can be used in the training area north of the room. The only exit"
                                   " leading towards the center of the palace is west.",
               "TRAIN", None, None, "DINE", None, None, [], [], True)

TRAIN = Room("Training Room", " You enter a room of complete white. The only thing there is a small training dummy"
                              " with a sword in the center of the room.",
             None, "BEDROOM", None, None, None, None, [], [dummy1], True)

COUNCIL = Room("Council", "The location where all of the official government business takes place. The room is bland,"
                          " with only a round table.\n There appears to be something hidden on the underside of the"
                          " table. The only way out is to the east.",
               None, None, "PALACE", None, None, "WORM", [], [], True)

WORM = Room("Cellar", "You descend the hidden stairs to reveal a cellar. In the middle is a worm chained to the floor."
                      " \nIt appears that the Water of Life is being extracted from it and stored in containers along"
                      " with spice.",
            None, None, None, None, "COUNCIL", None, [tooth1], [worm1])

HEAVEN = Room("Heaven", "You've found Heaven. Here, anything is possible as stacks of fried chicken and weapons are"
                        " everywhere.\n However, you search around and notice a small USB drive that appears to say "
                        "'call god'.",
              None, None, None, None, None, "SIETCH_BALBOA", [chicken1, chicken2, chicken3, chicken4, chicken5,
                                                              chicken6, chicken7], [], True)

# Region 4 - The Imperial


# Characters
player = Player(WATER)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
while playing:
    print(player.current_location.name)
    print(player.current_location.desc)
    if player.current_location.characters is None or player.current_location.characters is []:
        print("You are alone.")
    else:
        for i in range(len(player.current_location.characters)):
            character = player.current_location.characters[i]
            if len(player.current_location.characters) == 1:
                print("You are in a room with" + character.name)
            else:
                print("You are surrounded by:")
                print(character.name)
    command = input(">_")
    if command.lower() in short_directions:
        index = short_directions.index(command.lower())
        command = directions[index]
    elif command.lower() in ["q", "quit", "exit"]:
        playing = False
        print("Goodbye.")
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command.lower())
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    elif "take" in command.lower() or "t " in command.lower():
        if "take " in command.lower():
            item = command[5:]
        elif "t " in command.lower():
            item = command[2:]
        else:
            item = input("What do you want to take? >_")
        for number in range(len(player.current_location.items)):
            grab = player.current_location.items[number]
            if item.lower() in grab.grab or item == grab.name.lower():
                player.inventory.append(grab)
                player.current_location.items.remove(grab)
                print("You added %s to your inventory" % grab.name)
            elif item.lower() not in grab.grab or item != grab.name.lower():
                print("I don't know what you want to take.")
            elif item.lower() in ["", " "]:
                print("You have to actually take something.")
            elif range(len(player.current_location.items)) == 0:
                print("There is nothing left to take.")
    elif command.lower() in ["inventory", "i"]:
        for i in range(len(player.inventory)):
            item = player.inventory[i]
            print(item.name)
    elif "purchase " in command.lower() or "p " in command.lower():
        if "purchase " in command.lower():
            item = command[9:]
        elif "p " in command.lower():
            item = command[2:]
        else:
            item = input("What do you want to purchase?")
        for thing in range(len(player.current_location.items)):
            grab = player.current_location.items[thing]
            if item.lower() in grab.grab or item == grab.name.lower() \
                    and player.wallet >= grab.value and player.current_location == MARKET:
                player.inventory.append(grab)
                player.wallet -= grab.value
            if player.wallet < grab.value and item.lower() in grab.grab or item == grab.name.lower():
                print("You are too poor to purchase such an item, peasant.")
            elif player.current_location != MARKET:
                print("Bold of you to assume you could purchase something while not at a market.")
    elif "attack " in command.lower() or "hit" in command.lower() or "murder" in command.lower():
        if " " * 3 in command.lower():
            jac = command.lower().split()
            target = jac[1]
            weapon = jac[3]
        else:
            weapon = input("What do you want to attack with? >_")
            target = input("Who do you want to attack?")
        for i in range(len(player.current_location.characters)):
            char = player.current_location.characters[i]
            if target in char.name:
                target = char
        for i in range(len(player.inventory)):
            item = player.inventory[i]
            if weapon in item.name or weapon in item.grab:
                player.weapon = item
        if player.weapon not in player.inventory:
            print("You cannot use that because you do not have it.")
        if player.weapon.durability <= 0 or player.weapon.durability - 1 == 0:
            print("The weapon broke and the attack failed.")
        elif target.health <= 0:
                print("You're attacking a dead person")
        else:
            target.take_damage(player.weapon.damage)
            if target.health - player.weapon.damage > 0:
                    print("You attack %s for %d damage" % (target.name, player.weapon.damage))
                    target.health -= player.weapon.damage
            if target.health <= 0:
                print("%s died." % target.name)
            player.weapon.use()
    elif "consume" in command.lower() or "use" in command.lower() or "eat" in command.lower() \
        or "drink" in command.lower():
        
    else:
        print("Command Not Found")
