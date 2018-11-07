import random
cwallet = 15
round_count = 0
mwallet = 0
print("Welcome to Lucky 7's, the gambling game in which Heisenwiebe rips all of you money from your hands!")
print("Time to make a bet! You have made a $1 bet and if your role equals 7, you win it back, plus $4 extra dollars!")
while cwallet > 0:
   if cwallet > mwallet:
        mwallet = cwallet
    if bet.lower() == "bet":
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll = dice_1 + dice_2
        if roll == 7:
            print("Congratulations! You won this round")
            cwallet += 4
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1,6)
            round_count += 1
            print(cwallet)
            print("You currently have $%d" % cwallet)
        else:
            print("The dice rolled a %d" % roll)
            print("So sad. Heisenwiebe took your money this round.")
            cwallet -= 1
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            round_count += 1
            print("You currently have $%d" % cwallet)
