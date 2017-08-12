import random

def main():
    correct_guess = False
    number_of_guesses = 0
    num1 = random.randint(1, 100)
    while correct_guess == False:
        guess = int(input("Guess the random number!"))
        number_of_guesses += 1
        if guess > num1:
            print("Too high, try again.")
        elif guess < num1:
            print("Too low, try again.")
        elif guess == num1:
            print("Congratulations! You got the correct answer in", number_of_guesses, "guesses.")
            yes_no = input("Press Enter to play again.")
            correct_guess == True



main()
