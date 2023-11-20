# family = ["carlos", "theano", "lucas"]
#
# family.append("matias")
#
# family.extend(["Ra", "Churro", "Betty"])
#
# print(family)
import random

# 1 ask for user input of names
names_string = input("Give me everybody's names, separated by a comma. ")
# 2 once input is entered, it turns into a list
# 3 once list is printed, use .split(", ") to remove the comma and space from list. this
# will give you a regular list of names.
names = names_string.split(", ")
# 4 print names
print(names)
# 5 pick a random name based off of the index of the name.
random_choice = random.choice(names)
# 6 create output of random name with " is going to buy the meal today!"
print(f"{random_choice} is going to buy the meal today!")
