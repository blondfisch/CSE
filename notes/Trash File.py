import random
import math
import string
import datetime


def challenge1():
    numbers = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)
            print(numbers)

print(challenge1())
