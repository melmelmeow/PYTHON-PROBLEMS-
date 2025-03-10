# original template with out conditions 
gross_income = float(input("Enter gross income: "))
income_tax = float(input("Enter income tax: "))
sss_contribution = float(input("Enter SSS contribution: "))
medical_insurance = float(input("Enter medical insurance: "))

# formula
net_income = gross_income - (income_tax + sss_contribution + medical_insurance)

# printing stage
print("\nNet Income: {:.2f}".format(net_income))
