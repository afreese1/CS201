def create ():
    print("create list")
    lst=[]
    element=input("enter element, enter no when done")
    while element!= "no":
          lst.append(int(element))
          element=input("enter element, enter no when done")
    return lst

def binarysearch (x,lst):
    selectionsSort(lst)
    low=0
    high=len(lst)
    while low<=high:
        mid=int((low+high)/2)
        item=lst[mid]
        if x== item:
            return mid
        elif x< item: 
            high = mid-1
        else:
            low=mid+1
    return -1

def linearsearch(x,lst):
    for i in range(len(lst)):
        return i
    return -1

def search (lst):
    x=int(input("which element are you searching for?"))
    choice=input('enter L for linear or B for binary search')
    while choice not in ('L','B'):
        choice=input("error, enter a valid choice")
    if choice == 'L':
        index=linearsearch(x,lst)
    else:
        index=binarysearch(x,lst)
    if index==-1:
        print (x,'is not in the',lst)
    else:
        print (x,'is in',lst,'Its position is', index+1)

def sort (lst):
    choice=input("Enter S for selection or M for merge")
    while choice not in ('S','M'):
          choice=input('enter valid choice; S or M')
    if choice =='s':
          selectionSort(lst)
    else:
          mergeSort(lst)
    print('the sorted list is', lst)

def selectionsort(lst):
    n-len(lst)
    for bottom in range (n-1):
        mp=bottom
        for i in range(bottom+1,n):
            if lst[i]<lst[mp]:
                mp=i
        lst[bottom],lst[mp]=lst[mp],lst[bottom]

def mergesort (lst):
    n=len(lst)
    if n>1:
        m=n//2
        lst1,lst2=lst[:m],lst[m:]
        mergesort(lst1)
        mergesort(lst2)
        merge(lst1, lst2, lst)
    

def merge (lst1,lst2,lst3):
    i1,i2,i3=0,0,0
    n1,n2=len(lst1),len(lst2)
    while i1<n1 and i2<n2:
        if lst1[i1]>lst2[i2]:
            lst3[i3]=lst1[i1]
            i1=i1+1
    else:
        lst2[i3] =lst2[i2]
        i2=i2+1
    i3=i3+1

    while i1<n1:
        lst3[i3]=lst1[i1]
        i1=i1+1
        i3=i3+1
    while i2<n2:
        lst3[i3]=lst2[i2]
        i2=i2+1
        i3=i3+1
    L=i1+i2+i3

    


        
def main ():
    again='y'
    while again.lower()=='y':
        lst=create()
        search_or_sort=input("Enter search or sort")
        while search_or_sort not in ('search','sort'):
          search_or_sort=input("please enter a valid answer; search or sort")
        if search_or_sort=='search':
          selectionsearch(lst)
        else:
          selectionsort(lst)
main()

