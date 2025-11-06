
import random
def hangman():

    word=random.choice(["pugger","littelepugger","tiger","supermen","thor","pokemon","avengers","savewater","annable"])
    velidLatter=('backdghnoklpxyz')
    turns=10
    guessmade=''
    while len(word)>0:
        main=""
        missed=0
        for latter in word:
            if latter in guessmade:
                main=main+latter
            else:
                main=main+"_"+" "
            if main ==word:
                print(main)
                print("you win!")
                break
            print("guess the word:",main)
            guess=input()
                      
        if guess in velidLatter:
            guessmade=guessmade+guess
        else:
            print("enter a valied character")
            guess=input()

        if guess not in word:
            turns= turns - 1
            if turns == 9:
                print("9 turns left")
                print("--------")
            if turns == 8:
                print("8 turns left")
                print("--------")
                print("    O   ")
            if turns == 7:
                print("7 turns left")
                print("--------")
                print("    O   ")
                print("    |   ")
            if turns == 6:
                print("6 turns left")
                print("--------")
                print("    O   ")
                print("    |   ")
                print("    /   ")
            if turns == 5:
                print("5 turns left")
                print("--------")
                print("    O   ")
                print("    |   ")
                print("    /\  ")
            if turns == 4:
                print("4 turns left")
                print("--------")
                print("    O   ")
                print("    |   ")
                print("   \O   ")
            if turns == 3:
                print("3 turns left")
                print("--------")
                print("    O   ")
                print("    |   ")
                print("   \O/  ")
            if turns == 6:
                print("6 turns left")
                print("--------")
                print("    O   ")
                print("    |   ")
                print("  \O/|  ")
            if turns == 6:
                print("6 turns left")
                print("--------")
                print("    O   ")
                print("    |   ")
                print("  |\O/| ")
                break
    
name=input("enter your name")
print("welcome",name)
print("----------------------")
print("try to guess the word in less then 10 try")
hangman()
print()

