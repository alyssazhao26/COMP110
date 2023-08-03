

def odd_and_even(input: list[int]) -> list[int]:
    """a."""
    new_list: list[int] = list()
    i: int = 0
    while i < len(input):
        if i % 2 == 0:
            if input[i] % 2 != 0:
                new_list.append(input[i])
        i += 1
    return new_list

print(odd_and_even([2,3,4,5]))
print(odd_and_even([7,8,10,10,5,12,3,2,11,8]))