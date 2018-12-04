import random
import string
import datetime
import math


def challenge1(first_name, last_name):
    return "%s %s" % (last_name, first_name)


print(challenge1("Alex", "Fischer"))


def challenge2(a):
    if a % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."


print(challenge2(4))


def challenge3(base, height):
    return base*height*1/2


print(challenge3(5, 6))


def challenge4(a):
    if a >= 1:
        return "The number is positive"
    elif a == 0:
        return "The number is 0"
    else:
        return "The number is negative."


print(challenge4(-5))


def challenge5(radius):
    return math.pi * radius ** 3


print("The circle has an area of %s units." % challenge5(4))


def challenge6(radi):
    return 4/3 * radi * math.pi


print(challenge6(5))


def challenge7(n):
    return n + 11*n + 111*n


print(challenge7(1))


def challenge8(number):
    if number in range(1850, 2150):
        return "The number is within 150 of 2000"
    elif number in range(2850, 3150):
        return "That number is within 150 of 3000"
    else:
        return "That number is not even close to 2000 or 3000"


print(challenge8(3001))


def challenge9(letter):
    vowel_list = ["a", "e", "i", "o", "u"]
    if letter in vowel_list:
        return "That is a vowel"
    else:
        return "The letter is not a vowel"


print(challenge9("a"))


def challenge10(integer):
    try:
        int(integer)
        return True
    except ValueError:
        return False


print(challenge10(31))


def challenge11():
    return datetime.datetime.now()


print(str(challenge11()))


def challenge12(a, b):
    return math.gcd(a, b)


print(challenge12(4, 8))
