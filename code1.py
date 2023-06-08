#==============================================================================
#
#Created by: Alan Patricio González Bernal
#Date: 2023-06-08
#language: Python
#Code number: 1
#
#==============================================================================

#INSTRUCTIONS

#==============================================================================
# Create a program that asks the user for a number and then prints out a 
# list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly)
#==============================================================================

#Variable definition
selected = int(input("Enter a number: "))
divisors = []
chosen = selected

#Method
while selected > 0:
    if selected % 2 == 0:
        divisors.append(selected)
    selected -= 1
    
#Final prints
print("The divisors of:")
print(chosen)
print("are:")
print(divisors)