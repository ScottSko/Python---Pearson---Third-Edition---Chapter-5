def main():
    square_feet = int(input("How many square feet are you painting? "))
    paint = int(input("How much does the pain cost? "))
    charge(square_feet, paint)

def charge(num1, num2):
    gallons = (num1 / 112)
    paint_cost = gallons * num2
    labor_hours = gallons * 8
    labor_price = labor_hours * 35
    total_cost = paint_cost + labor_price

    print("The total number of gallons required is", gallons)
    print("The total hours of labor will be", labor_hours)
    print("The total cost of the paint will be", paint_cost)
    print("The total cost of labor will be", labor_price)
    print("The entire paint job will cost", total_cost)

main()