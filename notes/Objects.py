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
        super(WoodSword, self).__init__("Wooden Sword", 5, 60, "A wooden sword. It's not the best option",
                                        ["wood sword", "sword", "wooden sword"])


class Rapier(Sword):
    def __init__(self):
        super(Rapier, self).__init__("Rapier", 7, 50, "A sharp rapier sword. It is in excellent condition and will"
                                                      " do massive damage to enemies.",
                                     ["rapier", "sword"])


class DullSword(Sword):
    def __init__(self):
        super(DullSword, self).__init__("Dull Sword", 2, 25, "A dull sword. It has not been well maintained and is on"
                                                             " the verge of breaking.",
                                        ["sword", "dull sword", "dullsword"])


class BroadSword(Sword):
    def __init__(self):
        super(BroadSword, self).__init__("Broadsword", 10, 40, "This sword is quite heavy and will wear out quickly"
                                                               "but does massive damage.",
                                         ["broadsword", "sword", "broad sword", "sword"])


class CrysKnife(Sword):
    def __init__(self):
        super(CrysKnife, self).__init__("Crysknife", 6, 100, "This knife is made from the teeth of a worm. While not"
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
        super(BaseSoldier, self).__init__("Imperial", 50, 0, "A basic Imperial soldier. He is not well equipped and"
                                                             " does not have a shield.")


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
        super(Dummy, self).__init__("Dummy", 1000000000000, 0, "A training dummy. You could hit it, if you wanted to.")


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
sard1 = Sardaukar1()
worm = Worm()
tooth = Tooth()
sard2 = Sardaukar2()
fremen = Fremen()
soldier = BaseSoldier()
# sard2.attack(dummy)
