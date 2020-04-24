
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
    def __init__(self, name, quality, weak):
        self.name = name
        self.quality = quality
        self.weak = weak

    def bestow(self):
        player.weapon.dmg_type.append(self.quality)
        player.weak.remove(self.weak)


class Sagan(NPC):
    def __init__(self):
        super(Sagan, self).__init__("Carl Sagan", "ensurement", "deceit")
        self.dialogue1 = "Insert words here"
        self.dialogue2 = "Insert more words here. You have learned how to do the ensuring"
        self.dialogue3 = "You have defeated the ultimate evil. Congratulations on your victory"


class Rogers(NPC):
    def __init__(self):
        super(Rogers, self).__init__("Mr. Rogers", "optimism", "hopelessness")


class Ross(NPC):
    def __init__(self):
        super(Ross, self).__init__("Bob Ross", "tranquility", "stress")


# The NPCs
sagan = Sagan()
ross = Ross()
rogers = Rogers()


class Enemy(object):
    def __init__(self, name, desc, dmg_type, attack_dmg, hp=0, weak=None):
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
                player.take_dmg(player, self.dmg_type, self.attack_dmg)
        else:
            self.hp -= dmg
            if self.hp <= 0:
                print("Using {0}, you killed {1}!".format(dmg_type, self.name))
                player.current_location.enemies.remove(self)
            else:
                print("You attacked {0} with an attack of {1}, leaving them with {2} hp.".format(self.name, dmg_type,
                                                                                                 self.hp))
                player.take_dmg(player, self.dmg_type, self.attack_dmg)


class Slime(Enemy):
    def __init(self, name, desc, dmg_type, attack_dmg, hp=0, weak=None):
        super(Slime, self).__init__(name, desc, dmg_type, attack_dmg, hp, weak)
        self.name = name
        self.desc = desc
        self.hp = hp
        self.dmg_type = dmg_type
        self.weak = weak
        self.attack_dmg = attack_dmg


class Hopelessness(Enemy):
    def __init__(self):
        super(Hopelessness, self).__init__("Hopelessness", "words for Jack", "hopelessness", 12, 30, "optimism")

    """def spawn(self):
        """


class Stress(Enemy):
    def __init__(self):
        super(Stress, self).__init__("Stress", "words for Jack", "stress", 12, 30, "tranquility")

    """def spawn(self):
        """


class Deceit(Enemy):
    def __init__(self):
        super(Deceit, self).__init__("Deceit", "words for Jack", "deceit", 12, 30, "ensurement")

    """def spawn(self):
        """


class Hopeless_Slime(Slime):
    def __init__(self):
        super(Hopeless_Slime, self).__init__("Hopeless Slime", "A ball of goo that instills a feeling of hopelessness"
                                                               " within you.", "hopelessness", 5, 10, "optimism")


h_slime1 = Hopeless_Slime()
h_slime2 = Hopeless_Slime()
h_slime3 = Hopeless_Slime()
h_slime4 = Hopeless_Slime()
h_slime5 = Hopeless_Slime()
h_slime6 = Hopeless_Slime()
h_slime7 = Hopeless_Slime()
h_slime8 = Hopeless_Slime()


class Stress_Slime(Slime):
    def __init__(self):
        super(Stress_Slime, self).__init__("Stressful Slime", "A ball of goo that makes your heart race as you are"
                                                              "filled with a sense of pure stress.", "stress", 5, 10,
                                           "tranquility")


s_slime1 = Stress_Slime()
s_slime2 = Stress_Slime()
s_slime3 = Stress_Slime()
s_slime4 = Stress_Slime()
s_slime5 = Stress_Slime()
s_slime6 = Stress_Slime()
s_slime7 = Stress_Slime()
s_slime8 = Stress_Slime()


