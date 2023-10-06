# > (greater than), >= (greater than or equal), < (less than), <= (less than or equal), == (equality comparing), != (not equal to)
# to ask questions with these symbols we use the "if" statement.

x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y:  # boolean expression that has a true or false answer
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
# elif x != y: logically this is not necessary because the expression is the last argument possible and therefore we dont need an elif.
#     print("x is not equal to y")
else:
    print("x is not equal to y")
