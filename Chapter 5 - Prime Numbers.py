def main():
    possible_prime = int(input("Please enter a number: "))
    prime_or_not = is_prime(possible_prime)
    if prime_or_not == True:
            print("The number is prime.")
    else:
            print("The number is not prime.")

def is_prime(possible_prime):
    if possible_prime == 2 or possible_prime == 3 or possible_prime == 5 or possible_prime == 7:
        return True
    elif possible_prime % 2 == 0 or possible_prime % 5 == 0 or possible_prime % 3 == 0 or possible_prime % 7 == 0 \
        or possible_prime % 9 == 0:
        return False
    else:
        return True

main()
