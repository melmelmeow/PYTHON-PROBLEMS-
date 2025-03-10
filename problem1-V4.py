while True:
    try: 
        gross_income = float(input("Enter Gross Income: "))
        break 
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try: 
        income_tax = float(input("Enter Income Tax: "))
        break 
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        sss_contribution = float(input("Enter SSS contribution: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try: 
        medical_insurance = float(input("Enter Medical Insurance: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

net_income = gross_income - (income_tax + sss_contribution + medical_insurance)

print("\nNet Income: {:.2f}".format(net_income))