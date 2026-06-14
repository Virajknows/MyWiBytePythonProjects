print()

playername = input('Hello what is your name? ')
print()
print()
player_mood = input(f'Hello {playername}, How are you? ')

print()
print()

print("That's good to hear")

print()
print()

answer = input("Do you like Python? (yes/no): ")

if answer.lower() == "yes":
    print("That's awesome!")
else:
    print("Oh, maybe you'll like it more soon!")

print()

answer = input("would you like to check your age? (Yes/No): ")

if answer.lower() == "yes":
    print("PLEASE ENTER YOUR DATE OF BIRTH")
else:
    print("SORRY BUT PLEASE ENTER YOUR DATE OF BIRTH")

import datetime

today = datetime.date.today()

print()

year = int(input("Year (YYYY): "))
month = int(input("Month (MM): "))
day = int(input("Day (DD): "))

print()

birth_date = datetime.date(year, month, day)

age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

print(f"You are {age} years old!")
print()

LETTERS = {
    'A': ["  #  ", " # # ", "#####", "#   #", "#   #"],
    'B': ["#### ", "#   #", "#### ", "#   #", "#### "],
    'C': [" ####", "#    ", "#    ", "#    ", " ####"],
    'D': ["#### ", "#   #", "#   #", "#   #", "#### "],
    'E': ["#####", "#    ", "###  ", "#    ", "#####"],
    'F': ["#####", "#    ", "###  ", "#    ", "#    "],
    'G': [" ####", "#    ", "# ###", "#   #", " ####"],
    'H': ["#   #", "#   #", "#####", "#   #", "#   #"],
    'I': ["#####", "  #  ", "  #  ", "  #  ", "#####"],
    'J': ["#####", "    #", "    #", "#   #", " ### "],
    'K': ["#   #", "#  # ", "###  ", "#  # ", "#   #"],
    'L': ["#    ", "#    ", "#    ", "#    ", "#####"],
    'M': ["#   #", "## ##", "# # #", "#   #", "#   #"],
    'N': ["#   #", "##  #", "# # #", "#  ##", "#   #"],
    'O': [" ### ", "#   #", "#   #", "#   #", " ### "],
    'P': ["#### ", "#   #", "#### ", "#    ", "#    "],
    'Q': [" ### ", "#   #", "# # #", "#  # ", " ## #"],
    'R': ["#### ", "#   #", "#### ", "#  # ", "#   #"],
    'S': [" ####", "#    ", " ### ", "    #", "#### "],
    'T': ["#####", "  #  ", "  #  ", "  #  ", "  #  "],
    'U': ["#   #", "#   #", "#   #", "#   #", " ### "],
    'V': ["#   #", "#   #", "#   #", " # # ", "  #  "],
    'W': ["#   #", "#   #", "# # #", "## ##", "#   #"],
    'X': ["#   #", " # # ", "  #  ", " # # ", "#   #"],
    'Y': ["#   #", " # # ", "  #  ", "  #  ", "  #  "],
    'Z': ["#####", "   # ", "  #  ", " #   ", "#####"],
    ' ': ["     ", "     ", "     ", "     ", "     "],
}

DIGITS = {
    '0': [" ### ", "#   #", "#   #", "#   #", " ### "],
    '1': ["  #  ", " ##  ", "  #  ", "  #  ", " ### "],
    '2': [" ### ", "    #", " ### ", "#    ", "#####"],
    '3': ["#####", "    #", " ### ", "    #", "#####"],
    '4': ["#   #", "#   #", "#####", "    #", "    #"],
    '5': ["#####", "#    ", "#### ", "    #", "#### "],
    '6': [" ### ", "#    ", "#### ", "#   #", " ### "],
    '7': ["#####", "    #", "   # ", "  #  ", " #   "],
    '8': [" ### ", "#   #", " ### ", "#   #", " ### "],
    '9': [" ### ", "#   #", " ####", "    #", " ### "]
}

ART = {**LETTERS, **DIGITS}

def print_art(text):
    text = text.upper()
    for row in range(5):
        line = "  ".join(
            ART[char][row] if char in ART else "     "
            for char in text
        )
        print(line)
    print()

print_art(playername)
print_art("YOU  ARE  " + str(age))
print_art("YEARS OLD")