names = []

for _ in range(3):
    names.append(input("Please enter your name: "))

for name in sorted(names):
    print(f"Hello, {name}!")

# Every time we rerun the program, the names do not get saved. They will simply disappear and will
# be replaced with the new names. If a program required the names to be saved, then this would not work out.
