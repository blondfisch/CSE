import random
import Objects


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage: int, distance: int):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.range = distance


class Sword(Weapon):
    def __init__(self, name, damage: int, durability: int, desc, grab=None):
        super(Sword, self).__init__(name, damage, durability)
        self.name = name
        self.damage = damage
        self.distance = 0
        self.durability = durability
        self.desc = desc
        self.grab = grab

    def use(self):
        if self.durability <= 0:
            print("Your sword is broken.")
        else:
            self.durability -= 1


class WoodSword(Sword):
    def __init__(self):
        super(WoodSword, self).__init__("Wooden Sword", 15, 60, "A wooden sword. It's not the best option",
                                        ["wood sword", "sword", "wooden sword"])


class Rapier(Sword):
    def __init__(self):
        super(Rapier, self).__init__("Rapier", 7, 50, "A sharp rapier sword. It is in excellent condition and will"
                                                      " do massive damage to enemies.",
                                     ["rapier", "sword"])


class DullSword(Sword):
    def __init__(self):
        super(DullSword, self).__init__("Dull Sword", 10, 25, "A dull sword. It has not been well maintained and is on"
                                                              " the verge of breaking.",
                                        ["sword", "dull sword", "dullsword"])


class BroadSword(Sword):
    def __init__(self):
        super(BroadSword, self).__init__("Broadsword", 25, 40, "This sword is quite heavy and will wear out quickly"
                                                               "but does massive damage.",
                                         ["broadsword", "sword", "broad sword", "sword"])


class CrysKnife(Sword):
    def __init__(self):
        super(CrysKnife, self).__init__("Crysknife", 8, 100, "This knife is made from the teeth of a worm. While not"
                                                             " very sharp, it will undergo a lot of use before it"
                                                             " breaks.",
                                        ["knife", "crysknife"])


class Needle(Sword):
    def __init__(self):
        super(Needle, self).__init__("Poisoned Needle", 100, 1, "A poisoned needle. Can only be used once but does "
                                                                "massive damage to enemies",
                                     ["poisoned needle", "needle", "poisonedneedle"])


class Tooth(Sword):
    def __init__(self):
        super(Tooth, self).__init__("Nothing here", 0, 1000000, "You shouldn't care.",
                                    ["tooth", "object"])


class Gun(Weapon):
    def __init__(self, name, damage: int, durability: int, grab=None):
        super(Gun, self).__init__(name, damage, 1)
        self.name = name
        self.damage = damage
        self.distance = 1
        self.durability = durability
        self.grab = grab

    def use(self):
        if self.durability <= 0:
            print("Your gun is broken.")
        else:
            self.durability -= 1


class Lasgun(Gun):
    def __init__(self):
        super(Lasgun, self).__init__("Lasgun", 20, 30, ["gun", "lasgun"])


class Bow(Gun):
    def __init__(self):
        super(Bow, self).__init__("Bow and Arrow", 5, 50, ["bow", "bow and arrow"])


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name)
        self.name = name
        self.desc = description


class Food(Consumable):
    def __init__(self, name, description, health, grab=None):
        super(Consumable, self).__init__(name)
        self.name = name
        self.desc = description
        self.health = health
        self.grab = grab


class Bread(Food):
    def __init__(self):
        super(Bread, self).__init__("Bread", "This is a piece of bread. It can be eaten for health.", 25, "bread")


class Water(Food):
    def __init__(self):
        super(Water, self).__init__("Water", "Arguably the most valuable item on the planet, water heals you massive"
                                             " amounts but is very rare.", 50, ["water", "h2o", "aqua"])


class Rice(Food):
    def __init__(self):
        super(Rice, self).__init__("Rice", "This item can be eaten for health. It is rather common on the planet.", 15,
                                   "rice")


class Chicken(Food):
    def __init__(self):
        super(Chicken, self).__init__("Fried Chicken", "This glorious chicken hails from heaven and heals you for all"
                                                       " damage you may have taken. Use wisely.", 100,
                                      ["chicken", "fried chicken", "friedchicken"])


class Herb(Food):
    def __init__(self):
        super(Herb, self).__init__("Herbs", "Common Herbs. They are plentiful but heal for only a small amount", 10,
                                   ["herb", "herbs"])


class Potion(Consumable):
    def __init__(self, name, description, damage: int, grab=None):
        super(Potion, self).__init__(name, description)
        self.damage = damage
        self.grab = grab


