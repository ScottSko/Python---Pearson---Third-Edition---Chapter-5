def main():
    num1 = int(input("Please enter a value: "))
    num2 = int(input("Please enter another value: "))
    greater_value = maximum(num1, num2)
    print("The greater value is", greater_value)

def maximum(num1,num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        print("The values are equal.")
    else:
        return num2
main()