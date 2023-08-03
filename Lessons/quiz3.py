

def shrink(input_dict) -> list[int]:
    new_list = list()
    for i in input_dict:
        if input_dict[i] %2 == 0 and input_dict[i] < 18:
            new_list.append(input_dict[i])
    return new_list

test_dict = {'a': 16, 'b': 20, 'c': 17}

print(shrink(test_dict))