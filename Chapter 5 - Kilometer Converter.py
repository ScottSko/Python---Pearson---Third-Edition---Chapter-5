print("This program converts kilometers to miles.")
print("For your reference, the formula is: ")
print("Miles = Kilometers * 0.6214")

#kilometers = int(input("What is the distance in kilometers? "))

#miles = kilometers * .6214

#print("The distance in miles is:", miles)

#Alternative Version With Functions

def kilometers_converter(number):
    return number * .6214

kilometers = float(input("What is the distance in kilometers? "))

print("The distance in miles is:", kilometers_converter(kilometers))