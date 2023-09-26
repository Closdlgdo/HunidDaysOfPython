age = input("What is your current age? ")

days_left = 90 - int(age)
days_in_a_year = days_left * 365
weeks_in_a_year = days_left * 52
months_in_a_year = days_left * 12

print(f"You have {days_in_a_year} days, {weeks_in_a_year} weeks, and {months_in_a_year} months left.")
