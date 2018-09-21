'''("Authors: Freese, Stockla, DePeza")
 ("CS 201, 9/8/2014")
 ("Lab2, Question #4, Time conversions")'''

hours = int(input("Enter number of hours"))
min = int(input("Enter number of minutes"))
sec = int(input("Enter number of seconds"))

print(hours, "hours",min,"minutes and",sec,"seconds correspond to", hours*3600+min*60+sec,"seconds")
