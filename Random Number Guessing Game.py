'''

Alyssa Freese and Amanda Stockla
CS201
October 14, 2014
Lab 7 Question 2

Random Number Guessing Game

Test Cases:

1) Enter your guess 60
Too high, try again.
Enter your guess 50
Too high, try again.
Enter your guess 40
Too high, try again.
Enter your guess 30
Too high, try again.
Enter your guess 20
Too high, try again.
Enter your guess 10
Too low, try again.
Enter your guess 16
Too high, try again.
Enter your guess 14
Too high, try again.
Enter your guess 12
Too high, try again.
Enter your guess 11
Congratulations!
You have guessed correctly after 10 tries

'''

#imports random program
import random

#defines initial randomized number
def main():
    #calls intro
    intro()
    cont='yes'
    while cont=='yes':
        count=1
        number=random.randint(1,100)
        #calls solve
        solve(number,count)
        cont=input("Would you like to play again? yes or no: ")
        print()

#defines program    
def intro():
    print("This program generates a number between 1 and 100 and has you guess it!")
    print()

#compares a guess to the randomized number
def solve(n,count):
    guess=int(input("Enter your guess: "))
    while guess!=n:
        if guess>100:
            guess=int(input("Invalid.Enter another guess: "))
        elif guess<n:
            count=count+1
            print("Too low, try again.")
            print()
            guess=int(input("Enter your guess: "))
        elif guess>n:
            count=count+1
            print("Too high, try again.")
            print()
            guess=int(input("Enter your guess: "))
        else:
            count=count+1
            guess=int(input("Enter your guess: "))
    if guess==n:
        print("Congratulations!")
        print("You have guessed correctly after",count,"tries")
        print()

#calls main function
main()
