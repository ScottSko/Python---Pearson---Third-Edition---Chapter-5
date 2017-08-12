def main():
    for x in range(1,11):
        distance = falling_distance(x)
        print(distance)
def falling_distance(num1):
    return (9.8 * (num1**2)) * .5

main()