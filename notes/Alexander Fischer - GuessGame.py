import random
difficulty = input("Type in difficulty; Easy or Hard")
print("%s" % difficulty)

if difficulty.lower() == "easy":
    print("I have a random number between 0 and 10. You have 10 guesses to figure it out.")
    number = random.randint(0, 10)
else:
    number = random.randint(0, 100)
    print("I have a random number between 0 and 100. You have 10 guesses to figure it out.")

guess = int(input("Type in a number"))
amount_guess = 0

while amount_guess < 10:
    if number > guess:
        print("Guess higher")
        guess = int(input("Guess again"))
        amount_guess = amount_guess + 1
    elif number == guess:
        amount_guess = 11
    else:
        print("Guess lower.")
        guess = int(input("Guess again"))
        amount_guess = amount_guess + 1

if amount_guess == 10:
    print("You ran out of guesses. Heisenwiebe won.")

if amount_guess == 11:
    print("Congratulations! You won!")

