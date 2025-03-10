# with conditions 
def get_float_input(prompt):
    """Function to get a valid float input"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter numerical value only.")

            
    # data gathering 
gross_income = float(input("Enter Gross Income: "))
income_tax = float(input("Enter Income Tax: "))
sss_contribution = float(input("Enter SSS contribution: "))
medical_insurance = float(input("Enter Medical Insurance: "))

    # formula 
net_income = gross_income - (income_tax + sss_contribution + medical_insurance)

    #printing stage 
print("\nNet Income: {:.2f}".format(net_income))