'''
Alyssa Freese and Amanda Stockla
CS201
November 24, 2014
Lab 11 Question 2

File Analysis

Algorithm:
1. ask for file name and open file as read
2. create content into string and split by spaces
3. for each character in the string, append it to empty list
4. test if elements from one list are in another and append them to empty lists
   labeled both, one, two and either

works as expected

'''

    
L1=[]
L2=[]

for i in range(2):

    filename=input("Enter name of file: ")

    file=open(filename,'r')
    content=file.read()
    string=content.split( )
    if i==0:
        #append characters of string to empty list based on what file it's read from
        for ch in string:
            L1.append(ch)
    else:
        for ch in string:
            L2.append(ch)

both=[]
one=[]
two=[]

#compare elements from both lists to find if they are in both, or only one
#append to proper lists
for element in L1:
    if element in L2:
        both.append(element)
    else:
        one.append(element)

for element in L2:
    if element not in L1:
        two.append(element)

either=(one+two)

print()
print("The set of words that appear in both files is: ",both)
print()
print("The set of words that appear in file one is: ",one)
print()
print("The set of words that appear in file two is: ",two)
print()
print("The set of words that appear in either fle but not both is: ",either)

        
    
        
    


