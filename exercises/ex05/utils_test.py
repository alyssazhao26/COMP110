"""ex05 Unit Test."""
__author__ = '730615172'

from exercises.ex05.utils import only_evens, sub, concat


def test_empty() -> None:
    """Empty list."""
    assert only_evens([]) == []


def test_all_odds() -> None:
    """All odds elements."""
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []


def test_all_even() -> None:
    """All even elements."""
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_no_element() -> None:
    """Empty list."""
    first_list: list[int] = [1, 2, 3]
    second_list: list[int] = []
    assert concat(first_list, second_list) == [1, 2, 3]


def test_idential_list() -> None:
    """Identical lists."""
    list_1: list[int] = [3, 4]
    list_2: list[int] = [3, 4]
    assert concat(list_1, list_2) == [3, 4, 3, 4]


def test_negative() -> None:
    """Negative elements."""
    list_1: list[int] = [-1, 3]
    list_2: list[int] = [-2, 2]
    assert concat(list_1, list_2) == [-1, 3, -2, 2]


def test_negative_index() -> None:
    """Negative starting index."""
    start_i: int = -2
    end_i: int = 3
    test_list: list[int] = [0, 1, 2]
    assert sub(test_list, start_i, end_i) == [0, 1, 2]


def test_out_of_range() -> None:
    """Out of range ending index."""
    start_i: int = 0
    end_i: int = 4
    test_list: list[int] = [0, 1]
    assert sub(test_list, start_i, end_i) == [0, 1]


def test_multi_elements() -> None:
    """Multiple elements."""
    start_i: int = 1
    end_i: int = 3
    test_list: list[int] = [1, 2, 3, 4]
    assert sub(test_list, start_i, end_i) == [2, 3]