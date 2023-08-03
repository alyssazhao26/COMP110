
def value_exists(input_dict: dict[str, int], input_int: int) -> bool:
    new_list = []
    for keys in input_dict:
        if input_dict[keys] == input_int:
            new_list.append(input_int)
    if len(new_list) == 0:
        return False
    else: 
        return True
            

test_dict = {"a": 2, 'b': 4, 'c': 7, 'd': 1}

print(value_exists(test_dict, 4))
print(value_exists(test_dict, 5))