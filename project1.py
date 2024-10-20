''' ROCK PAPER SCISSORS GAME'''
'''
1-> ROCK
-1-> PAPER
0-> SCISSORS
'''
import random
computer=random.choice([1, -1, 0])
choice=input("Enter your choice: ")
youdict={'ROCK':1, 'PAPER':-1, 'SCISSORS':0}
reversedict={1: 'ROCK', -1:'PAPER', 0:'SCISSORS'}
you=youdict[choice]
print(f"You chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")
if(computer == you):
    print("GAME DRAW")
else:
    if(computer == 1 and you == -1):
        print("You loose!")
    elif(computer == 1 and you == 0):
        print("You loose!")
    elif(computer == -1 and you == 1):
        print("You Won!")
    elif(computer == -1 and you == 0):
        print("You won!")
    elif(computer == 0 and you == 1):
        print("You won!")
    elif(computer == 0 and you == -1):
        print("You loose!")
    else:
        print("SOMETHING WENT WRONG!")
