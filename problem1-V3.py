# usimg get_valid_float 
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value 
        except ValueError:
            print("Invalid input. Please enter a valid numerical value only.")
    # data gathering 
gross_income = get_valid_float("Enter Gross Income: ")
income_tax = get_valid_float("Enter Income Tax: ")
sss_contribution = get_valid_float("Enter SSS contribution: ")
medical_insurrance = get_valid_float("Enter Medical Insurance: ")
    # calculations
net_income = gross_income - (income_tax + sss_contribution + medical_insurrance)
    # printing stage 
print("\nNet Income: {:.2f}".format(net_income))