class Life(Potion):
    def __init__(self):
        super(Life, self).__init__("Water of Life", "An incredibly dangerous item. Consuming the Water of Life could "
                                                    "kill you or grant you superhuman strength.", 30,
                                   ["water of life", "water", "life"])


class Spice(Potion):
    def __init__(self):
        super(Spice, self).__init__("The Spice", "An addicting substance but it grants special strengths. Your attacks"
                                                 " will do more damage, but you will need to keep consuming spice.",
                                    20, ["spice", "the spice", "melange"])


class Armor(Item):
    def __init__(self, name, desc, defense: int, shield, grab=None):
        super(Armor, self).__init__(name)
        self.name = name
        self.desc = desc
        self.defense = defense
        self.shield = shield
        self.grab = grab


class FullShield(Armor):
    def __init__(self):
        super(FullShield, self).__init__("Full body shield", "This shield is incredibly powerful because it covers the"
                                                             "entire body.", 40, True,
                                         ["shield", "full shield", "best shield", "shield"])


class HalfShield(Armor):
    def __init__(self):
        super(HalfShield, self).__init__("Half Shield", "This shield has been worn down from use and only covers"
                                                        "half of the body.", 10, True,
                                         ["halfshield", "half shield", "shield"])


class QuartShield(Armor):
    def __init__(self):
        super(QuartShield, self).__init__("Quarter Shield", "A quarter shield, covering just a small part of the body",
                                          5, True,
                                          ["quarter shield", "quartershield", "quartshield", "shield"])


class Suit(Item):
    def __init__(self, name, health, grab=None):
        super(Suit, self).__init__(name)
        self.health = health
        self.grab = grab


class FremenSuit(Suit):
    def __init__(self):
        super(FremenSuit, self).__init__("Fremen Stillsuit", 500, ["suit", "fremen suit", "fremensuit"])


class ImperialSuit(Suit):
    def __init__(self):
        super(ImperialSuit, self).__init__("Imperial Stillsuit", 320, ["suit", "imperial suit", "imperialsuit"])


class StarterSuit(Suit):
    def __init__(self):
        super(StarterSuit, self).__init__("Low Quality Suit", 220, ["basic suit", "suit", "bad suit"])


class Money(Item):
    def __init__(self, name, value, grab=None):
        super(Money, self).__init__(name)
        self.name = name
        self.value = value
        self.grab = grab


class BigNote(Money):
    def __init__(self):
        super(BigNote, self).__init__("100 note bill", 100)


class SmallNote(Money):
    def __init__(self):
        super(SmallNote, self).__init__("10 note bill", 10)


class Enemy(object):
    def __init__(self, name, health: int, defense, weapon, desc=None, inven=None):
        if inven is None:
            inven = []
        self.health = health
        self.desc = desc
        self.items = []
        self.defense = defense
        self.name = name
        self.weapon = weapon
        self.inventory = inven

    def take_damage(self, damage: int):
        if self.defense > damage:
            print("No damage taken")
        else:
            self.health -= damage - self.defense
            if self.health <= 0:
                self.health = 0
            print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        weapon = input("What do you want to attack with? >_")
        if weapon not in self.inventory:
            print("You cannot use that")
        if self.weapon.durability <= 0:
            print("The weapon broke and the attack failed.")
        elif target.health <= 0:
            print("You're attacking a dead person")
        else:
            target.take_damage(self.weapon.damage)
            if target.health - self.weapon.damage > 0:
                print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
                target.health -= self.weapon.damage
            if target.health <= 0:
                print("%s died." % target.name)
            self.weapon.durability -= 1


class BaseSoldier(Enemy):
    def __init__(self):
        super(BaseSoldier, self).__init__("Imperial", 50, 0, DullSword(), "A basic Imperial soldier. He is not well "
                                                                          "equipped and does not have a shield.")


class Captain(Enemy):
    def __init__(self):
        super(Captain, self).__init__("Imperial Captain", 75, 50, Rapier(), "An Imperial Captain. He has a more"
                                                                            " advanced "
                                                                            "training and is wearing a shield.")


class Baron(Enemy):
    def __init__(self):
        super(Baron, self).__init__("The Baron", 200, 0, BroadSword(), "The Baron. He is extremely well trained and"
                                                                       " is very fast. His attacks will kill you "
                                                                       "quickly"
                                                                       " if you are unprepared, in the same way that he"
                                                                       " killed your parents.")


