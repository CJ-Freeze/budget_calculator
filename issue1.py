print("Let's budget for your dreams!\n")
Income_goal = input("How much is your financial goal?")
Number_of_year = input("\nGreat! You want to meet this financial goal in how many years? (must enter atleast 1)")
Current_income = input("\nOk, What is your current hourly wage? *do not enter a $*")
Number_of_hours = input("\nHow many hours a week do you work?")
tax_rate = input("\nWhat percent do you pay in taxes? Enter as a decimal!")
expenses = input("\nWhat are your total yearly expenses?")
Weekly_income =float(Current_income)*float(Number_of_hours)
Yearly_income = float(Weekly_income)*52
Yearly_income_after_taxes= float(Yearly_income)-float(Yearly_income)*float(tax_rate)
Yearly_income_after_taxes_and_expenses = float(Yearly_income_after_taxes)-float(expenses)
Money_needed = float(Income_goal)/float(Number_of_year)
The_difference = float(Money_needed)-float(Yearly_income_after_taxes_and_expenses)
print("\nThats all the info a need! Beep Boop\n")
print(f"You will need to make {The_difference} more each year to reach your goal!")


