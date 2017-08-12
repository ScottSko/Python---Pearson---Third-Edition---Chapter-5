def main():
    total_sales = float(input("What are the total sales for the month? "))
    total_county, total_state = calculate_tax(total_sales)
    total_tax = total_county + total_state
    print("The total county tax is", total_county)
    print("The total sales tax is", total_state)
    print("The total county and sales tax is", total_tax)

def calculate_tax(num1):
    county_tax = num1 * .05
    state_tax = num1 * .025

    return county_tax, state_tax

main()