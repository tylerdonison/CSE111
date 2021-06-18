def main():
    start = int(input("What is your starting odometer value in miles? "))
    end = int(input("What is your ending odometer value in miles? "))
    gallons = float(input("How many gallons of fuel did you use? "))
    mpg = mpg_calculator(end, start, gallons)
    lp100k = lp100k_convertor(mpg)

    mpg = round(mpg, 1)
    lp100k = round(lp100k, 2)

    print(f"Your mpg is {mpg}, and your lp100k is {lp100k}.")

def mpg_calculator(end, start, gallons):
    return (end-start)/gallons

def lp100k_convertor(mpg):
    return 235.215/mpg

main()