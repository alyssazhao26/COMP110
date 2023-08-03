"""EX03 - Wordle."""
__author__ = "730615172"

def contains_char(word: str, character: str) -> bool:
    """Check if the character exists in the word"""
    assert len(character) == 1
    #index of the word
    i = 0
    while i < len(word):
        if character == word[i]:
            return True
        i = i + 1
    return False

def emojified(guess_word: str, secret_word: str) -> str:
    """"Returns a string of emojis indicating correctness of guess word"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess_word) == len(secret_word)
    idx: int = 0
    emoji_string: str = ""
    while idx < len(secret_word):
        if contains_char(secret_word, guess_word[idx]) == False:
                emoji_string = emoji_string + WHITE_BOX
        else:
            if secret_word[idx] == guess_word[idx]:
                emoji_string = emoji_string + GREEN_BOX
            else:
                 emoji_string = emoji_string + YELLOW_BOX 
        idx = idx + 1
    return emoji_string

def input_guess(word_length: int) -> str:
    guess_input: str = input(f"Enter a {word_length} character word: ")
    while len(guess_input) != word_length:
        guess_input = input(f"That wasn't {word_length} chars! Try again: ")
    return guess_input

def main() -> None: 
    """The entrypoint of the program and amin game loop"""
    #expected word length
    input_l: int = 5
    #secret word
    stored_word: str = "codes"
    #player round
    number_of_round: int = 1
    #Boolean Operator for True
    bool = True
    while number_of_round <= 6 and bool:
        print(f'=== Turn {number_of_round}/6 ===')
        #guess word
        input_word: str = input_guess(input_l)
        print(input_word)
        print(emojified(input_word, stored_word))
        if input_word == stored_word:
            bool = False
        else:
            bool = True
            number_of_round = number_of_round + 1
    if  bool == False:
        print(f'You won in {number_of_round}/6 turns!')
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()