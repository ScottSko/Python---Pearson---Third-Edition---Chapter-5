model = int(input("Enter the model number: "))

def is_invalid(mod_num):
    if mod_num != 100 and mod_num != 200 and mod_num != 300:
        status = True
    else:
        status = False
    return status

# the next block of code executes only if is_invalid is true.
# it takes the model as an argument, but will not run unless the function returns true.

while is_invalid(model):
    print("The valid model numbers are 100, 200, and 300. ")
    model = int(input("Enter a valid model number: "))
