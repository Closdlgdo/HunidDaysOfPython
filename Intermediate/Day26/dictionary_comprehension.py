# This is to create a new dictionary.
# new_dict = {new_key:new_value for item in list}

# You can create a new dictionary using the values of an existing dictionary.
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# We can also create a new dictionary with a conditional.
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {
    "Alex": 99,
    "Beth": 89,
    "Caroline": 99,
    "Dave": 78,
    "Eleanor": 99,
    "Freddie": 89
}
passed_students = {name: score for (name, score) in student_scores.items() if score > 90}
print(passed_students)
