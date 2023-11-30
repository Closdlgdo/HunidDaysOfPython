# # rather than just validate the users input, lets assume the user is not going to type in data the way we want and so
# # we will have to clean up their input.
# # lets create some code that can help clean up the users input as well as older data from previous users if needed.
# # This will be able to standardize the input to be saved in a database to make it easier to read.
#
# name = input("Name: ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
#
# print(f"Hello, {name}!")
#
# # This code will swap the users input if name and last name were swapped. It will swap to be properly formatted.
# # Example: "Name: last, first" will be "Hello, first last"
# # This code however does have some bugs that need fixing. For example: "Name: last,first" will be last, first = name.split(", ")
# # ValueError: not enough values to unpack (expected 2, got 1)

################################################################################################
################################################################################################
import re

name = input("Name: ").strip()
matches = re.search(r"^(.+), (.+)$", name)  # we deliberately capture the dot plus for capturing purposes

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"Hello, {name}!")

# When we used re.search(), we used it to answer a question: "Does the users input mathe the following pattern?"
# you can also assign the re.search() to a variable to get a more precise answer to what has been found when searched for.
# the "A|B" is a special character that means match either A or B.
# the "(...)" is a special character that means match the expression inside the parentheses.
# the "(?:...)" is a special character that means match the expression inside the parentheses but do not capture the match.
