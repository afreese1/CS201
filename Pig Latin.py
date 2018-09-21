'''
Alyssa Freese and Amanda Stockla
CS201
November 3, 2014
Lab 10 Question 3

Pig Latin

Algorithm:

1. ask user to enter a sentence
2. create sentence into a string and remove blank spaces
3. for each word in the string, place it in its own string
4. print out the second to last character of the word, add the first character
   to the back with ay

Test Cases:

1) sentence = Look in the bag
   expected outcome = ooklay niay hetay agbay

   works as expected

2) sentence = i slept most of the night
   expected outcome = iay leptsy ostmay foay hetay ightnay

   works as expected

3) sentence = i can show you the world
   expected outcome = iay ancay howsay ouyay hetay orldway

   works as expected

'''

#ask user to enter a sentence
sentence=input("Enter a sentence: ")

#form sentence into a string a get rid of spaces
sent_string=sentence.split()

print()
print("In Pig Latin this is: ")
print()

#create each word into its own string and print from index one
#to the end of the word, add index 0 and ay at the end
for word in sent_string:
    w_string=word
    print(w_string[1:len(w_string)]+w_string[0]+'ay',end=' ')
