# This particular file with read the names from names.txt.
with open("names.txt", 'r') as file:
    lines = file.readlines()  # readlines is a special method that returns all the lines from the file as a list.

for line in lines:  # we want to iterate over the list of lines to print out each name.
    print(line.rstrip())
