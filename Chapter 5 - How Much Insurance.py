def main():
    cost = int(input("How much would it cost to replace the structure? "))
    windfall = insurance(cost)
    print("The amount you should spend to insure your structure is", windfall)


def insurance(number):
    return number * .8

main()