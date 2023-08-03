"""Ex07 Dictionary Functions."""
__author__ = "730615172"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys to values and the other way around."""
    # Check for identical elements
    new_key_list: list[str] = list()
    for keys in input_dict:
        new_key_list.append(input_dict[keys])
    idx: int = 0
    while idx + 1 < len(new_key_list):
        if new_key_list[idx] == new_key_list[idx + 1]:
            raise KeyError("Cannot contain same element for valid output.")
        idx += 1
    # Append output dict. 
    output_dict: dict[str, str] = {}
    for i in input_dict:
        output_dict[input_dict[i]] = i
    return output_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the most frequent value."""
    value_list: list[str] = list()
    for i in input_dict:
        value_list.append(input_dict[i])
    color_called: list[str] = list()
    idx_1: int = 0
    while idx_1 < len(value_list):
        for element in range(0, len(value_list), 1):
            if idx_1 == element:
                color_called 
            elif value_list[idx_1] == value_list[element]:
                color_called.append(value_list[element])
        idx_1 += 1
    if len(value_list) == 1:
        return value_list[0]
    elif len(value_list) == 0:
        return ''
    return color_called[0]


def count(input_list: list[str]) -> dict[str, int]:
    """Returns the count of each number."""
    output_dict: dict[str, int] = {}
    for i in input_list:
        if i in output_dict:
            output_dict[i] += 1
        else:
            output_dict[i] = 1
    return output_dict