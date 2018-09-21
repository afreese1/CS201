'''
Alyssa Freese
CS201
November 17, 2014
Programming Assignment 2

Algorithm:

Main

1. ask for student number and validate that it is not 0
2. ask for number of courses taken
3. create loop to ask for each course the name, number of credit hours and letter grade
4. validate that the entered credit hours is positive
5. find credit taken by adding credit for each course
6. find credit attained by adding credit from passed courses only
7. calculate the total quality points by finding the sum of the numeric grade times the credit for each course
8. gpa is calculated by dividing the total quality points by the credits taken
9. print the student number, credits attained, credits taken and gpa

Convert Letter Grade

1. carry over the input value for the grade
2. validate that the entered letter grade is valid, if not ask again
3. create if statements for each condition (grade)
4. each grade should be converted to a float
5. return the new value for the grade

Test Cases:

1) number of courses = 2
   Course 1 => credit = 3, grade = B+
   Course 2 => credit = 4, grade = A

   credit taken = sum of credit = 3+4 = 7
   credits attained = sum of credits, not including classes with an F = 3+4 = 7
   total quality points = sum of credit*numeric grade = (3*3.5)+(4*4) = 10.5+16 = 26.5           
   gpa = total quality points/credits taken = 26.5/7 = 3.786

   works as expected

2) number of courses = 3
   Course 1 => credit = 2, grade = A
   Course 2 => credit = 3, grade = F
   Course 3 => credit = 4, grade = D

   credit taken = sum of credit = 2+3+4 = 9
   credits attained = sum of credits, not including classes with an F = 2+4=6
   total quality points = sum of credit*numeric grade = (2*4)+(3*0)+(4*1) = 8+0+4 = 12
   gpa = total quality points/credits taken = 12/9 = 1.333

   works as expected

3) number of courses = 4
   Course 1 => credit = 3, grade = B
   Course 2 => credit = 4, grade = A
   Course 3 => credit = 4, grade = F
   Course 4 => credit = 3, grade = C

   credit taken = sum of credit = 3+4+4+3 = 14
   credits attained = sum of credits, not including classes with an F = 3+4+3 = 10
   total quality points = sume of credit*numerica grade = (3*3)+(4*4)+(4*0)+(3*2) = 9+16+0+6 = 31
   gpa = total quality points/credits taken = 31/14 = 2.214

   works as expected
   
'''

def main():

    student_number=int(input("Enter student number: "))
    print()

    #if student number is 0, program ends
    if student_number!=0:
        n=int(input("Enter number of courses taken: "))
        print()

        cred_attained=0
        cred_taken=0
        quality_pts=0
        
        for i in range(n):
            name=input("Enter course name: ")
            credit=int(input("Enter number of credit hours: "))
            #validate that credit is positive
            while credit<0:
                credit=int(input("Enter number of credit hours (must be positive): "))
            grade=input("Enter letter grade received in course: ")
            print()
            #call on convert_letter_grade function and carry value of grade
            grade=convert_letter_grade(grade)
            #calculate total quality points by finding sum of the amount of
            #credit multiplied by the numeric grade for each course
            quality_pts=quality_pts+(credit*grade)
            cred_taken=cred_taken+credit
            #if numeric grade equals 0, credit is not received
            if grade!=0:
                cred_attained=cred_attained+credit
            else:
                cred_attained=cred_attained

        #calculate gpa
        gpa=quality_pts/cred_taken
        
        print("Student",student_number,":")
        print()
        print("Attained a total of",cred_attained,"credit")
        print("out of a possible",cred_taken,"credits taken.")
        print("GPA:",format(gpa,'.3f'))
            
def convert_letter_grade(g):

    #validate that the letter grade is valid
    while g!='A'and g!='B+'and g!= 'B'and g!='C+'and g!='C'and g!='D'and g!='F':
        g=input("Enter a valid grade: ")
        print()

    #create if statements to determine what each grade is numerically equivalent to
    if g=='A':
        grade=float(4.0)
    elif g=='B+':
        grade=float(3.5)
    elif g=='B':
        grade=float(3.0)
    elif g=='C+':
        grade=float(2.5)
    elif g=='C':
        grade=float(2.0)
    elif g=='D':
        grade=float(1.0)
    else:
        grade=float(0.0)

    #reurn the new value for grade
    return grade
        
#call on the main function
main()
