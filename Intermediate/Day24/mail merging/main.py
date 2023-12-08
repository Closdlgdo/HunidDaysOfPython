# Create a letter using first_letter.txt and replace the [name] with the name of the guest from the invited_people.txt
# Save the letters in the folder ready_to_send.

with open("../names/invited_people.txt") as file:
    names = file.readlines()

with open("../letters/first_letter.txt") as file:
    letter = file.read()

for name in names:
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    with open(f"ready_to_send/letter_for_{name}.txt", mode="w") as file:
        file.write(new_letter)
