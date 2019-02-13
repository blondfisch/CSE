import math
from notes.Special_Random import RandomWiebe


class Phone(object):
    def __init__(self, carrier, charge_left=50):
        # These are attributes that a phone has.
        # These should all be relevant to our program
        self.screen = True
        self.camera = 2
        self.microphone = True
        self.carrier = carrier
        self.battery_left = charge_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

    def make_call(self, duration):
        if not self.screen:
            print("You cant make a phone call.")
            print("Your screen is broken")
            return
        battery_loss_per_minute = 5
        if self.battery_left <= 0:
            print("You cant, the phone is dead")
            return
        self.battery_left -= duration * battery_loss_per_minute
        if self.battery_left < 0:
            self.battery_left = 0
            print("Your phone died during the conversation.")
        elif self.battery_left == 0:
            print("Your phone dies at the end of the conversation.")
        else:
            print("You successfully make the phone call.")
            print("Your phone is now at %s." % self.battery_left)

    def smash_phone(self):
        if not self.screen:
            print("SMASH!!!!!!!!")
            print("It broke.")
            self.screen = False
        else:
            print("Your screen can't be broken. What a god.")


my_phone = Phone("ATT", 100)
your_phone = Phone("Bell", 0)
jacks_phone = Phone("Popeyes")
default_phone = Phone("Verizon")

my_phone.make_call(60)
my_phone.make_call(10)
my_phone.charge(100)
my_phone.make_call(10)
jacks_phone.smash_phone()
jacks_phone.make_call(1)

print(RandomWiebe.my_random())
