def save_user(
        **user):  # we can pass multiple key value pairs/arguments when we have double asterisk. Python will return
    # a dictionary automatically.
    print(user["name"])
    print(user["age"])


save_user(id=1, name="Carlos",
          age=32)  # we can pass keyword arguments to the user argument. This will create a dictionary.
#  output: {'id': 1, 'name': 'Carlos', 'age': 32}
