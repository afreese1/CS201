'''

Alyssa Freese and Amanda Stockla
CS201
October 14, 2014
Lab 7 Question 3

Rock Paper Scissors

Test Cases:

1)  This programs allows a person to play rock paper scissors against a computer.

Enter rock, paper, or scissors: scissors
paper
scissors wins, you win
>>> ================================ RESTART ================================
>>> 
This programs allows a person to play rock paper scissors against a computer.

Enter rock, paper, or scissors: rock
rock
It's a tie! try again...
Enter rock, paper, or scissors: paper
scissors
scissors wins, you win

'''

#import random
import random

#asks user for rock paper or scissors
def main():
    cont='yes'
    while cont=='yes':
        play=0
        play=input("Enter rock, paper, or scissors: ")
        #calls rps function
        rps(play)
        print()
        cont=input("Would you like to play again? yes or no: ")
        print()
    
#defines program
def intro():
    print("This programs allows a person to play rock paper scissors against a computer.")
    print()
    #calls main function
    main()

#randomizes computer's choice
def rps(play):
    h=random.randrange(3)
    if h==0:
        print("paper")
        play2="paper"
    elif h==1:
        print("rock")
        play2="rock"
    else:
        print("scissors")
        play2="scissors"
    #calls win function
    win(play2,play)
    
#gives all possible outcomes of the game and forces a tiebreaker if a tie is reached
def win(play2,play):
    if play=="rock" and play2=="paper":
        print("Paper wins, you lose")
    elif play=="paper" and play2=="rock":
        print("paper wins, you win")
    elif play=="rock" and play2=="scissors":
        print("scissors wins, you lose")
    elif play=="paper" and play2=="scissors":
        print("scissors wins, you win")
    elif play=="scissors" and play2=="rock":
        print("rock wins, you lose")
    elif play=="scissors" and play2=="paper":
        print("scissors wins, you win")
    else:
        print("It's a tie! try again...")
        #returns to main function if it's a tie
        return main()
    
#calls intro function
intro()    
