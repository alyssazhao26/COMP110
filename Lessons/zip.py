"""CQ04 - zip function."""

def zip(key_list: list[str], value_list: list[int]) -> dict[str, int]:
    """Return a dictionary wiht str keys and int values"""
    index: int  = 0
    output_dict: dict[str, int] = {}
    if len(key_list) != len(value_list):
        return output_dict
    if len(key_list) == 0  or len(value_list) == 0:
        return output_dict
    while index < len(key_list):
        output_dict[key_list[index]] = value_list[index]
        index += 1
    return output_dict