'''

Alyssa Freese
CS 201
9/15/2014
Lab 3: Conditionals

Money Counting Game

'''

pennies=int(input("Enter number of pennies"))
nickels=int(input("Enter number of nickels"))
dimes=int(input("Enter number of dimes"))
quarters=int(input("Enter number of quarters"))

if pennies+(nickels*5)+(dimes*10)+(quarters*25)==100:
    print("Congratulations, you won!")
elif pennies + (nickels*5) + (dimes*10) + (quarters*25) > 100:
    print("The total is more than one dollar")
else:
    print("The total is less than one dollar")

''' Works as expected '''
