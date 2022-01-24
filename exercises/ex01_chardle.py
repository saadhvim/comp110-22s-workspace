"""EX01 - Chardle - A cute step toward Worldle."""

__author__ = "730486125"

word: str = input("Enter a 5-character word: ")
if len(word) < 5:
    print("Error: Word must contain 5 characters.")
    exit()

if len(word) < 5:
    print("Error: Word must contain 5 characters.")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) < 1:
    print("Error: Character must be a single character.")
    exit()

if len(single_character) > 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + word)

match_characters: int = 0 

if single_character == word[0]:
    print(single_character + " found at index 0")
    match_characters = match_characters + 1

if single_character == word[1]:
    print(single_character + " found at index 1")
    match_characters = match_characters + 1

if single_character == word[2]:
    print(single_character + " found at index 2")
    match_characters = match_characters + 1

if single_character == word[3]:
    print(single_character + " found at index 3")
    match_characters = match_characters + 1

if single_character == word[4]:
    print(single_character + " found at index 4")
    match_characters = match_characters + 1

if match_characters == 0:
    print("No instance of " + single_character + " found in " + word)

if match_characters == 1:
    print("1 instance of " + single_character + " found in " + word)

if match_characters == 2:
    print("2 instances of " + single_character + " found in " + word)

if match_characters == 3:
    print("3 instances of " + single_character + " found in " + word)

if match_characters == 4:
    print("4 instances of " + single_character + " found in " + word)
