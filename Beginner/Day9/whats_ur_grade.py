student_score = {
    "Carlos": 91,
    "Matias": 78,
    "Theano": 99,
    "Lucas": 80,
    "Churro": 62,
}

# We create a new dictionary called ""students_grades"" as an empty dictionary.
students_grades = {}

# We create a for loop to iterate over the ""student_score"" dictionary.
for student, score in student_score.items():
    if score >= 90:
        students_grades[student] = "Outstanding"
    elif score >= 80:
        students_grades[student] = "Exceeds Expectations"
    elif score >= 70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"

print(students_grades)
