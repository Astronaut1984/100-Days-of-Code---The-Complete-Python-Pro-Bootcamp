# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def main():
    # Open the Invited names file and store names in a list
    # DONE
    names = []
    with open("./Input/Names/invited_names.txt", "r") as names_file:
        for name in names_file:
            names.append(name.strip())
    # Open the template letter and store that in a string
    template = ""
    with open("./Input/Letters/starting_letter.txt", "r") as template_file:
        template = template_file.read().strip()

    # For each name in the list, create a letter file and store it in the output directory
    for name in names:
        letter = template.replace("[name]", name)
        with open(f"./Output/{name}.txt", "w") as letter_file:
            letter_file.write(letter)


if __name__ == "__main__":
    main()
