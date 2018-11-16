import random
wordList = ["tiger", "edison", "wiebe"]
word = random.choice(wordList)
word_listform = list(word)
#   print(word)
guesseslft = 6
prior_guesses = []
#   print(word_listform)
disp_list = ["_"] * len(word)
wordidx = 0
letterslft = len(word)  # This is the length of the list
wordmax = 0
while guesseslft > 0 and letterslft > 0:
    print(' '.join(disp_list))
    #   print(prior_guesses)
    print("Guesses left: %d" % guesseslft)
    print("Letters left: %d" % letterslft)
    guessltr = input("Guess a letter")
    if guessltr in word_listform:
        wordidx = word
        wordmax = word.max(guessltr)
        if guessltr not in prior_guesses:

            for guessltr in word_listform   #[i for i, j in enumerate(a) if j == m:
                if wordidx == word.index(guessltr):
                    disp_list.pop(wordmax)
                    disp_list.inset(wordmax, guessltr)
                    prior_guesses.append(guessltr)
                    disp_list.pop(wordidx)
                    disp_list.insert(wordidx, guessltr)
                    letterslft -= 1

        else:

            print("You already guessed that. Guess again.")
    else:
        print("Incorrect")
        guesseslft -= 1
if guesseslft == 0:
    print("You ran out of turns. Heisenwiebe won.")
    print("The actual word was %s" % word)
if letterslft == 0:
    print("Congratulations! You guessed the word!")
    print("The word was %s" % word)
