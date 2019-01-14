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
totalword = anti_letters + word_listform
attsolve = False
disp_list = []
disp_listcopy = []
for i in range(len(word_listform)):
    if word_listform[i] in legal_letters:
        disp_list += "_"
    else:
        disp_list += word_listform[i]
solve = False
num = 0

'''
def copy():
    disp_listcopy = disp_list


def restore():
    disp_list = disp_listcopy
'''

while guesseslft > 0 and "_" in disp_list:
    print(' '.join(disp_list))
    attsolve = False
    print("Guesses left: %d" % guesseslft)
    asksolve = input("Would you like to solve the entire word? Y for yes N for no:")
    if asksolve == "Y" or asksolve == "y":
        attsolve = True
        guesswrd = input("Enter te word")
        guesswrd = list(guesswrd)
        for i in range(len(word_listform)):
            if guesswrd[i] == word_listform[i] or guesswrd[i] == anti_letters[i]:
                disp_list[i] = word_listform[i]
                num += 1

        if num == len(word_listform):
            solve = True
        else:
            print("Incorect")
            guesseslft -= 1
             disp_list = disp_listcopy
    if "_" in disp_list and solve is False and attsolve is False:
        guessltr = input("Guess a letter")
        if guessltr not in prior_guesses and guessltr in legal_letters and guessltr in totalword:
            for letter in range(len(word_listform)):
                if guessltr == word_listform[letter]:
                    disp_list[letter] = word_listform[letter]
                    prior_guesses.append(guessltr)

        elif guessltr not in anti_letters and guessltr in legal_letters and guessltr not in word_listform:
            print("Incorrect")
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
