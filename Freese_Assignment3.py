'''
Alyssa Freese
CS201
December 3, 2014
Programming Assignment

Alorithm:

MAIN
1. create a random 5 digit secret number
2. if the first digit of the secret number is 0, generate a new secret number
3. introduce user to game
3. call on guess and cary over value of secret number

GUESS
1. set a maximum amount of guesses and start of number of guesses at 0
2. ask user if he/she wants to play
3. in the while loop, set count and correct equal to 0
4. ask user to input his/her guess
5. validate that the guess is a five digit number
6. after guess, increase number of guesses by one
7. convert guess into a string
8. read through digits in secret (list) and for each digit convert to a string
   and check if its in guess
9. if digit is in guess, then increase count by one
10. create toop to check if values at each point are the same for guess and
    for the secret number, which must be converted to a string
11. if the values are the same, then correct is increased by one
12. print the number of values in the guess that are in the secret number
    and the number of values that are in the correct position with number of guesses
13. ask user if he/she wants to guess again
14. if yes, then repeats process, if no, print out number of guesses so far
15. if number correct equals five, then the player wins. Print congratulations
    with number of guesses taken
16. if number of guesses reaches max, game is over and player loses

Test Cases:

1) give 2 guesses then say that you do not want to continue
   print - You lost. You guessed the secret number a total of 2 times

   works as expected

2) take 10 random guesses
   print - Oops, you ran out of guesses. Better luck next time!

   works as expected

3) guess secret number in 5 tries
   print - Congratulations! You won! It took you 5 guesses

   works as expected

'''

import random

def main():

    #generate a random 5 digit number without repeats
    secret=random.sample(range(0,10),5)

    #if first digit of number is 0, generate a new number
    while secret[0]==0:
        secret=random.sample(range(0,10),5)

    print("Welcome to Secret Number!")
    print()
    #let player know how many tries they will recieve
    print("You have 10 tries to guess what the secret number is.")
    print()
    #call on guess, and carry over value of secret
    guess(secret)
        

def guess(s):

    #set maximum number of guesses
    max_guess=10

    num_guess=0

    #ask user if he/she wants to play
    cont=input("Wanna play? yes or no ")
    print()

    #create while loop to continue guessing as long as player agrees
    while cont=='yes':

        count=0
        correct=0

        #ask player to input guess
        guess=int(input("Guess what the five digit secret number is: "))

        #validate that guess is a five digit number
        while guess<10000 or guess>99999:
            guess=int(input("Guess must be five digits: "))

        num_guess=num_guess+1

        #convert guess to a string
        g=str(guess)

        for digit in s:
            #convert each digit in secret to a string to compare to guess
            digit=str(digit)
            if digit in g:
                count=count+1
            
        for i in range(5):
            #convert values in secret at each position to a string to compare to guess
            if g[i]==str(s[i]):
                correct=correct+1

        #print the number if guess, the number of digits that appear in secret number
        #and the number of digits that are in the correct position
        print("In your guess there are",count,"numbers in the secret number and",correct,"of them are in the correct position")
        print("You have guessed",num_guess,"times")
        print()
        
        #if guesses reach max, the game ends and the player loses
        if num_guess==10:
            print("Oops, you ran out of guesses. Better luck next time!")
            cont='no'

        #if the number of digits in the correct position equal 5, then
        #the player wins
        elif correct==5:
            print("Congratulations! You won! It took you",num_guess,"guesses")
            cont='no'
        else:
            #ask player if they would like to guess again
            cont=input("Would you like to try again? ")
            if cont=='no':
                print("You lost. You guessed the secret number a total of",num_guess,"times")
    
#call on main function
main()

