#Scope, local or global variables.
#local is defined inside a function.
#global is defined outside a function.

x = 1
def function1():
    y = 1

#x is a global, y is a local

#functions are new, this might mean that Dad's code doesn't have these.

nShapes = 0

def square_area(length):
    area = length**2
    return area

def rectangle_area(width, length):
    area = length * width
    return area

#import math #Python was downloaded with this library and more, math is one of them.
from math import pi
#import math as m

def main():
    radius = float(input("Enter the radius: "))
    area = circle_area(radius)
    print(area)

def circle_area(radius):
    area = pi *radius *radius
    return area

main()
print(pi)
