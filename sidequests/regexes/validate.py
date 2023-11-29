# # Regex is a regular expression that matches a string against a pattern.
#
# email = input("Email: ").strip()
#
# username, domain = email.split("@")
#
# if username and domain.endswith(".edu"):
#     print("Valid email!")
# else:
#     print("Invalid email!")
#
#
# This program is buggy because we set a very low bar. we only look for the @ so we can only input the @ and nothing else
# and the code would still call it as valid.
# This doesn't fix the code because we only look for the @ and a dot and nothing else.
#
# Now we are creating the code more valid but it is still buggy. Mainly because we can give a sketchy
# email address like "hello@.edu" and the code will still call it valid.
#
# ####################################################################################
# In python there is a library called re that can help us with regular expressions.
# re.search(pattern, string, flags=0)
# Pattern: is what we want to search for in the string that came from the user.
# string: is the string that we want to search.
# flags: is a flag that we can use to control the search.
#
# import re
#
# email = input("Email: ").strip()
#
# if re.search(".+@.+", email):
#     print("Valid email!")
# else:
#     print("Invalid email!")
#
# # This program is buggy because we set a very low bar. we only look for the @ so we can only input the @ and nothing else
# # and the code would still call it as valid. Now we are creating the code more valid but it is still buggy. Mainly because we can give a sketchy
# # email address like "hello@.edu" and the code will still call it valid.
#
# ####################################################################################
# ####################################################################################
#
# import re
#
# email = input("Email: ").strip()
#
# if re.search(".*@.*", email):  # zero or more characters followed by an @ sign followed by zero or more characters.
#     print("Valid email!")
# else:
#     print("Invalid email!")
#
# # how is re.search going to keep track of whether or not the users input matches the patterns?
# # it uses a machine of sorts called a finite state machine to keep track of the pattern.
# # A non-deterministic finite automaton.
#
# ####################################################################################
# ####################################################################################

import re

email = input("Email: ").strip()

if re.search(r".+@.+\.edu", email):  # the r at the beginning of the string means that the string is a raw string.
    # we can also use r"..." to tell python not to interpret the backslash as a escape character.
    print("Valid email!")
else:
    print("Invalid email!")

# This code is better but still buggy because we have not set a standard for the @.
# we can input many "@" characters and still call it valid. Ex: "hello@@@@@@.edu"
