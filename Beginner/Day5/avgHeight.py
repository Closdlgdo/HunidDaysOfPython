# # For Loops
#
# names = ['Carlos', 'Theano', 'Lucas']
#
# for name in names:
#     print(name)
#     print(name + " Delgado")

# input a python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# calculate the average height
total_height = 0  # have to start with an empty value
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

number_of_students = 0  # have to start with an empty value
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / len(student_heights))
print(f"average height = {average_height}")
