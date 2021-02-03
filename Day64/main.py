PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()
    print(names)

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()

for name in names:
    new_letter = letter_contents.replace(PLACEHOLDER, name.strip())
    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.docx", "w") as finished_letter:
        finished_letter.write(new_letter)
