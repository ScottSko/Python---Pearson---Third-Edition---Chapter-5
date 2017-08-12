import random
import math

def main():
    num1 = random.randint(0, 1000)
    num2 = random.randint(0, 1000)

    print("This program asks you to add two numbers together.")
    print(" ", num1)
    print("+", num2)
    answer = int(input("What is your answer? "))
    calculate(answer, num1, num2)

def calculate(num0, num1, num2):
    if num0 == num1 + num2:
        print("Correct!")
    else:
        print("Incorrect")
        print("The correct answer is", num1 + num2)

main()