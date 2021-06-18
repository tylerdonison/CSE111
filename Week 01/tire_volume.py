import math
import random #this is how I will always make my programs unique.

"""Size of a car tire is represented with three numbers, aaa/bbRcc
a is width 
b os aspect ration
c diameter in inches
"""

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000

print(f"The approximate volume is {volume:.1f} cubic cm.")
input("Push enter to continue. ")

randomization = random.randint(1,5)
if randomization == 1:
    wheels = 2
    vehicle = "a motorcycle"
elif randomization == 2:
    wheels = 3
    vehicle = "a 3-wheel vehicle"
elif randomization == 3:
    wheels = 4
    vehicle = "a typical 4-wheel vehicle"
elif randomization == 4:
    wheels = 6
    vehicle = "a dual rear wheel truck"
else: #if randomization == 5:
    wheels = 18
    vehicle = "a semi-truck"
new_volume = volume * wheels
print(f"With the calculated volume, we have detected that your vehicle is {vehicle}.")
print(f"The volume of your tires combined is {new_volume:.1f} cubic cm.")
input("Thank you for using Doni's tire calculation program. ")