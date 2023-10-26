# Time to create some functions with outputs!
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()  # we are capturing the f_name.title() into a variable called formatted_f_name
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"  # replacing the print function with return allows this part of the code
    # to replace the call function


# Since we are returning the formatted string as the output, we will save the output inside a variable.
formatted_string = format_name("carLoS", "dElGadO")
print(formatted_string)
