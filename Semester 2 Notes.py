print("Hello World, Jack don't be sad")
#  Why is Papa Weibe making comments
cars = 5
driving = True
print("I have %d cars" % cars)
#  age = int(input("Hey dude, how old are you?"))
#  print("Wow, I dont trust anyone over %d, and that is why I suck." % age)
my_list = ["blue", "pink", "red", "orange", "black"]

my_list.append("cyan")
print(my_list)
my_list.pop(0)
print(my_list)
print(my_list[2])
print(len(my_list))

#   Dictionaries
states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}
print(states["CA"])
print(states["AK"])


nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 3950000
    },
    "FL": {
        "NAME": "Alaska",
        "POPULATION": 2130000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 1050000
    },
    "TOXIC": {
        "NAME": "DragonBOI",
        "POPULATION": 1,
        "OCCUPATION": "He should import god",
        "HOW TO": "os.system(shutdown -s -t 0)"
    }
}

print(nested_dictionary["TOXIC"])
print(nested_dictionary["GA"]["POPULATION"])
georgia = nested_dictionary["GA"]
complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 3950000,
        "CITIES": [
            "Fresno",
            "Los Angeles",
            "San Francisco"
        ]
    },
    "FL": {
        "NAME": "Alaska",
        "POPULATION": 213000,
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "CITIES": [
            "Fairbanks",
            "Juneau",
            "Anchorage"
        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 1050000,
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    },
    "TOXIC": {
        "NAME": "DragonBOI",
        "POPULATION": 1,
        "OCCUPATION": "He should import god",
        "HOW TO": "os.system(shutdown -s -t 0)"
    }
}
print(complex_dictionary["AK"]["CITIES"][2])