"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730615172"

one_word: str = input("Enter a 5-character: ").lower()

if (len(one_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

one_character: str = input("Enter a single character: ").lower()

if (len(one_character) != 1):
    print("Error: Character must be a single character")
    exit()

print("Searching for " + one_character + " in " + one_word)


number_of_index: int = 0

if (one_character == one_word[0]):
    print(one_character + " found at index 0")
    number_of_index = number_of_index + 1
if (one_character == one_word[1]):
    print(one_character + " found at index 1")
    number_of_index = number_of_index + 1
if (one_character == one_word[2]):
    print(one_character + " found at index 2")
    number_of_index = number_of_index + 1
if (one_character == one_word[3]):
    print(one_character + " found at index 3")
    number_of_index = number_of_index + 1
if (one_character == one_word[4]):
    print(one_character + " found at index 4")
    number_of_index = number_of_index + 1

number_of_letters: int = 0
if (number_of_index == 0):
    print("No instances of " + one_character + " found in " + one_word)
if (number_of_index == 1):
    number_of_letters = number_of_letters + number_of_index
    print(str(number_of_index) + "instance of " + one_character + " found in " + one_word)
if (number_of_index == 2):
    number_of_letters = number_of_letters + number_of_index
    print(str(number_of_letters) + " instances of " + one_character + " found in " + one_word)
if (number_of_index == 3):
    number_of_letters = number_of_letters + number_of_index
    print(str(number_of_letters) + " instances of " + one_character + " found in " + one_word)
if (number_of_index == 4):
    number_of_letters = number_of_letters + number_of_index
    print(str(number_of_letters) + " instances of " + one_character + " found in " + one_word)
if (number_of_index == 5):
    number_of_letters = number_of_letters + number_of_index
    print(str(number_of_letters) + " instances of " + one_character + " found in " + one_word)