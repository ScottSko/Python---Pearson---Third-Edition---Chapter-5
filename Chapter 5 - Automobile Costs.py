def main():
    print("For the following prompts, please enter the monthly amount for each parameter.")
    loan_payment = int(input("How much is the loan payment? "))
    insurance = int(input("How much is the insurance? "))
    gas = int(input("How much do you spend on gas? "))
    oil = int(input("How much do you spend on oil? "))
    tires = int(input("How much do you spend on tires? "))
    maintenance = int(input("How much is maintenance? "))

    m_total, y_total = calculate_total(loan_payment, insurance, gas, oil, tires, maintenance)

    print("The total cost per month is $", m_total, " and the total cost per year is $", y_total, sep='')

def calculate_total(num1, num2, num3, num4, num5, num6):
    monthly_total = (num1 + num2 + num3 + num4 + num5 + num6)
    yearly_total = (num1 + num2 + num3 + num4 + num5 + num6) * 12

    return monthly_total, yearly_total

main()