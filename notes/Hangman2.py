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

while guesseslft > 0 and letterslft > 0:
guessltr = input("Guess a letter")

for guessltr in word_listform:
    print(' '.join(disp_list))
    #   print(prior_guesses)
    print("Guesses left: %d" % guesseslft)
    print("Letters left: %d" % letterslft)
    if wordidx == word.index(guessltr):
        prior_guesses.append(guessltr)
        disp_list.pop(wordidx)
        disp_list.insert(wordidx, guessltr)
        letterslft -= 1