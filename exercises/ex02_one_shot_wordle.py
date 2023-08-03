"""EX02 - One Shot Wordle."""
__author__ = "730615172"

secret_word: str = "python"
your_word: str = input(f"What is your {len(secret_word)}-letter guess? ")

# Checking for length of word
while len(your_word) != len(secret_word):
    your_word = input(f"That was not {len(secret_word)} letters! Try again: ")

# Constants emoji.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# index for 1 to 1 match  
i: int = 0 
# storing emojis
color_hint = " "  
while i < len(secret_word):
    if secret_word[i] == your_word[i]:
        # the letter match under same index
        color_hint += GREEN_BOX
    else: 
        # new variables to check whether the input word has letters exist but at a different index
        input_i: int = 0

        exist: bool = False
        while exist is False and input_i < len(secret_word):
            if your_word[i] == secret_word[input_i]:
                exist = True
            else:
                input_i += 1
        if exist:
            color_hint += YELLOW_BOX
        else: 
            color_hint += WHITE_BOX
    i += 1
print(color_hint)

if (your_word == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")    