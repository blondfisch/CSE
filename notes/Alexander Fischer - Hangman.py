import random
wordList = ["tiger", "edison", "wiebe"]
word = random.choice(wordList)
word_listform = list(word)
#   print(word)
guesseslft = 6
prior_guesses = []
#   print(word_listform)
disp_list = "_ " * len(word)
wordidx = 0
print(disp_list)
letterslft = len(word)  # This is the length of the list
while guesseslft > 0 and letterslft > 0:
    print(disp_list)
    #   print(word_listform)
    print("Guesses left: %d" % guesseslft)
    print("Letters left: %d" % letterslft)
    guessltr = input("Guess a letter")
    if guessltr in word_listform:
        if guessltr not in prior_guesses:
            print("Correct")
            letterslft -= 1
            prior_guesses.append(guessltr)
            wordidx = word.index(guessltr)
            print(wordidx)
            for guessltr in range(0, len(word)):
                disp_list.insert(wordidx, guessltr)
        else:
            print("You already guessed that. Guess again.")
            guessltr = input("Guess a letter")
    else:
        print("Incorrect")
        guesseslft -= 1
if guesseslft == 0:
    print("You ran out of turns. Heisenwiebe won.")
    print("The actual word was %s" % word)
if letterslft == 0:
    print("Congratulations! You guessed the word!")