class Fremen(Enemy):
    def __init__(self):
        super(Fremen, self).__init__("Fremen", 50, 0, CrysKnife(), "A Fremen soldier. While not formally trained, they"
                                                                   " are great fighters and are incredibly"
                                                                   " dangerous. Clearly this one is not happy that"
                                                                   " you took his items.")


class Sardaukar1(Enemy):
    def __init__(self):
        super(Sardaukar1, self).__init__("Sardaukar", 125, 0, BroadSword(), "The Sardaukar are the top soldiers of the"
                                                                            " Empire. They have expert training and can"
                                                                            " take extreme amounts of pain. "
                                                                            "Tread lightly.")


class Sardaukar2(Enemy):
    def __init__(self):
        super(Sardaukar2, self).__init__("Sardaukar", 125, 12, Lasgun(), "The Sardaukar are the top soldiers of the"
                                                                         " Empire. They have expert training and can"
                                                                         " take extreme amounts of pain. Tread lightly."
                                         )


class Emperor(Enemy):
    def __init__(self):
        super(Emperor, self).__init__("The Emperor", 500, 50, BroadSword(), "The leader of the known universe stands "
                                                                            "before you. This man has killed hundreds"
                                                                            " and is a"
                                                                            " machine. He wears his imperial shield.")


class Worm(Enemy):
    def __init__(self):
        super(Worm, self).__init__("Worm", 1000, 0, Tooth(), "A worm. A massive creature stretching over one thousand"
                                                             " yards. You could fight the massive creature but will "
                                                             "likely be crushed.")


class Dummy(Enemy):
    def __init__(self):
        super(Dummy, self).__init__("Dummy", 1000000000000, 0, None, "A training dummy. You could hit it, "
                                                                     "if you wanted to.")


half_shield = HalfShield()
quart_shield = QuartShield()
sword = Rapier()
dummy = Dummy()
spice = Spice()
full_shield = FullShield()
life = Life()
herb = Herb()
chicken = Chicken()
rice = Rice()
water = Water()
bread = Bread()
atomic = Bow()
lasgun = Lasgun()
needle = Needle()
crysknife = CrysKnife()
broadsword = BroadSword()
dull = DullSword()
wood_sword = WoodSword()
rapier = Rapier()


baron = Baron()
worm = Worm()
tooth = Tooth()
fremen = Fremen()
soldier = BaseSoldier()


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
    def __init__(self, starting_location, suit=None, weapon=None, wallet=0, defense=0, eweap=None, earmor=None):
        self.current_location = starting_location
        self.inventory = []
        self.sandslide = False
        self.suit = suit
        self.weapon = weapon
        self.wallet = wallet
        self.health = 200
        self.defense = defense
        self.consum = 0
        self.damage = 4
        self.equiparmor = eweap
        self.equipweapon = earmor

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
            print("You took no damage.")
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
rapier1 = Rapier()
dullsword1 = DullSword()
broadsword1 = BroadSword()
crysknife1 = CrysKnife()
rapier2 = Rapier()
dummy1 = Dummy()
full_shield1 = FullShield()
life1 = Life()
atomic1 = Bow()
lasgun1 = Lasgun()
needle1 = Needle()
crysknife2 = CrysKnife()
broadsword2 = BroadSword()
dullsword2 = DullSword()
wood_sword1 = WoodSword()
rapier3 = Rapier()
tooth1 = Tooth
# Armor
half_shield1 = HalfShield
half_shield2 = HalfShield
quart_shield2 = QuartShield
quart_shield1 = QuartShield()
# Food
chicken1 = Chicken()
chicken2 = Chicken()
chicken3 = Chicken()
chicken4 = Chicken()
chicken5 = Chicken()
chicken6 = Chicken()
chicken7 = Chicken()
chicken8 = Chicken()
spice1 = Spice()
spice2 = Spice()
spice3 = Spice()
spice4 = Spice()
spice5 = Spice()
rice1 = Rice()
water1 = Water()
bread1 = Bread()
herb1 = Herb()
water2 = Water()
water3 = Water()
water4 = Water()
water5 = Water()
water6 = Water()
water7 = Water()
water8 = Water()

# Characters
gi1 = BaseSoldier()
gi2 = Sardaukar2()
worm1 = Worm()
fremen1 = Fremen()
captain = Captain
sard1 = Sardaukar1()
sard2 = Sardaukar2()

