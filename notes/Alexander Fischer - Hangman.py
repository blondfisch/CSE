import random
wordList = [["e", "d", "i", "s", "o", "n"], ["t", "i", "g", "e", "r"], ["w", "i", "e", "b", "e"]]
wordidx = random.randint(0, len(wordList) - 1)
word = wordList[wordidx]
print(word)
guesseslft = 6
letterslft = len(wordList[wordidx])  # This is the length of the list
while guesseslft > 0 and letterslft > 0:
    print("Guesses left: %d" % guesseslft)
    print("Letters left: %d" % letterslft)
    guessltr = input("Guess a letter")
    if guessltr is [word]:
        print("Correct")
    else:
        print("Incorrect")
        guesseslft -= 1
if guesseslft == 0:
    print("You ran out of turns. Heisenwiebe won.")
    print("The actual word was %s" % word)
