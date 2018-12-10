import random
import math
import string
import datetime
import god


def challenge1():
    numbers = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)
            print(numbers)


print(challenge1())


print(math.factorial(8))


def challenge2(a, b, c, d, e, f, g):
    list_boi = [a, b, c, d, e, f, g]
    tuple_boi = (a, b, c, d, e, f, g)
    print(tuple_boi)
    return list_boi


print(challenge2(3, 4, 5, 6, 8, 10, 60))


theThing = input("T series will rule them all.")

# god.call(1)
