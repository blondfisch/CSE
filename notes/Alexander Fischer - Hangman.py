import random
import string
wordList = ["tiger", "Edison", "Wiebe!", "Thanos!", "pumpkin", "desktop", "database", "crossroads", "secret",
            "teacher", "redwood", "deliver", "computer", "political", "sadness", "fight!", "Heisenweibe", "Victory!"]
word = random.choice(wordList)
word_listform = list(word)
guesseslft = 8
prior_guesses = []
legal_letters = list(string.ascii_letters)
anti_letters = list(word.swapcase())
totalword = anti_letters + word_listform
disp_list = []
for i in range(len(word_listform)):
    if word_listform[i] in legal_letters:
        disp_list += "_"
    else:
        disp_list += word_listform[i]
solve = False
num = 0
while guesseslft > 0 and "_" in disp_list and solve is False:
    print(' '.join(disp_list))
    print("Guesses left: %d" % guesseslft)
    guessltr = input("Guess a letter")
    if len(guessltr) > 1:
        guesswrd = list(guessltr)
        if len(guesswrd) == len(word_listform):
            for i in range(len(word_listform)):
                if guesswrd[i] == word_listform[i] or guesswrd[i] == anti_letters[i]:
                    num += 1
            if num == len(word_listform):
                solve = True
            else:
                print("Incorrect")
                guesseslft -= 1
        else:
            guesseslft -= 1
            print("Incorrect")
    elif "_" in disp_list and len(guessltr) == 1:
        if guessltr not in prior_guesses and guessltr in legal_letters and guessltr in totalword:
            for letter in range(len(word_listform)):
                if guessltr == word_listform[letter] or guessltr == anti_letters[letter]:
                    disp_list[letter] = word_listform[letter]
                    prior_guesses.append(guessltr)
                    prior_guesses.append(guessltr.swapcase())
        elif guessltr not in anti_letters and guessltr in legal_letters and guessltr not in word_listform:
            print("Incorrect")
            prior_guesses.append(guessltr)
            guesseslft -= 1
        elif guessltr in prior_guesses:
            print("You already guessed that.")
        elif guessltr not in legal_letters:
            guesseslft -= 1
            print("That is not a valid letter")
if guesseslft == 0:
    print("You ran out of turns. Heisenwiebe won.")
    print("The actual word was %s" % word)
if "_" not in disp_list:
    print("Congratulations! You guessed the word!")
    print("The word was %s" % word)
