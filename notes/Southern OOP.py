import random
import god
import math
'''class Dog:

    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
Jak = Dog("Jak", 14)
Tom = Dog("Tom", 4)
Young_Joe = Dog("Young Joe", 2)
# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{} is a {}!".format(philo.name, philo.species))
print(philo.speak("Toxic"))
'''


class PPL(object):
    species = "Person"

    def __init__(self, name, toxic, age):
        self.name = name
        self.toxic = toxic
        self.age = age

    def word(self, sound):
        return "{0} says {1}. He is also {2}".format(self.name, sound, self.toxic)


Jak = PPL("Jak", "super toxic", 15)

print(Jak.word("I'm trash"))

# The Dictionary
dict1 = {'age': {"Jack": 14, "Jak": god.call_god(), "Jac": 18, "Jacket": 645}}

# dict1['age']["Jak"]
print(dict1)
print("{0} had a birthday! {0} is now {1} years old. No one likes math, especially {0}"
      .format(dict1["name"], dict1["age"]))
