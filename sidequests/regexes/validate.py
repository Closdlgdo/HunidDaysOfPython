# Regex is a regular expression that matches a string against a pattern.

email = input("Email: ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

# This program is buggy because we set a very low bar. we only look for the @ so we can only input the @ and nothing else
# and the code would still call it as valid.
# This doesn't fix the code because we only look for the @ and a dot and nothing else.
