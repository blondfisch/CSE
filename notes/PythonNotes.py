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
import random   #This should be on line 1
print(random.randint(0, 100))
