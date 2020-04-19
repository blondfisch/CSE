
# derek jandrush = jared Kushner
# evil damages: hopelessness, stress, deceit
# good damges: Mr. Rogers = optimism, Bob Ross = tranquility, Carl Sagan = ensurement (matched up vertically with good strengths)
# tranquility weak to deceit
# ensurement weak to hopelessness
# optimism weak to stress
playername = input("Before you enter the fever dream, what is your name? >_")


class Player(object):
    def __init__(self, weapon, starting_location):
        self.hp = 100
        self.maxhp = 100
        self.inventory = []
        self.weapon = weapon
        self.name = playername
        self.current_location = starting_location
        self.weak = ["hopelessness", "stress", "deceit"]

    def take_dmg(self, enemy, dmg_type, dmg: int):
        global playing
        evade = random.randint(0, 10)
        if evade == 1:
            print("You evaded the attack!")
        else:
            if dmg_type in self.weak:
                dmg *= 1.5
                self.hp -= dmg
                if player.hp <= 0:
                    print("{0} hit you with a fatal {1} attack.".format(enemy.name, dmg_type))
                    playing = False
                else:
                    print("{0} used a crushing {1} attack! You now have {2} hp left.".format(enemy.name, dmg_type,
                                                                                             player.hp))
            else:
                self.hp -= dmg
                if player.hp <= 0:
                    print("{0} hit you with a fatal {1} attack.".format(enemy.name, dmg_type))
                    playing = False
                else:
                    print("{0} just attacked you with {1}! You have {2} hp left.".format(enemy.name, dmg_type,
                                                                                         player.health))

    def move(self, new_location):
        self.current_location = new_location

    def find_next_room(self, direction):
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


class NPC(object):
    def __init__(self, name, description, quality, weak):
        self.name = name
        self.description = description
        self.quality = quality
        self.weak = weak

    def bestow(self):
        player.weapon.dmg_type.append(self.quality)
        player.weak.remove(self.weak)


class Carl_Sagan(NPC):
    def __init__(self, name, description):
        super(NPC, self).__init__(name, description)
        self.name = name
        self.descritption = description
        self.dialogue1 = "Insert words here"
        self.dialogue2 = "Insert more words here. You have learned how to do the ensuring"
        self.dialogue3 = "You have defeated the ultimate evil. Congratulations on your victory"


class Enemy(object):
    def __init__(self, name, desc, hp, dmg_type, attack_dmg, weak=None):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.dmg_type = dmg_type
        self.weak = weak
        self.attack_dmg = attack_dmg

    def take_dmg(self, dmg_type, dmg: int):
        if self.weak in dmg_type:
            dmg *= 1.5
            self.hp -= dmg
            if self.hp <= 0:
                print("Using a critical strike of {0}, you attacked {1} and killed them!".format(dmg_type, self.name))
                player.current_location.enemies.remove(self)
            else:
                print("Using a critical strike of {0}, you attacked {1} and left them with {2} hp.".format(dmg_type,
                                                                                                           self.name,
                                                                                                           self.hp))
        else:
            self.hp -= dmg
            if self.hp <= 0:
                print("Using {0}, you killed {1}!".format(dmg_type, self.name))
                player.current_location.enemies.remove(self)
            else:
                print("You attacked {0} with an attack of {1}, leaving them with {2} hp.".format(self.name, dmg_type,
                                                                                                 self.hp))


class Slime(Enemy):
    def __init(self, name, desc, hp, dmg_type, attack_dmg, weak=None):
        super(Slime, self).__init__(name, desc, hp, dmg_type, attack_dmg, weak)
        self.name = name
        self.desc = desc
        self.hp = hp
        self.dmg_type = dmg_type
        self.weak = weak
        self.attack_dmg = attack_dmg


class Hopeless_Slime(Slime):
    def __init__(self):
        super(Hopeless_Slime, self).__init__("Hopeless Slime", "A ball of goo that instills a feeling of hopelessness"
                                                               " within you.", 10, "hopelessness", 5, "optimism")


slime_test = Hopeless_Slime()


class Stress_Slime(Slime):
    def __init__(self):
        super(Stress_Slime, self).__init__("Stressful Slime", "A ball of goo that makes your heart race as you are"
                                                              "filled with a sense of pure stress.", 10, "stress",
                                           "tranquility")


class Deceit_Slime(Slime):
    def __init__(self):
        super(Deceit_Slime, self).__init__("Deceitful Slime", "A ball of goo that seems to be made of lies and deceit.",
                                           10, "deceit", "ensurement")


class Object(object):
    def __init__(self, name):
        self.name = name


class Weapon(Object):
    def __init__(self, name, description, dmg):
        super(Weapon, self).__init__(name)
        self.name = name
        self.description = description
        self.dmg = dmg
        self.dmg_type = ["normal"]


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("")

class Consumable(Object):
    def __init__(self, name, desc):
        super(Object, self).__init__(name)
        self.name = name
        self.desc = desc


class Room(object):
    def __init__(self, name, desc, north, south, east, west, items=None, enemies=None, NPC=None):
        self.name = name
        self.desc = desc
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        if enemies is None:
            self.enemies = []
        else:
            self.enemies = enemies
        if NPC is None:
            self.npc = []
        else:
            self.npc = NPC
        if items is None:
            self.items = []
        else:
            self.items = items


# Defining the Player
player = Player(None, None)
playing = True

while playing:
    print("no")

