#import shenanigans
import time
import sys
import random
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#pravidla hry
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}
#volby bot
choices_bot = {
  "1": "rock",
  "2": "paper",
  "3": "scissors"
}
#volby hráč
choices_pl = {
  "1": "rock",
  "2": "paper",
  "3": "scissors"
}
#some nice fella v quora se zeptal, a nějaký iq pán to vymyslel. :)
def delay_print1(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


#porovnání co vyhraje

def hra(human, bot): #definování formátu vstupu
    if bot == rules[human]: #Vyhrál bot nad člověkem?
                            # #když bot má stejný jako přiřazená hodnota k výběru human (volby, 1 = rock atd..)
        print (f"The Bot chose {bot}, you chose {human}. {human} wins.")
        delay_print1("Bot: NOOOOO. I Lost!\n")
    elif human == rules[bot]:
        print (f"The Bot chose {bot}, you chose {human}. {bot} wins.")
        delay_print1("Bot: HAHA you fool! You thought you would outsmart me!\n")
    else:
        print (f"The Bot chose {bot}, you chose {human}. You both chose the same. It's a tie!")
        delay_print1("Bot: Well. That's awkward...\n")

#interaktivní část


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

def delay_printch(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)


while True:
    clear = lambda: os.system('cls') #buďto to udělá co má, nebo to vyhodí . Podle toho, zda jsi v pycharm, nebo vscode (vscode funguje)
    print("Hi player!")
    delay_print("WELCOME\n")
    print("to the awesome")
    time.sleep(0.5)
    delay_print("ROCK PAPER SCISSORS game©\n") #v plánu bylo to mít bold a nějak vyznačený. Ale too much work a ještě bych dostal body mínus
    time.sleep(1)
    print("Now. let's begin. The rules are simple.")
    print("rock beats scissors, scissors beat paper, paper beats rock")
    print("Choices: ")
    delay_printch("1 = rock, 2 = paper, 3 = scissors (or type -quit- to quit)\n")
    time.sleep(0.5)
    choice = input("Now the fate of yours, lies in your hand. What will you choose?: ")
    if choice == ("quit"):
        print("Oke see ya later..")
        break
    else:
        try:
            a = int(choice)
            b = str(choice)
            rnum = random.randint(1, 3)
            rstrg = str(rnum)
            c = choices_pl[b]
            d = choices_bot[rstrg]
            print (f"Bot: So you chose {c}.")
            delay_print1(f"Bot: Well... I chose: {d}\n")
            hra(choices_pl[b], choices_bot[rstrg])
            time.sleep(5)
            clear()
        except ValueError:
            print("That was not a number!!! I am mad. Bye...")
            time.sleep(5)
            clear()
            break
        except KeyError:
            print(f"ey. 1 to 3 (or quit)... not {b}... You tried to fool me.... Bye... ")
            time.sleep(5)
            clear()
            break

