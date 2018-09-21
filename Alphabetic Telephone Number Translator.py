'''
Alyssa Freese and Amanda Stockla
CS201
November 3, 2014
Lab 10 Question 2

Alphabetic Telephone Number Translator

Algorithm:

1. ask user to enter a 10 character telephone number
2. create an empty list
3. convert the entered telephone number into a string
4. create a loop so that each character in the telephone number is checked
   to fit the criteria in each if statement in order to determine what number
   each letter is equivalent to
5. append the list with the numbers in the series, the dashes and
   each equivalent value to the letters
6. print each element in the list

Test Cases:

1) tel_num = 555-GET-FOOD
   expected outcome = 555-438-3663

   works as expected

2) tel_num= 874-HAV-EFUN
   expected outcome = 874-428-3386

   works as expected

3) tel_num = 790-VOT-E4ME
   expected outcome = 790-868-3463

   works as expected

'''

#ask user to input telephone number
tel_num=input("Enter a 10-character telephone number in the format XXX-XXX-XXXX: ")

tel_list=[]

#convert to string
tel_string=tel_num

#read through string and determine what value will be appended to empty list
for num in tel_string:
    if num=='A' or num== 'B' or num== 'C':
        tel_list.append(2)
    elif num=='D' or num== 'E' or num== 'F':
        tel_list.append(3)
    elif num=='G' or num== 'H' or num== 'I':
        tel_list.append(4)
    elif num=='J' or num== 'K' or num== 'L':
        tel_list.append(5)
    elif num=='M' or num== 'N' or num== 'O':
        tel_list.append(6)
    elif num=='P' or num== 'Q' or num== 'R' or num== 'S':
        tel_list.append(7)
    elif num=='T' or num== 'U' or num== 'V':
        tel_list.append(8)
    elif num=='W' or num== 'X' or num== 'Y' or num== 'Z':
        tel_list.append(9)
    elif num=='-':
        tel_list.append('-')
    else:
        num=int(num)
        tel_list.append(num)

#prints out each element in the list on one line
for element in tel_list:
    print(element, end='')
    
    
