def main():
    input_mass = int(input("What is the object's mass in kilograms? "))
    input_velocity = int(input("What is the object's velocity "))

    print("The object's kinetic energy is: ", kinetic_energy(input_mass, input_velocity))

def kinetic_energy(mass, velocity):
    return (mass * (velocity**2)) * .5

main()