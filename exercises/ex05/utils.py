"""Ex05 Functions Storage."""

__author__ = '730615172'


def only_evens(input_list: list[int]) -> list[int]:
    """Return a list of even integers."""
    i: int = 0
    new_list: list[int] = []
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            new_list.append(input_list[i]) 
        i += 1
    return new_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Return a combination of two lists."""
    output_list: list[int] = []
    idx: int = 0
    while idx < len(list_1):
        output_list.append(list_1[idx])
        idx += 1
    i: int = 0
    while i < len(list_2):
        output_list.append(list_2[i])
        i += 1
    return output_list


def sub(list: list[int], int1: int, int2: int) -> list[int]:
    """Return the sublist at given indexes."""
    output_list: list[int] = []
    if len(list) == 0 or int1 >= len(list) or int2 <= 0:
        output_list = []
        return output_list
    if int1 < 0:
        int1 = 0
    if int2 > len(list):
        int2 = len(list) 
    while int1 <= (int2 - 1):
        output_list.append(list[int1])
        int1 += 1
    return output_list 