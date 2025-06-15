"""
Task 2: Character Selection Criteria
Task Description
Modify your code from Task 1 so that the user's first character choice determines the team category.
Once the first valid character is chosen, all following characters must fit the team category to be added to the team.

The three team categories are:

name longer than 10 letters

one word name

name with three vowels

Each valid character below fits only one of the three categories above:

CJ7
Dora
Elsa
Finn from Adventure Time
Goku
Kirby
Mr Peabody
Optimus Prime
Spongebob Squarepants
Xi Yang Yang

For example, if the first character chosen is CJ7, then it satisfies the one word name category.
This means, the user is only allowed to pick: Dora, Elsa, Goku and Kirby as the rest do not fit that category.

If the first character chosen is Finn from Adventure Time, then it satisfies the name longer than 10 letters category.
And so on.

The selection stops when the user decides to stop or when no remaining characters fit the same category.
"""

print("Welcome to the Edge of Insanity!\n")

# define categories
all_char = [
    "CJ7", "Dora", "Elsa", "Finn from Adventure Time", "Goku", "Kirby",
    "Mr Peabody", "Optimus Prime", "Spongebob Squarepants", "Xi Yang Yang"
]
ten_word_plus = ["Finn from Adventure Time", "Optimus Prime", "Spongebob Squarepants"]
one_word = ["CJ7", "Dora", "Elsa", "Goku", "Kirby"]
three_vowels = ["Mr Peabody", "Xi Yang Yang"]

# Initialize count, the chosen category and the selected char
count = 0
selected = []
category = []
category_name = ""

# prompt for the first char to determine category
while True:
    name = input("Enter a character name: ")
    if name in ten_word_plus:
        category, category_name = ten_word_plus, "name longer than 10 letters"
        break
    elif name in one_word:
        category, category_name = one_word, "one word name"
        break
    elif name in three_vowels:
        category, category_name = three_vowels, "name with three vowels"
        break
    else:
        print("Invalid character name. Please try again.\n")

# add first selected character and add 1 count
selected.append(name)
count += 1
print(f"Congrats, you have added {name} to your team!\n")

#ask the user whether to continue
if input("Do you wish to continue? (Y/N) \n") == "Y":

    #keep asking for input if there are char in the chosen category
    while count < len(category):
        name = input("Enter a character name: ")

        # check if character was already chosen
        if name in selected:
            print(f"You have already chosen {name}. Please try again.\n")
            continue

        # add character to the team if the input is in the chosen category
        elif name in category:
            selected.append(name)
            count += 1
            print(f"Congrats, you have added {name} to your team!")

        # continue if the input is not in the chosen category
        elif name in all_char:
            print(f"{name} does not fit the '{category_name}' category. Please try again.\n")
            continue

        # continue if input invalid character
        else:
            print("Invalid character name. Please try again.\n")
            continue

        # ask if user wants to continue
        if count < len(category):
            print()
            if input("Do you wish to continue? (Y/N) ") == "N":
                break
            print()

    #exit loop if there is no char in chosen category
    if count == len(category):
        print(f"No more characters fit the '{category_name}' category.")

# output the number of char selected, mind "s" if there are more than 1 char
print(f"You have {count} character{'s' if count > 1 else ''} in your team!")
