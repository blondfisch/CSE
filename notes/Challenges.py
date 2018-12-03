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


def challenge7(n):
    return n + 11*n + 111*n


print(challenge7(1))


def challenge8(number):
    if number in range(1850, 2150):
        print("The number is within 150 of 2000")
    elif number in range(2850, 3150):
        print("That number is within 150 of 3000")
    else:
        print("That number is not even close to 2000 or 3000")


print(challenge8(3001))


def challenge9(letter):
    vowel_list = ["a", "e", "i", "o", "u"]
    if letter in vowel_list:
        print("That is a vowel")
    else:
        print("The letter is not a vowel")


print(challenge9("a"))


def challenge10():
