class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, damage, range):
        super(Weapon, self).__init__(damage)
        self.damage = damage
        self.range = range


class Sword(Weapon):
    def __init__(self, name, damage, shield=True):
        super(Sword, self).__init__(name, damage, shield)
        self.name = name
        self.shield = shield
        self.damage = damage


class Lasgun(Weapon):
    def __init__(self, name, damage, shield=False):
        super(Lasgun, self).(name, damage, shield)
        self.name = name
        self.shield = shield
        self.damage = damage
