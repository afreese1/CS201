'''("Authors: Freese, Stockla, DePeza")
 ("CS 201, 9/8/2014")
 ("Lab2, Question #2, Temperature conversion")
 
 converts fahrenheit to celsius and kelvin
 '''

fah = int(input("Enter the temperature in Fahrenheit"))
cel = (fah-32)*(9/5)
kel = cel+273

print("This converts to" , cel , "degrees celsius and", kel, "degrees kelvin")
          

