#==============================================================================
#
#Created by: Alan Patricio González Bernal
#Date: 2023-06-08
#language: Python
#Code number: 5
#
#==============================================================================

#INSTRUCTIONS

#==============================================================================
# Write a Python program where you use OOP to create a class called "Circle" and
# make two methods to compute the area and perimeter of a circle.
#==============================================================================

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
circle = Circle(int(input("Write the radius of the circle: ")))
print("The area of the circle is: ", circle.area())
print("The perimeter of the circle is: ", circle.perimeter())

