import random
import string


def challenge1(first_name, last_name):
    return "%s %s" % (last_name, first_name)


print(challenge1("Alex", "Fischer"))


def challenge2(a):
    if a % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


print(challenge2(4))


def challenge3(base, height):
    return base*height*1/2


print(challenge3(5, 6))


def challenge4(a):
    if a >= 1:
        print("The number is positive")
    elif a == 0:
        print("The number is 0")
    else:
        print("The number is negative.")


print(challenge4(-5))


def challenge5(radius):
    return 2*radius*3.1415


print("The circle has an area of %s units." % challenge5(4))


def challenge6(radi):
    return 4/3 * radi * 3.1415


print(challenge6(5))

