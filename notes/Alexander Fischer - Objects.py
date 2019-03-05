class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, distance):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.range = distance


class Sword(Weapon):
    def __init__(self, name, damage, shield):
        super(Sword, self).__init__("Sword", 10, 0)
        self.name = name
        self.shield = shield
        self.damage = damage
        self.distance = 0


class Gun(Weapon):
    def __init__(self, name, damage, shield):
        super(Gun, self).__init__("Lasgun", 15, 1)
        self.name = name
        self.damage = damage
        self.shield = shield
        self.distance = 1


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name)
        self.name = name
        self.desc = description


class Food(Consumable):
    def __init__(self, name, health, description):
        super(Food, self).__init__(name, description)
        self.name = name
        self.heal = health
        self.description = description


class Armor(Item):
    def __init__(self, name, type, defense):
        super(Armor, self).__init__(name)
        self.name = name