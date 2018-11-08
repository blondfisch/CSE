import random
wordList = [['e', 'd', 'i', 's', 'o', 'n'], ['t', 'i', 'g', 'e', 'r'], ['w', 'i', 'e', 'b', 'e']]
wordidx = random.randint(0, 2)
word = wordList[wordidx]
print(word)
guesseslft = 6
while guesseslft > 0:
    print("Guesses left: %d" % guesseslft)
    guessltr = input("Guess a letter")
    if guessltr in [word]:
        print("Correct")
    else:
        print("Incorrect")
        guesseslft -= 1
