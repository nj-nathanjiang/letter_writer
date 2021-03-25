PLACEHOLDER = "[name]"

with open("input/names.txt", "r") as file:
    names = file.readlines()

with open("input/letter/letter_template.txt", "r") as file:
    letter = file.read()

for name in names:
    name = name.replace("\n", "")
    new_letter = letter.replace(PLACEHOLDER, "%s" % (name,))
    with open(f"output/letters/letter_to_{name}.txt", "w") as file:
        file.write(new_letter)
