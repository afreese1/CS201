'''

Alyssa Freese
CS 201
9/15/2014
Lab 3: Conditionals

Age Classifier

States what classification a given age is

'''

age = int(input("Enter age"))

if age <= 1:
        print("infant")
elif age < 13:
        print("child")
elif age < 20:
        print("teenager")
else:
        print("adult")


''' Works as expected '''
