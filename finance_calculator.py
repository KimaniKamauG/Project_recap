monthly_income = int( input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your monthly expenses: '))
annual_interest = 0.05
monthly_savings = monthly_income - monthly_expenses
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * annual_interest))
print(f'Your monthly savings are ${monthly_savings}.')
print(f'Projected savings after one year, with interest, is: ${projected_savings}.')
