import random
cwallet = 15
round_count = 0
mwallet = 0
print("Welcome to Lucky 7's, the gambling game in which Heisenwiebe rips all of you money from your hands!")
print("Time to make a bet! You have made a $1 bet and if your role equals 7, you win it back, plus $4 extra dollars!")
while cwallet > 0:
    if mwallet <= cwallet: # THis is the problem, you just need to figure out where this code goes
        mwallet = cwallet
        bet = input("Type in bet to play")
        if bet.lower() == "bet":
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            roll = dice_1 + dice_2
            if roll == 7:
                print("Congratulations! You won this round")
                print("The dice rolled a/an %d" % roll)
                cwallet += 4
                dice_1 = random.randint(1, 6)
                dice_2 = random.randint(1, 6)
                round_count += 1
                print("You currently have $%d" % cwallet)
            else:
                print("The dice rolled a/an %d" % roll)
                print("So sad. Heisenwiebe took your money this round.")
                cwallet = cwallet - 1
                print("You currently have $%d" % cwallet)
                dice_1 = random.randint(1, 6)
                dice_2 = random.randint(1, 6)
                round_count += 1
