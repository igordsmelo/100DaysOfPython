###
age = input("What is your current age?")
###

###
age = int(age)
years_left = 90 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")
