#==============================================================================
#
#Created by: Alan Patricio González Bernal
#Date: 2023-06-08
#language: Python
#Code number: 2
#
#==============================================================================

#INSTRUCTIONS

#==============================================================================
# Create a simple calculator that asks the user for two numbers and an operator
# (+, -, *, /). Then calculate the result and print it out to the user.
#==============================================================================

#We define the variables
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /): ")

print("The result of your selection is: ")

#Method of operation
if operator == "+":
    print(n1 + n2)
elif operator == "-":
    print(n1 - n2)
elif operator == "*":
    print(n1 * n2)
elif operator == "/":
    print(n1 / n2)
    
