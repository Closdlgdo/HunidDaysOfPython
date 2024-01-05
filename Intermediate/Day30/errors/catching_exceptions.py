# This is how catching exceptions looks like:
# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there was no exception
# finally: do this no matter what
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdfasdf"])  # prints nothing, but it doesn't show an error because of the except operator.
except:  # if we use the except operator, it will ignore all errors.
    file = open("a_file.txt", "w")
    file.write("Something")
