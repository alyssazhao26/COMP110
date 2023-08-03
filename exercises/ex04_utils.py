"""Ex04 - Utils."""
__author__ = "730615172"


def all(list_input: list[int], single_int: int) -> bool:
    """Returns True only if when single_int match with all numbers in int_list."""
    # list index
    idx: int = 0
    if len(list_input) == 0:
        return False
    while idx < len(list_input):
        if list_input[idx] != single_int:
            return False
        idx += 1
    return True


def max(second_input: list[int]) -> int:
    """Returns the largest number in the list."""
    if len(second_input) == 0:
        raise ValueError("max() arg is an empty list")
    max_number: int = second_input[0]
    i: int = 0
    while i < len(second_input):
        new_number: int = second_input[i]
        if new_number > max_number:
            max_number = new_number
        i += 1
    return max_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns whether the two lists are the exact same."""
    # list index
    index: int = 0
    while len(list_1) == 0 or len(list_2) == 0:
        if len(list_1) == 0 and len(list_2) == 0:
            return True
        else:
            return False
    while index < len(list_1):
        if list_1[index] != list_2[index] or len(list_1) != len(list_2):
            return False
        index += 1
    return True