# Rooms
# Region 1 - The Desert
DESERT1 = Room("Open Desert", 'The sun beats down on the sandy desert all around you. There are caves to the north'
                              ' inside of the rock, a place of safety from the worms in the desert.\n On all other '
                              'sides is the desert.',
               "SIETCH", 'DESERT2', 'DESERT3', 'DESERT4')

SIETCH = Room("Sietch Tabr", 'You walk into a hidden Fremen cave. Inside, you find paths leading deeper into the'
                             ' chamber to the east and west.',
              None, 'DESERT1', 'SPICE_ROOMS', 'FREMEN_PIT', None, None, [quart_shield1, dullsword1])

SPICE_ROOMS = Room("Spice Rooms", "Spice is stacked in boxes in for ceremonies. You are aware of the power that it can"
                                  " bring from consumption, however the addiction can be fatal.\n There is only a path"
                                  " to the left leading out of the room.",
                   None, None, None, 'SIETCH', None, None, [spice1, spice2])

FREMEN_PIT = Room("Fremen Pit", "A massive room with seating similar to a coliseum. Battle marks from swords line the"
                                " walls of the center pit.\n There is a staircase descending downwards and a path"
                                " leading east.", None, None, "SIETCH", None, None, "WATER", [crysknife1], [fremen1])

WATER = Room("Water Storage", 'The water storage area of the sietch. You see tanks of water containing hundreds of'
                              ' liters kept in storage, all carefully counted for the tribe.\n The only way out is the'
                              ' staircase leading up.',
             None, None, None, None, "FREMEN_PIT", None, [water1, water1, water1], [fremen1])

DESERT2 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you. This time, however, there"
                              " is a lonely Imperial Guard out on patrol.",
               'DESERT1', None, 'DESERT5', None, None, None, [dullsword2], [gi1])

DESERT3 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT6", 'DESERT5', 'DESERT7', 'DESERT1', None, None, [wood_sword1], [fremen1])

DESERT4 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               None, None, "DESERT1", "FUNERAL_PLAIN", None, None, [atomic1], [fremen1])

FUNERAL_PLAIN = Room("Funeral Plain", "The expanse of the desert only grows larger as you come across the Funeral"
                                      " Plain,\n where the Fremen take the dead. You are completely outside the reaches"
                                      " of society with no clear paths ahead of you.",
                     "GREAT_FLAT", "GREAT_FLAT", "DESERT4", "GREAT_FLAT", None, None, [dullsword1], [fremen1, fremen1])

GREAT_FLAT = Room("The Great Flat", "The farthest known point on the western half of the world. The only way out"
                                    " is back through the Funeral Plain. While here, a massive worm "
                                    "appears out of the ground.",
                  "FUNERAL_PLAIN", "FUNERAL_PLAIN", "FUNERAL_PLAIN", None, None, None, [], [worm1, fremen1])

DESERT5 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "DESERT3", None, "DESERT8", "DESERT2", None, None, [], [fremen1, fremen1])


DESERT6 = Room("Open Desert", "The sun beats down on the sandy desert all around you. You need to find a way out of"
                              " the desert\n before the lack of water or Imperials kill you.",
               "ROCKFACE", "DESERT3", None, None, None, None, [], [fremen1])

ROCKFACE = Room("Cliff side", "You come upon a cliff side in the desert. It is blocking the north and east, but it"
                              " appears scalable.",
                None, "DESERT6", None, "PATROL_STATION", "SIETCH_BALBOA")

SIETCH_BALBOA = Room("Sietch Balboa", "You find a massive door leading to another Sietch aligned with the Fremen."
                                      "The door appears locked and you don't know how to open it.",
                     None, None, None, None, "HEAVEN", "ROCKFACE", [broadsword2, water6])

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
               "DESERT7", None, None, "DESERT5", None, None, [], [fremen1])

# Region 2 - The City

STREET1 = Room("Suburbs of Arrakeen", "Small houses line both sides of the dusty streets. Most of the doors are locked"
                                      " except for one orange house north of you. The street continues to the south.",
               "POPEYES", "STREET2", "MARKET", "DESERT7", None, None, [], [gi1, gi2, gi1])

STREET2 = Room("Streets of Arrakeen", "You find a small alley corner. As you enter, you notice Imperial guards on the"
                                      " opposite side looking out for any Fremen. You could continue east or head "
                                      "north",
               "STREET1", None, "MARKET")

