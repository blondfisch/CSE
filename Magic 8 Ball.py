import random
import time


def start():
    print('''   
       _.a$$$$$a._
     ,$$$$$$$$$$$$$.
   ,$$$$$$$$$$$$$$$$$.
  d$$$$$$$$$$$$$$$$$$$b
 d$$$$$$$$~'"`~$$$$$$$$b
($$$$$$$p   _   q$$$$$$$)
$$$$$$$$   (_)   $$$$$$$$
$$$$$$$$   (_)   $$$$$$$$
($$$$$$$b       d$$$$$$$)
 q$$$$$$$$a._.a$$$$$$$$p
  q$$$$$$$$$$$$$$$$$$$p
   `$$$$$$$$$$$$$$$$$'
     `$$$$$$$$$$$$$'
       `~$$$$$$$~'
''')
    print("You seek the power of the 8 ball. Ask a question and you shall receive an answer.\nOr you can request to add"
          "answers to the magnificent 8 ball.")
    name = input("What is your name? ").title()
    return name


start()
playing = True
response_added = 0
questions_asked = 0
while playing is True:
    outputs = ["that is never going to happen", "all signs point to yes", "I don't get paid enough for that",
               "try again later", "absolutely", "very high chance of it happening", "my sources tell me yes",
               "you're an idiot if you think there is a chance", "I'm not going to tell you", "please repeat that",
               "I think it is probable"]
    answer = input("Do you seek answers or do you want to improve the glorious 8 ball?").lower()
    if "improve" in answer:
        addition = input("What response would you like to add to the 8 ball? ")
        outputs.append(addition)
        response_added += 1
    
    elif "q " in answer or "quit" in answer:
        print("{0}, thank you for visiting the 8 ball. You added {1} responses and asked {2} questions.".format(name,
              response_added, questions_asked))
        time.sleep(2)
        print('''
        ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """"........
        Come back soon!''')
        playing = False
    elif "knowledge" in answer or answer in "question " or "ask" in answer:
        questions_asked += 1
        print(name + ", " + random.choice(outputs))
