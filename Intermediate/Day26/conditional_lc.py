# new_list = [new_item for item in list if test]
# Conditional List Comprehensions
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
