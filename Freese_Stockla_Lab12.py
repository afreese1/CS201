'''
Alyssa Freese and Amanda Stockla
CS201
December 3, 2014
Lab 12

Algorithm:

1. ask user to input numbers to form a list
2. ask if user wants to search or sort
3. based on users answer, ask for which method he/she would prefer
4. call on appropriate funciton
5. return value at end
6. prints accordingly

Test Cases:

1) Linear Search

   L=[5,8,9,2,3]  x=9  -> found

   L=[5,8,9,2,3]  x=4  -> not found

   works as expected
   

2) Binary Search

   L=[4,7,9,3,1]  x=1  -> found

   L=[4,7,9,3,1]  x=5  -> not found

   works as expected
   

3) Selection Sort

   L=[3,9,6,1,5]  ->  [1,3,5,6,9]

   works as expected
   

4) Merge Sort

   L=[9,7,8,1,4]  ->  [1,4,7,8,9]

   works as expected

'''

def main():

    L=[]

    num=int(input("Enter an integer. Type -1 to stop: "))
    
    #create the list of numbers
    while num!=-1:
        L.append(num)
        num=int(input("Enter an integer. Type -1 to stop: "))

    print(L)
    print()

    #ask user whether he/she wants to search or sort and by which method.
    #call on appropriate function for each
    choose=input("Would you like to search or sort? ")
    if choose=='search':
        search=input("Would you like use linear or binary search? ")
        if search=='linear':
            place=linear(L)
        else:
            place=binary(L)
    else:
        search=input("Would you like to use selection or merge sort? ")
        if search=='selection':
            sort=selection(L)
            place=-2
        else:
            place=-2
            sort=mergesort(L)

    if place==-1:
        print("not found")
    elif place==-2:
        print(sort)
    else:
        print("found")


    
def linear(L):
    
    x=int(input("Enter number you want to find: "))
    for i in range(len(L)):
        if L[i]==x:
            return i
    return -1

def binary(L):

    L=selection(L)
    
    x=int(input("Enter number you want to find: "))
                  
    low=0
    high=len(L)-1
    while low<=high:
        mid=int((low+high)/2)
        item=L[mid]
        if x==item:
            return mid
        elif x<item:
            high=mid-1
        else:
            low=mid+1
    return -1
        
def selection(L):

    n=len(L)

    for bottom in range(n-1):
        mp=bottom
        for i in range(bottom+1, n):
            if L[i]<L[mp]:
                mp = i
        L[bottom], L[mp]=L[mp], L[bottom]
    return L

def mergesort(L):

    n=len(L)
    if n>1:
        m=n//2
        L1, L2=L[:m], L[m:]
        mergesort(L1)
        mergesort(L2)
        merge(L1, L2, L)
    return L

def merge(L1, L2, L3):
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(L1), len(L2)
    while i1<n1 and i2<n2:
        if L1[i1]<L2[i2]:
            L3[i3]=L1[i1]
            i1=i1+1
        else:
            L3[i3]=L2[i2]
            i2=i2+1
        i3=i3+1

    while i1<n1:
        L3[i3]=L1[i1]
        i1=i1+1
        i3=i3+1
        
    while i2<n2:
        L3[i3]=L2[i2]
        i2=i2+1
        i3=i3+1
    L=L1+L2+L3
    return L3

main()
