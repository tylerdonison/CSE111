"""

x = 5
y = 6
print(x < y)

FavoriteNumbersList= [3, 4, 5, 6, 7, 8]
# in and not in are membership operators, can use in lists

if (4 not in FavoriteNumbersList) :
    print("This is true.")

x < y and y < 3
#this becomes false because on of them is false.
#if the "and" is or, because on side is true, both or true.
x < y not(y < 20)

name = "Joey"
if "J" in name:
    print("J was in the name")
    #capitalization matters in this case, if "j" is different than if "J".

x = x+1 
x += 1
#these two are the same. You can also change the + to other operators.
#these operators include +, -, /, *, **, //, %.
# // divides but rounds down. / gives float, // gives int
# % gives remainder, 5 % 1 gives 1.

x = 10
for i in range(0, x):
    print(i)
"""
#functions
#def functionname(variable, variable2):
#    print(variable, variable2)

import math

def ComputeCircumference(radius):
    return 2 * radius * math.pi
  
User_radius = float(input("Please enter a radius to find a circumference: "))

x = ComputeCircumference(User_radius)
print (x)