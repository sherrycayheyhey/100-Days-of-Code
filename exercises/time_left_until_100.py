
age = input("What is your current age? ")

# 110 is the life expectancy, years_left will be how many more years you're expected to live
years_left = 100 - int(age)
months = years_left * 12
weeks = years_left * 52
days = years_left * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left until you turn 100.")
