import math

def main():
    a = float(input("Enter the length of Side A: "))
    b = float(input("Enter the length of Side B: "))

    c = math.hypot(a, b)

    print("The length of the hypotenuse is", c)

main()