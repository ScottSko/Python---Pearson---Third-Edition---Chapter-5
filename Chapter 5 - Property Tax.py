def main():
    actual_value = int(input("How much is the property valued at? "))
    assessment_value = actual_value * .6
    property_tax_value = property_tax(assessment_value)
    print("The actual value is ", actual_value, "and the assessment value is", assessment_value)
    print("The property tax is", property_tax_value)

def property_tax(num):
    value = (num/100) * .72
    value = (format(value, '.2f'))
    return value

main()