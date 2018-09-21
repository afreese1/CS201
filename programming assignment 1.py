'''
Alyssa Freese
CS201
October 20, 2014

Programming Assignment #1

Test Cases:

Pay Code 10

    1) rate=$100/week, worked total of 52 hours for the week
            worked over 50 hours, receive a 5% increase in weekly rate
            pay=rate*.5=100*.05=105, contribution=pay*.04=105*.04=4.2,
            total pay=pay-contribution=105-4.2=100.8
            expected outcome=$100.80

            works as expected
            
    2) rate=$50/week, worked total of 40 hours for the week
            didnt work over 50 hours=> pay=$50, contribution=pay*.04=50*.04=$2
            total pay=pay-contribution=50-2=48
            expected outcome=$48.00

            works as expected

Pay Code 20

    1) rate=$2/hour, worked total of 50 hours for the week
            pay=rate*hours=2*50=100, excess hours=50-48=2,
            overtime pay = 2hours*$2*1.5=$6
            total pay=pay+overtime pay-$25=100+6-25=81
            expected outcome=$81.00

            Works as expected
      
    2)rate=$5/hour, worked total of 20 hours for the week
         pay=rate*hours=5*20=$100, no excess hours, total pay=pay-$25=100-25=75
         expected outcome=$75.00

         Works as expected

Pay Code 30

    1) rate=$10/hour, worked total of 25 hours for the week
            pay=hours*rate=25*10=250, didn't earn more than $250 in a week
            expected outcome=$250

            works as expected
            
    2) rate=$10/hour, worked total of 30 hours for the week
            pay=hours*rate=30*10=300, earned more than $250 in a week
            must contribute 10% of pay for health insurance
            contribute=pay*.1=300*.1=30, total pay=pay-contribute=300-30=270
            expected outcome=$270.00

            works as expected

'''

#defines the main function
def main():
    #calls the intro function
    intro()
    cont='yes'
    #creates a loop so that the user can calculate another employees payroll
    while cont=='yes':
        #asks user for their pay code
        code=int(input("Enter your Pay Code: "))
        #creates loop to validate pay code number
        while code!=10 and code!=20 and code!=30:
            code=int(input("Invalid. Please enter your Pay Code again: "))
        correct=input("Is this pay code correct? yes or no: ")
        #creates loop to ask user if the entered pay code is correct
        while correct=='no':
            code=int(input("Enter correct pay code: "))
            if code!=10 and code!= 20 and code!= 30:
                code=int(input("Invalid. Please enter your Pay Code again: "))
            correct=input("Is this pay code correct? yes or no: ")
        print()
        #asks user for their pay rate
        rate=float(input("Enter your pay rate: "))
        print()
        if code==10:
            #calls the function for pay code 10
            pay_code_10(rate)
        elif code==20:
            #calls the function for pay code 20
            pay_code_20(rate)
        else:
            #calls the function for pay code 30
            pay_code_30(rate)
        #asks the user if he/se wants to calculate another employees payroll
        cont=input("Does another employee need to be processed? yes or no: ")
        print()

#finds payroll for employee under the conditions of pay code 10
def pay_code_10(rate):
    total=0
    #creates loop to ask user for hours worked each day
    for i in range(1,6):
        print("Enter hours worked on day",i, end=": ")
        hours=int(input())
        #calculates total number of hours worked for the week
        total=total+hours
    #determines the amount that is paid based on the pay rate for the hours
    if total>50:
        pay=rate*.05+rate
    else:
        pay=rate
    #finds how much of their pay is contributed towards a pension fund    
    contribute=pay*.04
    #subtracts the contribution from the pay to find the total pay
    total_pay=pay-contribute
    #prints the total pay
    print("Your total pay is $",format(total_pay,'.2f'))
    print()

#finds payroll for employee under the conditions of pay code 20    
def pay_code_20(rate):
    total=0
    #creates loop to ask user for hours worked each day
    for i in range(1,7):
        print("Enter hours worked on day",i, end=": ")
        hours=int(input())
        #calculates total number of hours worked for the week
        total=total+hours
    #determines the amount that is earned by multiplying the total hours to
    #the pay rate since they recieve an hourly pay rate
    pay=rate*total
    #determines the amount that is paid based on hours worked
    if total>48:
        #finds amount of hours worked over 48 hours
        excess_hours=total-48
        #determines how much is payed for over time by multiplying the excess time
        #to the hourly rate and multiplying it by 1.5 since time and a half (150%)
        #is received
        excess_pay=excess_hours*rate*1.5
        #pay is now equal to the original pay plus the amount that is earned from
        #over time (excess_pay)
        pay=pay+excess_pay
    else:
        pay=pay
    #calculates the total pay by subtracting the amount employees must pay in
    #union dues from their pay
    total_pay=pay-25
    #prints the toal pay
    print("Your total pay is $",format(total_pay,'.2f'))
    print()

#finds payroll for employee under the conditions of pay code 30
def pay_code_30(rate):
    total=0
    #creates loop to ask user for hours worked each day
    for i in range(1,4):
        print("Enter hours worked on day",i, end=": ")
        hours=int(input())
        #calculates total number of hours worked for the week
        total=total+hours
    #determines the pay rate that is earned by multiplying the total hours to
    #the pay rate since they recieve an hourly pay rate
    pay=rate*total
    #determines if the employee has to pay a 10% contribution for health insurance
    if pay>250:
        contribute=pay*.1
        #subtracts the contrubution from the pay to find total pay
        total_pay=pay-contribute
    else:
        #there is no contribution so pay equals the total pay
        total_pay=pay
    #prints the total pay
    print("Your total pay is $",format(total_pay,'.2f'))
    print()
    
#defines what this program does
def intro():
    print("This program will calculate the payroll for an indeterminate number")
    print("of employees of Scott Book Company.")
    print()

#calls the main function
main()
