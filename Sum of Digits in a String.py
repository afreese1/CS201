'''
Alyssa Freese and Amanda Stockla
CS201
November 3, 2014
Lab 10 Question 1

Sum of Digits in a String

Algorithm:

1. Ask user to enter a series of numbers
2. convert series into a string
3. create loop to read each character in the string
4. for each character, convert it to an integer and add it to sum
5. print sum

Test Cases:

1) Series = 2514
   expected outcome = 2+5+1+4 = 12

   works as expected

2) Series = 692153
   expected outcome = 6+9+2+1+5+3 = 26

   works as expected

3) Series = 50912
   expected outcome = 5+0+9+1+2 = 17

   works as expected

'''

#user enters series of numbers
series=input("Enter a series of single-digit numbers with nothing separating them: ")

#creates a string
series_string=series

#reads each character in string and converts to integer
#adds each to sum
sum=0
for ch in series_string:
    ch=int(ch)
    sum=sum+ch
    
#prints the sum
print("The sum of all the sintle digit numbers is",sum)
