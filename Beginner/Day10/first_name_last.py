# Time to create some functions with outputs!
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()  # we are capturing the f_name.title() into a variable called formatted_f_name
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"  # replacing the print function with return allows this part of the code
    # to replace the call function


# We can also use the function call inside the print function rather than assigning it to a variable.
print(format_name("carLoS", "dElGadO"))
