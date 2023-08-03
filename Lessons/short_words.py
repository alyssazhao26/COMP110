

def short_words(input_list: list[str]) -> list[str]:
    new_list = []
    for item in input_list:
        if len(item) < 5:
            new_list.append(item)
        else:
            print(f"{item} is too long!")
    return new_list

my_list = ['sun', 'cloud', 'sky']
print(short_words(my_list))