class Baby_Slime(Slime):
    def __init__(self, parent):
        super(Baby_Slime, self).__init__("Deceitful Slime", "A ball of goo that seems to be made of lies and deceit.",
                                         "deceit", 0, 1, "ensurement")
        self.parent = parent

    def take_dmg(self, dmg_type, dmg: int):

        print("Your sword passes straight through the slime, and you realize it was just an illusion.")
        player.current_location.enemies.remove(self)
        if player.current_location.enemies == [parent]:
            parent.updated = False


class Deceit_Slime(Slime):
    def __init__(self):
        super(Deceit_Slime, self).__init__("Deceitful Slime", "A ball of goo that seems to be made of lies and deceit.",
                                           "deceit", 7, 10, "ensurement")
        self.alive = True
        self.updated = False

    def spawn(self):
        baby1 = Baby_Slime(self)
        baby2 = Baby_Slime(self)
        player.current_location.enemies.insert(0, baby1)
        player.current_location.enemies.insert(1, baby2)
        self.updated = True

    def take_dmg(self, dmg_type, dmg: int):
        if self.weak in dmg_type:
            dmg *= 1.5
            self.hp -= dmg
            if self.hp <= 0:
                print("Using a critical strike of {0}, you attacked {1} and killed them!".format(dmg_type, self.name))
                player.current_location.enemies.remove(self)
                if baby1 in player.current_location.enemies or baby2 in player.current_location.enemies:
                    player.current_location.enemies.remove(baby1)
                    print("As the Deceitful Slime dies, so does its illusions.")
            else:
                print("Using a critical strike of {0}, you attacked {1} and left them with {2} hp.".format(dmg_type,
                                                                                                           self.name,
                                                                                                           self.hp))
                if self.updated is False:
                    self.spawn()
                # player.take_dmg(player, "deceit", self.attack_dmg)
        else:
            self.hp -= dmg
            if self.hp <= 0:
                print("Using {0}, you killed {1}!".format(dmg_type, self.name))
                player.current_location.enemies.remove(self)
                if baby1 in player.current_location.enemies or baby2 in player.current_location.enemies:
                    player.current_location.enemies.remove(baby1)
                    print("As the Deceitful Slime dies, so does its illusions.")
            else:
                print("You attacked {0} with an attack of {1}, leaving them with {2} hp.".format(self.name, dmg_type,
                                                                                                 self.hp))
                if self.updated is False:
                    self.spawn()
                # player.take_dmg(player, "deceit", self.attack_dmg)


d_slime1 = Deceit_Slime()
d_slime2 = Deceit_Slime()
d_slime3 = Deceit_Slime()
d_slime4 = Deceit_Slime()
d_slime5 = Deceit_Slime()
d_slime6 = Deceit_Slime()
d_slime7 = Deceit_Slime()
d_slime8 = Deceit_Slime()
d_slime9 = Deceit_Slime()


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
        super(Sword, self).__init__("Sword of Light", "A sword made of pure determination.", 5)


sword = Sword()


class Bow(Weapon):
    def __init__(self):
        super(Bow, self).__init__("Bow of Light", "A bow made of pure determination.", 5)


class Consumable(Object):
    def __init__(self, name, desc):
        super(Object, self).__init__(name)
        self.name = name
        self.desc = desc


class Room(object):
    def __init__(self, name, desc, north, south, west, east, items=None, enemies=None, NPC=None):
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


spawn_room = Room("The Cave", "A dark cave--------", "Hopeless #1", None, None, None,
                  None, None, None)
