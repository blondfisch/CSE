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
    bleep = input("What is your name? ").title()
    return bleep


name = start()


def randowm_answers(q_counter, a_counter, their_name, options, loop_trick):
    guessing = True
    while guessing is True:
        question = input("What is your question, mortal?").lower()
        if question in "quit" and "?" not in question:
            print("Goodbye, come again soon.")
            guessing = False
        elif "quit all" in question:
            time.sleep(2)
            print('''
                               ____
                           ,dP9CGI88@b,
                         ,IP  _   Y888@@b,
                        dIi  (_)   G8h88@b
                        dCII  (_)   G8888@@b
                        GCCIi     ,GG8888@@@
                        GGCCCCCCCGGG88888@@@
                        GGGGCCCGGGG88888@@@@...
                        Y8UGGGGG8888888@@@@P.....
                        Y88888888888@@@@@P......
                        `Y8888888@@@@@@@P'......
                           `@@@@@@@@@P'.......
                               """"........
                               Come back soon!''')
            return "{0}, thank you for visiting the 8 ball. You added {1} responses and asked {2} questions.".format(
                their_name, a_counter, q_counter)

        elif "zoomer" in question or "boomer" in question:
            print("{}, you absolutely are one. The first step to overcoming the disease is admitting you "
                  "have it.".format(name))
        elif "infinity stone" in question:
            print("""
MMMMMMMMMMMMMMMMMMMMMMMMMMMWXOxol:;,,,,,;;:loxOKK0kxolokKWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNKNMMMWN0xlc;'.................',:lodxkkddoox0NMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWKxxkKNNOo:'....,,,'''''''''''''''',cxkxollldO0kl::cxKWMMMMMMMMMMMMMM
MMMMMMMMMXxlldKXkc'..........................,d0XWMMWO:. 'ckK0o;.;dXMMMMMMMMMMMM
MMMMMMWKl:lOXOc'.....          .            .oXNWMWO:.   .  .l0Xk:..oKWMMMMMMMMM
MMMMMNd,lKXk;....                           :KXNMMO.  .cO0Ol. .;kX0c..dNMMMMMMMM
MMMMNo:OXk;..                              .xXXWMMd   ,KWWMX;  .;ckN0:.:XMMMMMMM
MMWWkdK0:..                                'ONXWMM0'   ;dkx:. .:xo;c0Nx':KMWMMMM
MMWK0Kd.        ....''........             'OXXNMMM0c'.       ....'.'xN0;lNMMMMM
MMWNKc...       . ,l;',;::,'....           .xXXXWMMMMNd.  .lkkdcc, ...lXKoOMMMMM
Xkl:.           . ,c..o0000ko:..            :KXXXWMMMX;  .xMMMMXolo.'l':KXKWMMMM
'               . 'l' c0KKXXK0o'.           .oXXXXNWM0'   oNMMMWo.dklOk.:XMMMMMM
.''....         . 'l'.o0KXXXXXO;....    .    .oKXXXXNNl   .:xOxc. '0WWWo.lNMMMMM
l,,'......   .   .;:.:OKXXXXXXO;.. .....''...  :OXXXXXKo.        .:0MWN0;.xWMMMM
O,':,......  ..  'c',xKKXXXXXOc.    ..........  .cOXXXXX0dc;,,:cd0XNWMNNx.;XMMMM
NolK0c. .........'. .dKXXXXOo'.   ..';:;'. .....  .;dOXXXXXXXXXXXXXNWMWN0,.dWWMM
NodXXx.   ........  .dXXKkl'.  .';:okkdc;. .. .'.    .,cdk0KKXXXXXXXWMW0o' :NWWW
X:,dkOxc;'......:xxdkOko:.....,cocc0WWWkc' ... .'.        ..',;;:ccoKMWd'. ,KMMX
o.   .';,.......'::;'.. ...';lOXXX0OXMMWWx,,,:,.''               .':KMWd'. .OMMO
;    ....  ....       ..';dOkkKNWMMX0XMMMOcol:c'.,.              ''lNMNo'. .OMMx
k'  ..:do:'.   ...,,',lxdxKNWWXKNMMMKxxkklckdod;...              .,xWMK:'. 'OMWl
WKxoc;;xXNXOookO0KXXkONNNKKMMMW00WWXd,,;,',cokkl.               .':KMMk,'. ,KMK;
MMMMWN0O0K0xod0XNWWKkKMMMN0XMNKl;oOo:kWWWO;,,;do.               .,xWMNl'.  lWMx.
MMMMMMMMM0ldkxloO0k;'o0K0d;:ddc;dXWW00X0kl:ol'..               .'cKMMO;'. .OMNc.
MMMMMMWNOcxWMN0KWWXdxKKKKxcxXWNO0WMWOllc;::,.                 ..;OWMXc'.  cNMx.:
MMWKxl;'.lXMW0ONMMNOKMMMMNKXMMM0dkOd:::,'.                   ..,kWMNd'.  '0MK,.k
MWd'.   .':ooclOXXOokWMMMKkKWWXdcc;'..                      ..;kWMWx,.  .kMX:.lN
MNl...         .....,coddl:looc:,..                        .':OWMNd,.  .xWXc.cXM
MMNkc;'....             ......                           ..,lKWWKl'.  .xWX:.cXMM
MMMMWNKkd,  .....               .......                ..':kNMNx;.   'OW0;'dNMMM
MWWMMMMMMO.   ...,,,,,'''''.........                ..'':xXWXkc.   .cKNd,:0WMMMM
MMMMMMMMMWx. .''...',,,,''..........',,'..      ...'',lkNWKd:.    ,kNO:;kNMMMMMM
MMMMMMMMMMWO,.,ll;'..........'',,,,,''.........''';lxKNKkl'.    ,xX0l:dXMMMMMMMM
MMMMMMMMMMMMKc.'clc;'....................'''';cdkKK0xc,..   .;kXOl:dXMMMMMMMMMM
MMMMMMMMMMMMMW0o:,,;,''.....'''.'''''',;;:ldxO00Oxl;..    .,oO0xllxNMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNOo:'....''',;;::cllooddxxxdol:,...    .;okkxdodKWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWKko:,.....'',;;;,,''......    .':okKK0OkOKWMMMMMMMMMMMMMMMMM
XXXXXXXXXXXXXXXXXXXXXXXX0kdlc;'......  ......';cldk0KXXKKKXXXXXXXXXXXXXXXXXKKXXX
            """)
            time.sleep(5)
            print("You have upset the balance of the universe. You should not have looked for this, yet you did."
                  " Dread it, run from it, destiny arrives all the same.")
            time.sleep(5)
            print("""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWK0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0OkKWMMMMMMMMXKX0KNKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l,,.'xWMMMMMMWXKKKKKKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc,;,. 'OWMWNXK00KK0KXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd:::,...dWWXK0OO0Okxxk0KKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk::cc'...oNMWNKO0OkOkxxkkOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx:odc'...lXMMMWXKKK0K0O0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdlkOl'...lXMMMWXK000XWXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKolxdc,...cXMMMMWK0XNNMMWNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMOldOOo,.',:OWMMMMNNWMWWXOdlcdKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdoO0x:'.,,oNMWMMMMWXOxlc;,',lkkkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOok0xc;,',:OWWWNX0Odoxd:..;coko,,oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxdkkl;,'''cxkkkkkkxxx:..,:dk0d,..oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxloo:;cl:,',;lkKKKkc,. .;oOKKx;..:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXd:cl:;:ll;,'.'coo:,....,cdxxkxc'.;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMNK0dc:;;;;:cc,''...........,clllc;'.,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Kk;..,:ccll::;.......';:oOd,;dOko:,...:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdo,   .'lxkkdc;'  ..,;lkKNMO,'cloooc,'.'xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKdol:c:'...,oddkkdcc;.  .''',;dN0:;oxkkkdl:'.,dXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOxl,,;lxkkxoddlclx0xl:,.  ..''..,oo;ldlccc;,... .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0oc;;;:llddodo:;clkXOl;'.   .......,,:lc;'....   .kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkocxxl:;;:ll:co,,cldOd:'....  ..   .,,,:lolc;,'...cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNklodxkd:;:okxc;c:',:clc,'''..      .',,;::,''''.. .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xc;cdxdo::coddc,;c::ccl:,'',,,'    ..',..,,''.......dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMKoooc:ckxllc:clol;,:l:cllc:;,',,,'.. ..''..',,',''''....kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWOloxl;:xo;:::lolc:cccc::cc:;,,,'''''...'..,:,'',,',''...lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkkkl:;:;,::cooolcclddl::::;,,,',,',,.  ..:oc;;,',,'.,'.,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xo;::,;::clxxl:,,::co:,,,,,,,,,'...   .;oo:;;::cl;.''.,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd;;l:;:lodkOdl:,'..;c'...'';:'       .:cc:::;:lo:,'..dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkclo::dO0KKkcc:,. ';.....',,.      .,;;;';;,;oko;,'lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWkll;;d0XNN0d:;,..:c;:,......      .'',.....;d0d;'cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWkl;,o0XXXXOc'......,'....        .'... ...'ldc':0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxc;:xKXXK0d'... ..'..           ....    ..';',kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo:',oO00kc.....;....           ..       ...'xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l,'';:,'.... ..  .         ..            'xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd;,,,...........       ..;'.           'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKc..',.   .....  .....':;'....       .:0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:,,'.    .....';;;;;;'..;,...  .....;kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;'''.   .loolc::,....,,;,. ..  .....cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd,;l,...:xdcllc,.....,;c:.  ........cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            """)
            time.sleep(15)
            print("Did you do it?")
            time.sleep(3)
            print("Yes")
            time.sleep(3)
            print("What did it cost?")
            time.sleep(2)
            print("44 lines of code.")
            looptrick = False
            guessing = False

        else:
            q_counter += 1
            print("I'm thinking...")
            time.sleep(2.15)
            print(name + ", " + random.choice(options))


