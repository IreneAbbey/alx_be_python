# User Input for Financial Details:
monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your monthly expense: "))


# Calculate Monthly Savings:
monthly_savings = monthly_income - monthly_expense
print(f"Your monthly savings are ${monthly_savings}")

# Project Annual Savings:
project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${project_savings}")