hopeless_1 = Room("Hopeless #1", "You come into ------", None, "The Cave", "Hopeless #2", "Hopeless #3", None, h_slime1, None)
hopeless_2 = Room("Hopeless #2", "You come into ------", "Hopeless #4", None, None, "Hopeless #1", None, h_slime2, None)
hopeless_3 = Room("Hopeless #3", "alskdfjla;sdfj", "Hopeless #5", None, "Hopeless #1", None, None, h_slime3, None)
hopeless_4 = Room("Hopeless #4", "asdklfj", "Hopeless #6", "Hopeless #2", None, None, None, h_slime4, None)
hopeless_5 = Room("Hopeless #5", "asdlf", "Hopeless #7", "Hopeless #3", None, None, None, h_slime5, None)
hopeless_6 = Room("Hopeless #6", "asdfj", None, "Hopeless #4", None, "Hopeless #8", None, h_slime6, None)
hopeless_7 = Room("Hopeless #7", "asdfj", None, "Hopeless #5", "Hopeless #8", None, None, h_slime7, None)
hopeless_8 = Room("Hopeless #8", "asdf", "Hopeless #9", None, "Hopeless #6", "Hopeless #7", None, h_slime8, rogers)  # NPC here
hopeless_9 = Room("Hopeless #9", "asdfj", "Stress #1", "Hopeless #8", None, None, None, None, None)

stress_1 = Room("Stress #1", "You come into ------", None, "Hopeless #9", "Stress #2", "Stress #3", None, s_slime1, None)
stress_2 = Room("Stress #2", "You come into ------", "Stress #4", None, None, "Stress #1", None, s_slime2, None)
stress_3 = Room("Stress #3", "alskdfjla;sdfj", "Stress #5", None, "Stress #1", None, None, s_slime3, None)
stress_4 = Room("Stress #4", "asdklfj", "Stress #6", "Stress #2", None, None, None, s_slime4, None)
stress_5 = Room("Stress #5", "asdlf", "Stress #7", "Stress #3", None, None, None, s_slime5, None)
stress_6 = Room("Stress #6", "asdfj", None, "Stress #4", None, "Stress #8", None, s_slime6, None)
stress_7 = Room("Stress #7", "asdfj", None, "Stress #5", "Stress #8", None, None, s_slime7, None)
stress_8 = Room("Stress #8", "asdf", "Stress #9", None, "Stress #6", "Stress #7", None, s_slime8, ross)  # NPC here
stess_9 = Room("Stress #9", "asdfj", "Deceit #1", "Stress #8", None, None, None, None, None)

deceit_1 = Room("Deceit #1", "You come into ------", None, "Stress #9", "Deceit #2", "Deceit #3", None, d_slime1, None)
deceit_2 = Room("Deceit #2", "You come into ------", "Deceit #4", None, None, "Deceit #1", None, d_slime2, None)
deceit_3 = Room("Deceit #3", "alskdfjla;sdfj", "Deceit #5", None, "Deceit #1", None, None, d_slime3, None)
deceit_4 = Room("Deceit #4", "asdklfj", "Deceit #6", "Deceit #2", None, None, None, d_slime4, None)
deceit_5 = Room("Deceit #5", "asdlf", "Deceit #7", "Deceit #3", None, None, None, d_slime5, None)
deceit_6 = Room("Deceit #6", "asdfj", None, "Deceit #4", None, "Deceit #8", None, d_slime6, None)
deceit_7 = Room("Deceit #7", "asdfj", None, "Deceit #5", "Deceit #8", None, None, d_slime7, None)
deceit_8 = Room("Deceit #8", "asdf", "Deceit #9", None, "Deceit #6", "Deceit #7", None, d_slime8, sagan)  # NPC here
deceit_9 = Room("Deceit #9", "asdfj", "Covid", "Deceit #8", None, None, None, None, None)
covid = Room("Covid", "asdklf", None, "Deceit #9", None, None, None, None, None)

# Defining the Player
player = Player(spawn_room, None)
playing = True
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while playing:
    print("Opening Text that tells you that you have a sword in hand...plz I dont want to code in a 'take' function")
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
    elif "attack" in command.lower() or "hit" in command.lower():
        info = command.lower().split()
        target = " ".join(info[1:])
        for i in range(player.current_location.enemies):
            d["group" + str(i)] = self.getGroup(selected, header + i)
        for i in player.current_location.enemies:
            if i.name.lower() == target:
                target = i
                break