def add_response(thing_added, options):
    addition = input("What response would you like to add to the 8 ball? ")
    options.append(addition)
    thing_added += 1
    responses = open("8ball.txt", "w+")
    responses.write(addition)
    print("Your response has been uploaded to the mainframe. The ultimate 8 ball thanks you.")


def the_8_ball():
    playing = True
    response_added = 0
    questions_asked = 0
    while playing is True:
        outputs = ["that is never going to happen.", "all signs point to yes.", "I don't get paid enough for that.",
                   "try again later.", "absolutely.", "very high chance of it happening.", "my sources tell me yes.",
                   "you're an idiot if you think there is a chance.", "I'm not going to tell you.",
                   "please repeat that.", "I think it is probable.", "pay me and I might tell you...I'm still waiting.",
                   "Do you think I pay attention to stuff like that?", "don't worry about it.",
                   "let me nap first...oh wait I'm a computer.", "whatever you want to happen will happen."
                   ]
        answer = input("Do you seek knowledge or do you want to improve the glorious 8 ball?").lower()
        if "improve" in answer:
            add_response(response_added, outputs)
        elif "q " in answer or "quit" in answer:
            print("{0}, thank you for visiting the 8 ball. You added {1} responses and asked {2} "
                  "questions.".format(name, response_added, questions_asked))
            time.sleep(2)
            print('''
           ____
       ,dP9CGI88@b,
     ,IP  _   Y888@@b,
    dIi  (_)   G8h88@b
    dCII  (_)   G8888@@b
    GCCIi     ,GG8888@@@
    GGCCCCCCCGGG88888@@@
    GGGGCCCGGGG88888@@@@...
    Y8UGGGGG8888888@@@@P.....
    Y88888888888@@@@@P......
    `Y8888888@@@@@@@P'......
       `@@@@@@@@@P'.......
           """"........
           Come back soon!''')
            playing = False
        elif "knowledge" in answer or answer in "question " or "ask" in answer or "answer" in answer:
            randowm_answers(response_added, questions_asked, name, outputs, playing)


print(the_8_ball())
