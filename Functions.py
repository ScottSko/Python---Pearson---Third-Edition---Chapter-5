import random

print("What is your name? ")
name = input("")

def show_double(string):
    number = random.randrange(1, 5)
    if number == 1:
        result = name + ", the Definer of Functions"
    elif number == 2:
        result = name + ", the Conquerer of Python"
    elif number == 3:
        result = name + ", the Master of CS"
    elif number == 4:
        result = name + ", the Guru of Processing"
    print(number)
    print("You will henceforth be known as", result)
show_double(name)

#print (random.randrange(0, 10))