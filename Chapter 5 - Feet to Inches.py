def main():
    feet = int(input("How many feet are there?"))
    inches = feet_converter(feet)
    if feet == 1:
        print("In", feet, "foot, there are", inches, "inches.")
    else:
        print("In", feet, "feet, there are", inches, "inches.")

def feet_converter(num1):
    return num1 * 12

main()