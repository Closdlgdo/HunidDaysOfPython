student_dict = {
    "student": ["Mike", "Kobe", "James"],
    "score": [56, 96, 68]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
