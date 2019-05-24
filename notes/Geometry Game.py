import math
import random


def choose(total, number):
    combin = math.factorial(total) / (math.factorial(number) * math.factorial(total - number))
    return combin


def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])


num1 = 0
num2 = 0
profits = 0
total = 0
wins = 0
matters = []
valid_ints = [1., 1., 1., 1., 2., 2., 2., 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
              9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

for i in range(0, 1000000):
    matters = []
    num1 = random.choice(valid_ints)
    valid_ints.remove(num1)
    dealer1 = random.choice(valid_ints)
    valid_ints.remove(dealer1)
    num2 = random.choice(valid_ints)
    valid_ints.remove(num2)
    dealer2 = random.choice(valid_ints)
    valid_ints.remove(dealer2)
    nat = num1 + num2
    if num1 == 10 or num1 == 11:
        matters.append(num1)
    if num2 == 10 or num2 == 11:
        matters.append(num2)
    if nat == 21:
        profits += 5
        print("You won")
        wins += 1
    else:
        for i in range(random.randint(0, 4)):
            hey = i + 1
            new = random.choice(valid_ints)
            if new == 10 or new == 11:
                matters.append(new)
    if 10 in matters and 11 in matters:
        profits += 5
        print("You won")
        wins += 1
    else:
        profits -= 5
        print("You lost")
    valid_ints = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
                  9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
    total += 1
print(profits)
print(wins)
average = float(profits / total)
print("You basically lost %d every round" % average)
