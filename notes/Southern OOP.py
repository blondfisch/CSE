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

class PPL:
    species = "Person"

    def __init__(self, name, toxic, age):
        self.name = name
        self.toxic = toxic
        self.age = age

    def word(self, sound):
        return "{0} says {1}. He is also {2}".format(self.name, sound, self.toxic)


Jak = PPL("Jak", "super toxic", 15)

print(Jak.word("I'm trash"))

