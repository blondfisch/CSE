import random
cwallet = 15
round_count = 0
mwallet = 15
best_round = 0
print("Welcome to Lucky 7's, the gambling game in which Heisenwiebe rips all of you money from your hands!")
print("Time to make a bet! You have made a $1 bet and if your role equals 7, you win it back, plus $4 extra dollars!")
while cwallet > 0:
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            roll = dice_1 + dice_2
            if roll == 7:
                print("Congratulations! You won this round")
                print("The dice rolled a %d" % roll)
                cwallet += 4
                dice_1 = random.randint(1, 6)
                dice_2 = random.randint(1, 6)
                round_count += 1
                print("You currently have $%d" % cwallet)
                if mwallet < cwallet:
                    mwallet = cwallet
                    best_round = round_count
            else:
                print("The dice rolled a/an %d" % roll)
                print("So sad. Heisenwiebe took your money this round.")
                cwallet = cwallet - 1
                print("You currently have $%d" % cwallet)
                dice_1 = random.randint(1, 6)
                dice_2 = random.randint(1, 6)
                round_count += 1

print("You had a maximum amount of $%d" % mwallet)
print("You lasted %d rounds" % round_count)
print("You should have stopped after round %d" % best_round)
