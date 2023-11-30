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
#
# import re
#
# email = input("Email: ").strip()
#
# if re.search(r".+@.+\.edu", email):  # the r at the beginning of the string means that the string is a raw string.
#     # we can also use r"..." to tell python not to interpret the backslash as a escape character.
#     print("Valid email!")
# else:
#     print("Invalid email!")
#
# # This code is better but still buggy because we have not set a standard for the @.
# # we can input many "@" characters and still call it valid. Ex: "hello@@@@@@.edu"

# ####################################################################################
# ####################################################################################

# import re
#
# email = input("Email: ").strip()
#
# if re.search(r".+@.+\.edu", email):  # the r at the beginning of the string means that the string is a raw string.
#     # we can also use r"..." to tell python not to interpret the backslash as a escape character.
#     print("Valid email!")
# else:
#     print("Invalid email!")
#
# # This is also buggy because at input, it allows me to create a sentence that contains my email.
# # Ex: Email: "my email is closdlgdo@gmail.edu.". This will call valid as long as there is something before and after the _@_.edu

# ####################################################################################
# ####################################################################################
# import re
#
# email = input("Email: ").strip()
#
# if re.search(r"^.+@.+\.edu$", email):  # the r at the beginning of the string means that the string is a raw string.
#     # we can also use r"..." to tell python not to interpret the backslash as a escape character.
#     print("Valid email!")
# else:
#     print("Invalid email!")
#
# # "^" is a special character that means start of string. This is the first character that we are looking for.
# # "$" is a special character that means end of string. This is the last character that we are looking for.
#
# # This is also buggy because at input, it allows me to create a sentence that contains my email as long as we do not end
# # email without a period. Ex: "my email is cl@d.edu" is valid.

# ####################################################################################
# ####################################################################################

# import re
#
# email = input("Email: ").strip()
#
# if re.search(r"^[^@]+@[^@]\.edu$",
#              email):  # the r at the beginning of the string means that the string is a raw string.
#     # we can also use r"..." to tell python not to interpret the backslash as a escape character.
#     print("Valid email!")
# else:
#     print("Invalid email!")
#
# # "[]" is a special character that means match any character inside the brackets.
# # "[^]" is a special character that means match any character not inside the brackets.
# # This particular change to the code will not allow the user to input various @ symbols. However,
# # this code will still allow for a sentence before the actual email address.

# ####################################################################################
# ####################################################################################
#
# import re
#
# email = input("Email: ").strip()
#
# if re.search(r"^\w+@\w+\.(com|edu|gov|org|net)$",
#              email, re.IGNORECASE):  # the r at the beginning of the string means that the string is a raw string.
#     # we can also use r"..." to tell python not to interpret the backslash as a escape character.
#     print("Valid email!")
# else:
#     print("Invalid email!")
#
# # the "\w" = [a-zA-Z0-9_], which means that the character is a special character that means match any word character.
# # the "\d" is a special character that means match any digit.
# # the "\D" is a special character that means match any non-digit.
# # the "\s" is a special character that means match any whitespace character.
# # the "\S" is a special character that means match any non-whitespace character.
# # the "W" is a not a word character.
# # the "A|B" is a special character that means match either A or B.
# # the "(...)" is a special character that means match the expression inside the parentheses.
# # the "(?:...)" is a special character that means match the expression inside the parentheses but do not capture the match.
# # the re.IGNORECASE is a special character that means to ignore case.
# # the re.MULTILINE is a special character that means to match multiple lines.
# # the re.VERBOSE is a special character that means to use verbose mode.
# # the re.DOTALL is a special character that means to match all characters including newlines.
#
# # This code is great but still buggy, it does not allow for an email to have two sub domains after the @. In case
# # the user wanted to use a work email or school email. Ex: "hello@university.go.edu"

# ####################################################################################
# ####################################################################################
import re

email = input("Email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|org|net)$",
             email, re.IGNORECASE):  # the r at the beginning of the string means that the string is a raw string.
    # we can also use r"..." to tell python not to interpret the backslash as a escape character.
    print("Valid email!")
else:
    print("Invalid email!")

# the "." any character is considered except a newline.
# the "*" is a special character that means match zero or more of the preceding characters.
# the "+" is a special character that means match one or more repetitions of the preceding character.
# the "?" is a special character that means match zero or one of the preceding characters.
# the "{m}" is a special character that means match exactly m repetitions of the preceding character.
# the "{m,}" is a special character that means match m or more repetitions of the preceding character.
# the "{m,n}" is a special character that means match from m to n repetitions of the preceding character.
# The program is getting great but there is still another problem. The program does not allow the user to have
# "." in their username. Ex: "hello.world@school.edu"
