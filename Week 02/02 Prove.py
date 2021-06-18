import math
from datetime import datetime
import random #my strech will always have a random element

#Prove from last week
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000

print(f"The approximate volume is {volume:.1f} cubic cm.")

#Prove this week
current_date = datetime.now().date()

with open("volumes.txt", "at") as volume_file:
    print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.1f}", file=volume_file)

#This week's exceeding requirements

print("Your tire dimensions have been saved!")
print(f"{width}/{aspect_ratio}R{diameter}")
buy_tires = input("Would you like to order tires with these dimensions? (y/n) ")
buy_tires = buy_tires.lower()

if buy_tires == "y": #if they desire to order tires
    tire_number = input("How many tires would you like to order? ")
    print("We will have one of our operators contact you, but first, we need your name and phone number.")
    checker = "n" #while loop's condition if the customer's details are incorrect.
    while checker == "n":
        last_name = input("Please insert your last name: ")
        last_name = last_name.capitalize()
        first_name = input("Please insert your first name: ")
        first_name = first_name.capitalize()
        phone_number = input("Please insert your phone number in this format: ###-###-####: ")
        checker = input(f"Is {last_name}, {first_name}, {phone_number} correct? (y/n) ")
        checker = checker.lower()
    #Save info to text file
    with open("volumes.txt", "at") as volume_file:
        print(f"{last_name}, {first_name}, {phone_number}, {tire_number} tires.", file=volume_file)
    
    #random factor
    first_rng = random.randint(1,4)
    second_rng = random.randint(1,4)

    #random operator first name
    if  first_rng == 1:
        rnd_first_name = "Taylor"
    elif first_rng == 2:
        rnd_first_name = "Kalina"
    elif first_rng == 3:
        rnd_first_name = "Nathan"
    else:
        rnd_first_name = "Ben"

    #random operator last name
    if  second_rng == 1:
        rnd_last_name = "Dara"
    elif second_rng == 2:
        rnd_last_name = "Warner"
    elif second_rng == 3:
        rnd_last_name = "Birch"
    else:
        rnd_last_name = "Ellis"

    print(f"Thank you for shopping with us. Your information has been saved and our operator, {rnd_first_name} {rnd_last_name} will call you shortly.")
else:
    with open("volumes.txt", "at") as volume_file:
        print("The user did not desire to purchase tires.", file=volume_file)
    print("Thanking for shopping with us. Please have a good day.")