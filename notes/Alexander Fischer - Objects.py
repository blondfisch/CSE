class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, distance):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.range = distance


class Sword(Weapon):
    def __init__(self, name, damage, durability, desc):
        super(Sword, self).__init__(name, damage, 0)
        self.name = name
        self.damage = damage
        self.distance = 0
        self.durability = durability
        self.desc = desc

    def swing(self):
        if self.durability <= 0:
            print("Your sword is broken.")
        else:
            self.durability -= 1


class Rapier(Sword):
    def __init__(self):
        super(Rapier, self).__init__("Rapier", 7, 50, "A sharp rapier sword. It is in excellent condition and will"
                                                      " do massive damage to enemies.")


class DullSword(Sword):
    def __init__(self):
        super(DullSword, self).__init__("Dull Sword", 2, 25, "A dull sword. It has not been well maintained and is on"
                                                             " the verge of breaking.")


class BroadSword(Sword):
    def __init__(self):
        super(BroadSword, self).__init__("Broadsword", 10, 40, "This sword is quite heavy and will wear out quickly"
                                                               "but does massive damage.")


class CrysKnife(Sword):
    def __init__(self):
        super(CrysKnife, self).__init__("Crysknife", 6, 100, "This knife is made from the teeth of a worm. While not"
                                                             " very sharp, it will undergo a lot of use before it"
                                                             " breaks.")


class Gun(Weapon):
    def __init__(self, name, damage, charge):
        super(Gun, self).__init__(name, damage, 1)
        self.name = name
        self.damage = damage
        self.distance = 1
        self.charge = charge

    def shoot(self):
        if self.charge <= 0:
            print("The gun does not have any charge left.")
        else:
            self.charge -= 1


class Lasgun(Gun):
    def __init__(self):
        super(Lasgun, self).__init__("Lasgun", 20, 30)


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name)
        self.name = name
        self.desc = description


class Food(Consumable):
    def __init__(self, name, description, health):
        super(Consumable, self).__init__(name)
        self.name = name
        self.desc = description
        self.health = health


class Bread(Food):
    def __init__(self):
        super(Bread, self).__init__("Bread", "This is a piece of bread. It can be eaten for health.", 25)


class Water(Food):
    def __init__(self):
        super(Water, self).__init__("Water", "Arguably the most valuable item on the planet, water heals you massive"
                                             " amounts but is very rare.", 50)


class Rice(Food):
    def __init__(self):
        super(Rice, self).__init__("Rice", "This item can be eaten for health. It is rather common on the planet.", 15)


class Chicken(Food):
    def __init__(self):
        super(Chicken, self).__init__("Fried Chicken", "The most holy of items, fried chicken. This item heals for all"
                                                       " of your health.", 100)


class Herb(Food):
    def __init__(self):
        super(Herb, self).__init__("Herbs", "Common Herbs. They are plentiful but heal for only a small amount", 10)


class Potion(Consumable):
    def __init__(self, name, description, damage):
        super(Potion, self).__init__(name, description)
        self.damage = damage


class Life(Potion):
    def __init__(self):
        super(Life, self).__init__("Water of Life", "An incredibly dangerous item. Consuming the Water of Life could "
                                                    "kill you or grant you superhuman strength.", 30)


class Armor(Item):
    def __init__(self, name, desc, defense, shield):
        super(Armor, self).__init__(name)
        self.name = name
        self.desc = desc
        self.defense = defense
        self.shield = shield


class FullShield(Armor):
    def __init__(self):
        super(FullShield, self).__init__("Full body shield", "This shield is incredibly powerful because it covers the"
                                                             "entire body.", 4, True)


class HalfShield(Armor):
    def __init__(self):
        super(HalfShield, self).__init__("Half Shield", "This shield has been worn down from use and only covers"
                                                        "half of the body.", 2, True)


class Enemy(object):
    def __init__(self, health, item=None, desc=None, shield=False):
        self.health = health
        self.desc = desc
        self.items = []
        self.shield = shield
        self.items = item


class BaseSoldier(Enemy):
    def __init__(self):
        super(BaseSoldier, self).__init__("Imperial", 50, "A basic Imperial soldier. He is not well equipped and does"
                                                          " not have a shield.")


class Captain(Enemy):
    def __init__(self):
        super(Captain, self).__init__("Imperial Captain", 75, Rapier, "An Imperial Captain. He has a more advanced "
                                                                      "training and is wearing a shield.", True)


class Baron(Enemy):
    def __init___(self):
        super(Baron, self).__init___("The Baron", 200, BroadSword, "The Baron. He is extremely well trained and"
                                                                   " is very fast. His attacks will kill you quickly"
                                                                   " if you are unprepared, in the same way that he"
                                                                   " killed your parents.", False)
