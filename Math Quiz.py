'''

Alyssa Freese and Amanda Stockla
CS201
October 14, 2014
Lab 7 Question 1

Math Quiz

Test Cases:

1. 759+735 =
    input = 900
    Should print incorrect and ask for continue = yes
    107 + 370 =
    input = 477
    should print congratulations! and ask for continue = no
    print: 1 correct out of 2

'''

import random

#explains what this program will do
def intro():
    print("This program will display two random numbers that are to be added")
    print("to help test your addition skills")
    print()
    
#define initial count and correct values
def main():
    count=0
    correct=0
    #calls intro
    intro()
    #prints 2 numbers to be added and asks user if he/she wants to continue (loop)
    cont="yes"
    while cont=="yes":
        count=count+1
        num1 = random.randrange(100,1000)
        num2 = random.randrange(100,1000)
        print(num1,"+",num2,"= ", end='')
        if solve(num1,num2):
            correct=correct+1
        cont=input("Would you like to continue? 'yes' or 'no' ")
    print("You have answered",correct,"correct out of",count,"questions")

#finds solution to problem and tells user whether or no he/she is correct
def solve(num1,num2):
    answer=int(input())
    if answer==num1+num2:
        print("Congratulations!")
        #returns value to main function
        return True
    else:
        print("That is incorrect. The correct answer is",num1+num2)
        #returns value to main function
        return False

#calls main
main()
