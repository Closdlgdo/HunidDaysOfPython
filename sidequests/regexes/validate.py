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

# This program is buggy because we set a very low bar. we only look for the @ so we can only input the @ and nothing else
# and the code would still call it as valid.
# This doesn't fix the code because we only look for the @ and a dot and nothing else.

# Now we are creating the code more valid but it is still buggy. Mainly because we can give a sketchy
# email address like "hello@.edu" and the code will still call it valid.

#####################################################################################
# In python there is a library called re that can help us with regular expressions.
# re.search(pattern, string, flags=0)
# Pattern: is what we want to search for in the string that came from the user.
# string: is the string that we want to search.
# flags: is a flag that we can use to control the search.

import re

email = input("Email: ").strip()

if re.search("@", email):
    print("Valid email!")
else:
    print("Invalid email!")

# This program is buggy because we set a very low bar. we only look for the @ so we can only input the @ and nothing else
# and the code would still call it as valid.
