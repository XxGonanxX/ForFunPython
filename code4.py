#==============================================================================
#
#Created by: Alan Patricio González Bernal
#Date: 2023-06-08
#language: Python
#Code number: 3
#
#==============================================================================

#INSTRUCTIONS

#==============================================================================
#  Write a Python program that accepts an integer (n) and computes the value of 
#  n+nn+nnn.
#==============================================================================

a = int(input("Enter a number: "))

n1 = int( "%s" % a )

n2 = int( "%s%s" % (a,a) )

n3 = int( "%s%s%s" % (a,a,a) )

print("Your number is:")
print(n1+n2+n3)
