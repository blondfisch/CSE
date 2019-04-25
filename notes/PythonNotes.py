"""
print("Hello World, I am alive")

# This is a comment. This has no effect on the code
# but this does allow me to do things. I can:
# 1. Make notes to myself
# 2. Comment pieces of code that do not work
# 3. Make my code easier to read

#print("Look at what happens here. Is there any space?")
#print()
#print()
#print("There should be a couple blank lines here.")

#Math
print(3+5)
print(5-2)
print(3*4)
print(6/2)

print("Figure this out...")
print(6//2)
print(5//2)
print(9//4)

print("Here is another one...")
print(6%2)
print(5%2)
print(11%4) #Modulus (Remainder)

#Powers
#What is 2^20
print(3**27)

# Taking input
name = input("What is your name?")
print("Hello %s." % name)

age = input("How old are you >_")
print("%s?!? You belong in a museum." % age)
print()
print("%s is really old. They are %s years old." % (name, age))

# variable Assignments
car_name = "Van Mobile"
car_type = "Tesla"
car_cylinders = 16
car_miles_per_gallon = 0.01

# Make it print "I have a car called Wiebe mobile. It is a Tesla."
print("I have a car called %s. It is a %s." % (car_name, car_type))

# Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print("This is your real age: %d" % hidden_age)


This is a multi line comment
anything between the "s is not run
"""


# Functions
def sayIt():
    print("Hello World!")



sayIt()
sayIt()
sayIt()


# f(x) = 2x+3
def f(x):
    print(2*x + 3)


f(1)
f(2)
f(5000)


# Distance Formula
def dist(x1, y1, x2, y2):
    dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    print(dist)

dist(0, 0, 3, 4)
dist(0, 0, 8, 15)

# Loops
"""for i in range(510):   # range 5 is list of numbers 0-4
    sayIt()
"""
# For Loops
for i in range(10):
    print(i + 1)


for i in range(5):
    f(i)

# While loops
a = 1
while a < 10:
    print(a)
    a += 2  # This is the same as saying a = a + 1


"""
For loops - Use when you know EXACTLY  how many iterations
While loops - Use when you DON'T know how many iterations
"""

#  Control Structures (If statements)
sunny = False
if sunny:
    print("Go outside")


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)

#   "Random" Notes
import random   # This should be on line 1
print(random.randint(0, 100))

#   Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3   # A is set to 3
a == 3 # Is a equal to 3
"""

# Creating a list
colors = ["blue", "turquoise", "cyan", "pink", "orange", "black", "red", "wiebe", "grape doctor", "thanosBoi", "food"]
print(colors[0])

# Length of list
print("There are %d things in the list." % len(colors))

# Changing elements in a list
colors[1] = "Chocolate Covered Maple Smoked Bacon Soda"
print(colors[1])

# Looping through lists
for item in colors:
    print(item)

'''
Make a list with 7 items
change the 3rd thing in the list
print the item print the full list

myList = ["Jack", "Chocolate", "Smoked", "Maple", "Smoked", "Bacon", "Soda"]
list[2] = "Covered"
print(list[2])
for thing in list:
    print(thing)
print("The last thing in the list is %s" % list[len(list) - 1])

# Slicing a List
print(list[1:3])
print(list[1:5])
print(list[1:])
print(list[:4])
'''

food_list = ["Chocolate covered maple smoked bacon soda", "sushi", "rocks", "cow tongues", "chicken feet", "popcorn",
              "chocolate", "maple syrup", "corn dogs", "livers - we don't discriminate", "salmon", "ice cream",
              "turkey", "beef", "chicken", "salads", "fried oreo bacon", "fried bacon oreo", "pumpkin spice bacon",
              "pasta", "pasta soda", "pirate soda", "peppermint oreos", "double stuffed oreos", "bacon oreos",
             "pancakes", "eggs", "pie"]
print(len(food_list))

# Adding stuff to a list
food_list.append("apple pie")
food_list.append("waffles")
# Notice that everything is object.method(parameters)
print(food_list)
food_list.insert(1, "eggo waffles")
print(food_list)


# Removing stuff from a list
food_list.remove("salads")
print(food_list)

'''
make a new list with 3 items
add a 4th item to the list
remove one of the first 3'''
soda_list = ["cherry", "diet", "vanilla"]

soda_list.append("Chocolate Covered Maple Smoked Bacon")
soda_list.remove("diet")
print(soda_list)


# Tuples
brands = ("apples", "Samsung", "HTC")   # Notice the parentheses

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)

# Find the index of an item
print(food_list.index("chicken"))

# changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

for i in range(len(list1)): # i goes through all indices
    if list1[i] == "u":  # if we find a U
        list1.pop(i)    # remove the i-th index
        list1.insert(i, "*")    # put a * there instead

'''for character in list1:
    if character == "u":
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")
'''
# Turn a list into a string
print("".join(list1))
# a**2 + b**2 = c**2


def pythagorean(a, b):
    return (a**2 + b**2)**(1/2)


print(pythagorean(3, 4))

