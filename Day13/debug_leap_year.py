# year = input()  # This is the wrong piece that breaks the code.
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# The error message shows up when we run the code:
# if year % 4 == 0:
# TypeError: not all arguments converted during string formatting
# What happened is that the input is taking in a string and not an integer and so the first go at the if statement
# does not compute. The input string needs to be converted to an integer.