MARKET = Room("Arrakeen Market", "You find yourself at the central market of Arrakeen. There are shops selling food,"
                                 " water, and Stillsuit repairs.\n Looking to the north you see the entrance to the"
                                 " palace. The street continues to the south and west while the shield wall is on the "
                                 "east.",
              "PALACE", "STREET2", "SHIELD_WALL", "STREET1", None, None,
              [BroadSword(), Rapier(), HalfShield(), QuartShield(), CrysKnife(),
               Bow(), Lasgun(), ImperialSuit(), Bread(), Chicken()
               ])

SHIELD_WALL = Room("Shield Wall",
                   "The shield wall is the eastern boundary of the city. Venturing beyond is too dangerous.",
                   None, None, None, "MARKET", None, None, [quart_shield2], [gi1, gi2])
# Region 3 - The Palace

PALACE = Room("Palace Entrance", "You approach the massive palace. The massive gold throne and large, red banners"
                                 " hang down. The floor is velvet red carpet\n with the crest of the Harkonnens. "
                                 "The Council appears to meet the west and dine in a room to the east.",
              None, "MARKET", "DINE", "COUNCIL", None, None, [broadsword1], [sard1, sard1], True)

DINE = Room("Dining Hall", "The room is filled with a massive wooden table with food still sitting out, "
                           "accompanied by beautiful red decorations.\n"
                           "The massive banners hanging down symbol Imperial power. Above the head of the table is "
                           "the head of the bear that killed the old Duke.\n The entrance to the palace is to the west"
                           " and the private quarters are to the east.",
            None, None, "BEDROOM", "PALACE", None, None, [bread1, spice4, water3], [sard1, sard2, captain], True)

BEDROOM = Room("Private Quarters", "This is the private quarters of the Imperial. The walls are lined with swords and "
                                   "shields,\n which can be used in the training area north of the room. The only exit"
                                   " leading towards the center of the palace is west.",
               "TRAIN", None, None, "DINE", None, None, [full_shield1], [sard1, sard2], True)

TRAIN = Room("Training Room", " You enter a room of complete white. The only thing there is a small training dummy"
                              " with a sword in the center of the room.",
             None, "BEDROOM", None, None, None, None, [rapier2], [dummy1], True)

COUNCIL = Room("Council", "The location where all of the official government business takes place. The room is bland,"
                          " with only a round table.\n There appears to be something hidden on the underside of the"
                          " table. The only way out is to the east.",
               None, None, "PALACE", None, None, "WORM", [], [sard1, sard2, Objects.Baron], True)

WORM = Room("Cellar", "You descend the hidden stairs to reveal a cellar. In the middle is a worm chained to the floor."
                      " \nIt appears that the Water of Life is being extracted from it and stored in containers along"
                      " with spice.",
            None, None, None, None, "COUNCIL", None, [], [worm1])

HEAVEN = Room("Heaven", "You've found Heaven. Here, anything is possible as stacks of fried chicken and weapons are"
                        " everywhere.\n However, you search around and notice a small USB drive that appears to say "
                        "'call god'.",
              None, None, None, None, None, "SIETCH_BALBOA", [chicken1, chicken2, chicken3, chicken4, chicken5,
                                                              chicken6, chicken7], [], True)

# Region 4 - The Imperial


