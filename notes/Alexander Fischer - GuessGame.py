import random
difficulty = input("Type in difficulty; Easy or Hard")
print("%s" % difficulty)

if difficulty.lower() == "easy":
    print("I have a random number between 0 and 10. You have 5 guesses to figure it out.")
    number = random.randint(0, 10)
else:
    number = random.randint(0, 100)
    print("I have a random number between 0 and 100. You have 5 guesses to figure it out.")
