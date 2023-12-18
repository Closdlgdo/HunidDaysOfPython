# This is to create a new dictionary.
# new_dict = {new_key:new_value for item in list}

# You can create a new dictionary using the values of an existing dictionary.
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# We can also create a new dictionary with a conditional.
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)
