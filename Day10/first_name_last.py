# Time to create some functions with outputs!
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()  # we are capturing the f_name.title() into a variable called formatted_f_name
    formatted_l_name = l_name.title()
    print(f"{formatted_f_name} {formatted_l_name}")  # we then print out the formatted_f_name and formatted_l_name using
    # f-string interpolation.


format_name("carLoS", "dElGadO")
