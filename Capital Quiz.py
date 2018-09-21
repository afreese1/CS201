'''
Alyssa Freese and Amanda Stockla
CS201
November 24, 2014
Lab 11 Question 1

Capital Quiz

Algorithm:
1. create dictionary with states as keys as capitals as values
2. create a while loop so that the program continues to ask for capitals until
   it runs out of states to ask about
3. print random key
4. ask user to input answer
5. compare users answer to correct answer
6. print correct and add one to count if answer matches
7. print incorrect and give answer if they don't match
8. at end print number correct and number incorrect

works as expected

'''
import random

cap={"Washington":"Olympia","Oregon":"Salem",
                    "California":"Sacramento","Ohio":"Columbus",
                    "Nebraska":"Lincoln","Colorado":"Denver",
                    "Michigan":"Lansing","Massachusetts":"Boston",
                    "Florida":"Tallahassee","Texas":"Austin",
                    "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",
                    "Alaska":"Juneau","Utah":"Salt Lake City",
                    "New Mexico":"Santa Fe","North Dakota":"Bismarck",
                    "South Dakota":"Pierre","West Virginia":"Charleston",
                    "Virginia":"Richmond","New Jersey":"Trenton",
                    "Minnesota":"Saint Paul","Illinois":"Springfield",
                    "Indiana":"Indianapolis","Kentucky":"Frankfort",
                    "Tennessee":"Nashville","Georgia":"Atlanta",
                    "Alabama":"Montgomery","Mississippi":"Jackson",
                    "North Carolina":"Raleigh","South Carolina":"Columbia",
                    "Maine":"Augusta","Vermont":"Montpelier",
                    "New Hampshire":"Concord","Connecticut":"Hartford",
                    "Rhode Island":"Providence","Wyoming":"Cheyenne",
                    "Montana":"Helena","Kansas":"Topeka",
                    "Iowa":"Des Moines","Pennsylvania":"Harrisburg",
                    "Maryland":"Annapolis","Missouri":"Jefferson City",
                    "Arizona":"Phoenix","Nevada":"Carson City",
                    "New York":"Albany","Wisconsin":"Madison",
                    "Delaware":"Dover","Idaho":"Boise",
                    "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}


count=0
#create loop while dictionary still has keys left
while len(cap)>0:
    #choose random key from dictionary
    P=random.choice(list(cap.keys()))
    correct_answer=cap.get(P)
    print ("What is the capital of",P,"?")
    answer=input("answer: ")
    #compare input answer to correct answer
    if answer.lower()==correct_answer.lower():
        print ("That is Correct!")
        print()
        count=count+1
    else:
        print ("That's Incorrect.")
        print ("The correct answer is",correct_answer)
        print()
    #delete key from dictionary
    del cap[P]

print ("You got",count,"correct and",50-count,"wrong")




