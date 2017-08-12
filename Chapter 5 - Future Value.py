def main():
    present_value = int(input("What is the account's present value? "))
    monthly_interest_rate = int(input("What is the monthly interest rate? ")) * .01
    number_of_months = int(input("How many months will the money be left in the account? "))

    value_over_time = future_value(present_value, monthly_interest_rate, number_of_months)

    print("The future value of your account is", value_over_time)

def future_value(present_value, monthly_interest_rate, number_of_months):
    equation_part_1 = 1 + monthly_interest_rate
    equation_part_2 = equation_part_1 ** number_of_months
    equation_part_3 = present_value * equation_part_2
    return equation_part_3
main()