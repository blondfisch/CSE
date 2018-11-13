import random
wordList = ["tiger", "edison", "wiebe"]
word = random.choice(wordList)
word_listform = list(word)
#   print(word)
guesseslft = 6
#   print(word_listform)
disp_list = ["_" * len(word)]
print(disp_list)
letterslft = len(word)  # This is the length of the list
while guesseslft > 0 and letterslft > 0:
    print(disp_list)
    #   print(word_listform)
    print("Guesses left: %d" % guesseslft)
    print("Letters left: %d" % letterslft)
    guessltr = input("Guess a letter")
    if guessltr in word_listform:
        print("Correct")
        letterslft -= 1
        disp_list.append(guessltr)
    else:
        print("Incorrect")
        guesseslft -= 1
if guesseslft == 0:
    print("You ran out of turns. Heisenwiebe won.")
    print("The actual word was %s" % word)
if letterslft == 0:
    print("Congratulations! You guessed the word!")
