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
# Create a program to print current time.
#==============================================================================

#Now we play with the imports

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
