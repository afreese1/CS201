'''("Authors: Freese, Stockla, DePeza")
 ("CS 201, 9/8/2014")
 ("Lab2, Question #3, conversion")
 
 Converts gallons quarts, pints and cups
 can be updated to include ounces or to work the other way cups->gal
 '''

gal = int(input("Enter number of gallons"))
quart = gal*4
pints = quart*2
cups = pints*2

print(gal,"gallons is equal to",quart,"quarts,", pints, "pints, and",cups, "cups")
