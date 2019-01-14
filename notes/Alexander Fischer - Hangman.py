import random
import string
wordList = ["tiger", "Edison", "Wiebe!", "Thanos!", "pumpkin", "desktop", "database", "crossroads", "secret!",
            "teacher", "redwood", "deliver", "computer", "political", "sadness", "fight!"]
word = random.choice(wordList)
word_listform = list(word)
guesseslft = 8
prior_guesses = []
legal_letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
print(legal_letters)
oppo_letters = word.swapcase()
anti_letters = list(oppo_letters)
print(oppo_letters)
disp_list = []
for i in range(len(word_listform)):
    if word_listform[i] in legal_letters:
        disp_list += "_"
    else:
        disp_list += word_listform[i]
while guesseslft > 0 and "_" in disp_list:
    print(' '.join(disp_list))
    print("Guesses left: %d" % guesseslft)
    guessltr = input("Guess a letter")
    if guessltr not in prior_guesses and guessltr in legal_letters and guessltr in word_listform:
        for letter in range(len(word_listform)):
            if guessltr == word_listform[letter]:
                disp_list[letter] = word_listform[letter]
                prior_guesses.append(guessltr)
    elif guessltr in anti_letters:
        for letter in range(len(oppo_letters)):
            if guessltr == anti_letters[letter]:
                disp_list[letter] = word_listform[letter]
                prior_guesses.append(guessltr)
    elif guessltr in prior_guesses:
        print("You already guessed that.")
    if guessltr not in word_listform:
        guesseslft -= 1
        print("Incorrect")
        prior_guesses.append(guessltr)
if guesseslft == 0:
    print("You ran out of turns. Heisenwiebe won.")
    print("The actual word was %s" % word)
if "_" not in disp_list:
    print("Congratulations! You guessed the word!")
    print("The word was %s" % word)
