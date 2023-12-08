# Create a letter using first_letter.txt and replace the [name] with the name of the guest from the invited_people.txt
# Save the letters in the folder ready_to_send.

# Read names from 'invited_people.txt'
with open("names/invited_people") as file:
    names = file.readlines()

# Read the template letter
with open("letters/first_letter") as file:
    letter = file.read()

# Create personalized letters
for name in names:
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    output_path = f"./output/ready_to_send/letter_for_{name}.txt"
    with open(output_path, mode="w") as file:
        file.write(new_letter)
