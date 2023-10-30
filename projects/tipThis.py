#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

#to get the percentage of a tip, you have to divide the percentage by 100.
print("This is the tip calculator")
# input: What was the total bill?
bill_total = float(input("What was the total of your bill? "))
# input: What percentage tip would you like to give? 10, 12, 15, 20?
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15, 20? "))
# input: How many people will split the bill?
people_amount = int(input("How many people will split the bill? "))
# total: Your bill comes out to: ()/ per person.
tip_as_percent = tip_percentage / 100
total_tip_amount = bill_total * tip_as_percent
total = bill_total + total_tip_amount
total_for_each_person = total / people_amount

round_total_tip_amount = round(total_tip_amount, 2)
round_total = round(total, 2)
round_total_for_each_person = round(total_for_each_person, 2)

print(f"The total tip quantity is: ${round_total_tip_amount}")
print(f"The final amount with tip is: ${round_total}")
print(f"Each person will have to pay: ${round_total_for_each_person}")