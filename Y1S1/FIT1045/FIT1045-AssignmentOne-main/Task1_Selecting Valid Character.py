"""
Task 1: Selecting Valid Character
Task Description
Write a Python program that prompts the user to enter a character name. The program should keep prompting the user until a valid character name is entered.

Once a valid character name is entered, ask the user if they wish to continue. If they choose to continue, prompt the user to select more characters. Repeat this process until the user decides to stop, then inform the user of the number of successful character selections.

The valid character options are:

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
"""



print("Welcome to the Edge of Insanity!\n")

# list characters
characters = [
    "CJ7", "Dora", "Elsa", "Finn from Adventure Time", "Goku", "Kirby",
    "Mr Peabody", "Optimus Prime", "Spongebob Squarepants", "Xi Yang Yang"
]
count = 0  # initialize count

# while loop to keep prompting user for input if True
while True:
    name = input("Enter a character name: ")

    # count+1 if choose an existing character
    if name in characters:
        count += 1
        print(f"Congrats, you have added {name} to your team!\n")

        # Prompt to continue or stop
        choice = input("Do you wish to continue? (Y/N) \n")
        if choice == "N":
            break

    # no further action if choose invalid character
    else:
        print("Invalid character name. Please try again.\n")

# format output the number of characters chosen, mind the singular form for "character"
team = f"You have {count} character{'s' if count != 1 else ''} in your team!"
print(team)

