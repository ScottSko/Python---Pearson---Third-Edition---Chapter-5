import random

print(""" "What is your name's name?" """)
name = input("")

def show_double(string):
    number = random.randint(1, 5)

    #Alternatively, you can write:
    # number = random.randrange(1, 5)


    if number == 1:
        result = name + ", the Definer of Functions"
    elif number == 2:
        result = name + ", the Conqueror of Python"
    elif number == 3:
        result = name + ", the Master of CS"
    elif number == 4:
        result = name + ", the Guru of Processing"
    print(format(number, ",.2f"))
    print("You will henceforth be known as", result)
show_double(name)

#print (random.randrange(0, 10))