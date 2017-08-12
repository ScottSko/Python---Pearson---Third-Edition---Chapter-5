def main():
    a_class = int(input("How many Class A seats were sold? "))
    b_class = int(input("How many Class B seats were sold? "))
    c_class = int(input("How many Class c seats were sold? "))

    a_total, b_total, c_total = seat_revenue(a=a_class, b=b_class, c=c_class)

    total = a_total + b_total + c_total

    print("The total amount of revenue generated for Class A seats is $", a_total, sep='')
    print("The total amount of revenue generated for Class B seats is $", b_total, sep='')
    print("The total amount of revenue generated for Class C seats is $", c_total, sep='')
    print("The total amount of revenue generated for each seat class is $", total, sep='')

def seat_revenue(a, b, c):
    a_revenue = a * 20
    b_revenue = b * 15
    c_revenue = c * 10

    return a_revenue, b_revenue, c_revenue

main()