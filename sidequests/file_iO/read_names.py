# # This particular file with read the names from names.txt.
# with open("names.txt", 'r') as file:
#     for line in file:
#         print(line.rstrip())  # this shortens the code below and makes it cleaner.
# #     lines = file.readlines()  # readlines is a special method that returns all the lines from the file as a list.
# #
# # for line in lines:  # we want to iterate over the list of lines to print out each name.
# #     print(line.rstrip())

################################################################
# # We want to print the names from names.txt in a sorted order. To do this, we can use the sorted() function.
# names = []  # we create an empty list
#
# with open("names.txt") as file:  # we do not need to specify 'r' for read.
#     for line in file:
#         names.append(line.rstrip())  # we append the names to the list
#
# for name in sorted(names):
#     print(f"Hello, {name}!")

################################################################
# We can simplify the above code even more with the sorting of the names by doing:
with open("names.txt") as file:  # we do not need to specify 'r' for read.
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}!")