# Characters
player = Player(DESERT1)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
print('''You are the lost heir to the ''')
while playing:
    print("_ _ _ _ _ _ _ _ _ _ _")
    print()
    print(player.current_location.name)
    print(player.current_location.desc)
    if player.current_location.characters is None or player.current_location.characters is []:
        print("You are alone.")
    else:
        for i in range(len(player.current_location.characters)):
            character = player.current_location.characters[i]
            if len(player.current_location.characters) == 1:
                print("You are in a room with " + character.name)
            else:
                print("You are surrounded by:")
                print(character.name)
    if player.current_location.items is None or player.current_location.items is []:
        print("There is nothing for you to take.")
    else:
        for i in range(len(player.current_location.items)):
            thingy = player.current_location.items[i]
            if len(player.current_location.items) == 1:
                print("You can take " + thingy.name)
            else:
                print("You see a " + thingy.name)
    command = input(">_")
    if command.lower() in short_directions:
        index = short_directions.index(command.lower())
        command = directions[index]
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
        print("Goodbye.")
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command.lower())
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    elif "take" in command.lower() or "t " in command.lower() or "grab " in command.lower():
        if "take " in command.lower() or "grab" in command.lower():
            item = command[5:]
        elif "t " in command.lower():
            item = command[2:]
        else:
            item = input("What do you want to take? >_")
            print(item)
        for i in player.current_location.items:
            grab = i
            """if len(player.current_location.items) > 1 and item in "all":
                player.inventory.append(player.current_location.items)"""
            if item.lower() in grab.grab or item.lower() in grab.name.lower():
                if type(grab) is Objects.Money:
                    player.wallet += grab.value
                    print("You added %d coins to your wallet" % grab.value)
                else:
                    player.inventory.append(grab)
                    player.current_location.items.remove(grab)
                    print("You added %s to your inventory" % grab.name)
            elif item.lower() in ["", " "]:
                print("You have to actually take something.")
            elif range(len(player.current_location.items)) == 0:
                print("There is nothing left to take.")
    elif command.lower() in "inventory" or command.lower() == "i":
        print("You have:")
        for i in player.inventory:
            item = i
            print(item.name)
    elif "purchase " in command.lower():
        if "purchase " in command.lower():
            item = command[9:]
        else:
            item = input("What do you want to purchase?")
        for thing in player.current_location.items:
            grab = thing
            if item.lower() in grab.grab or item == grab.name.lower() \
                    and player.wallet >= grab.value and player.current_location == MARKET:
                player.inventory.append(grab)
                player.wallet -= grab.value
            if player.wallet < grab.value and item.lower() in grab.grab or item == grab.name.lower():
                print("You are too poor to purchase such an item, peasant.")
            elif player.current_location != MARKET:
                print("Bold of you to assume you could purchase something while not at a market.")
    elif "attack " in command.lower() or "hit" in command.lower() or "murder" in command.lower() or\
            "attack" in command.lower():
        if len(command.lower().split()) == 4:
            jac = command.lower().split()
            target = jac[1]
            weapon = jac[3]
        else:
            weapon = input("What do you want to attack with? >_")
            target = input("Who do you want to attack? >_")
        for i in player.current_location.characters:
            char = i
            if target.lower() in char.name.lower():
                target = char
        if weapon.lower() in player.equipweapon.name.lower() or weapon.lower() in player.equipweapon.grab:
            player.weapon = player.equipweapon
            player.damage = player.weapon.damage + player.consum
        else:
            for g in player.inventory:
                if weapon.lower() in g.name.lower() or weapon in g.grab:
                    player.weapon = g
                    player.damage = player.weapon.damage + player.consum
        if weapon.lower() not in player.inventory and weapon.lower() not in player.equipweapon.name and\
                weapon.lower() not in player.equipweapon.grab:
            print("You cannot use that because you do not have it.")
        if player.weapon.durability <= 0 or player.weapon.durability - 1 == 0:
            print("The weapon broke and the attack failed.")
        elif target.health <= 0:
            print("You're attacking a dead person")
        else:
            target.take_damage(player.damage)
            if target.health - player.damage > 0:
                    print("You attack %s for %d damage" % (target.name, player.damage))
                    target.health -= player.damage
            if target.health <= 0:
                print("%s died." % target.name)
                player.current_location.characters.remove(target)
            player.weapon.use()
            player.take_damage(target.weapon.damage)
            print("You were attacked for %d damage and have %d health left." % (target.weapon.damage - player.defense,
                                                                                player.health))
    elif "consume" in command.lower() or "use" in command.lower() or "eat" in command.lower() or\
            "drink" in command.lower():
        temp = command.lower().split()
        obj = temp[1]
        for i in player.inventory:
            if obj in i.name or obj in i.grab:
                obj = i
            player.inventory.remove(i)
        if issubclass(type(obj), Food):
            player.health += obj.health
            print("You increased your health to %d" % player.health)
        elif issubclass(type(obj), Potion):
            player.consum += obj.damage
            print("You increased your damage by %d" % player.consum)
    elif "equip " in command.lower() or "equip" in command.lower():
        if len(command.lower().split()) == 2:
            templist = command.lower().split()
            goal = templist[1]
        else:
            goal = input("What do you want to equip? >_")
        for i in player.inventory:
            if goal.lower() in i.name.lower() or goal.lower() in i.grab:
                goal = i
                player.inventory.remove(goal)
        if issubclass(type(goal), Armor):
            player.equiparmor = goal
            print(player.equiparmor)
            player.defense = player.equiparmor.defense
        elif issubclass(type(goal), Weapon):
            player.equipweapon = goal
            print(player.equipweapon.name)
    else:
        print("Command Not Found")
