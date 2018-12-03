import random
import string
# defining variables
wordList = ["tiger", "edison", "wiebe", "thanos", "pumpkin", "desktop", "database", "crossroads", "secret",
            "teacher", "redwood", "deliver", "computer", "political", "sadness"]
word = random.choice(wordList)
word_listform = list(word)
guesseslft = 6
prior_guesses = []
disp_list = ["_"] * len(word)
while guesseslft > 0 and "_" in disp_list:
    print(' '.join(disp_list))
    print("Guesses left: %d" % guesseslft)
    guessltr = input("Guess a letter")
    if guessltr not in prior_guesses:
        for letter in range(len(word_listform)):
            if guessltr == word_listform[letter]:
                disp_list[letter] = guessltr  # replace all letters in the chosen word that match the players guess
                prior_guesses.append(guessltr)
    else:
        print("You already guessed that.")
    if guessltr not in word_listform:
        guesseslft -= 1
        print("Incorrect")
        prior_guesses.append(guessltr)
if guesseslft == 0:
    print("You ran out of turns. Heisenwiebe won.")
    print("The actual word was %s" % word)
if letterslft == 0:
    print("Congratulations! You guessed the word!")
    print("The word was %s" % word)
