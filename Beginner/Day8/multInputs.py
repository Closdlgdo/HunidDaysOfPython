# Functions with more than one input.
def greet(name, location):
    print(f"Hello {name} from {location}")


greet("Carlos", "California")  # Positional arguments
greet("Theano", "Athens")


# def myfunc(a, b, c):
# do this with a            a = 1
# then do this with b       b = 2
# finally do this with c    c = 3
# myfunc(1, 2, 3)

# If you want to be clearer on where you want your arguments to go, you can use keyword arguments.
# def myfunc(a, b, c):
# do this with a
# then do this with b
# finally do this with c
# myfunc(a=1, b=2, c=3)

# Functions with keyword arguments.


def greetings(name, location):
    print(f"Hello {name} from {location}")


greet(name="Carlos", location="California")  # Positional arguments
greet(name="Theano", location="Athens")
