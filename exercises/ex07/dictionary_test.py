"""Ex07 Unit test."""
__author__ = "730615172"

from exercises.ex07.dictionary import invert
import pytest
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_empty_dict() -> None:
    """Returns empty list."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_multi_elements() -> None:
    """Output inverse dictionary."""
    test_dict: dict[str, str] = {'a': 'Monday', 'b': 'Tuesday', 'c': 'Wednesday'}
    assert invert(test_dict) == {'Monday': 'a', 'Tuesday': 'b', 'Wednesday': 'c'}


def test_one_element() -> None:
    """Returns the correct dict."""
    test_dict: dict[str, str] = {'Vowel': 'a'}
    assert invert(test_dict) == {'a': 'Vowel'}


def test_key_error() -> None:
    """Check for identical keys."""
    with pytest.raises(KeyError):
        test_dict = {'kris': 'jordan', 'michael': 'jordan'}
        invert(test_dict)


def test_multi_element() -> None:
    """Return the most frequent called value."""
    test_dict: dict[str, str] = {'a': 'pink', 'b': 'black', 'c': 'red', 'd': 'black'}
    assert favorite_color(test_dict) == "black"


def test_tie_color() -> None:
    """Returns the color that first appeared."""
    test_dict: dict[str, str] = {'a': 'pink', 'b': 'pink', 'c': 'black', 'd': 'black'}
    assert favorite_color(test_dict) == 'pink'


def test_single_element() -> None:
    """Returns the only element."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ''


def test_unique_strs() -> None:
    """Returns 1 for each str."""
    test_list: list[str] = ['a', 'b', 'c']
    assert count(test_list) == {'a': 1, 'b': 1, 'c': 1}


def test_multi_count() -> None:
    """Returns the correct count."""
    test_list: list[str] = ['a', 'a', 'b', 'b']
    assert count(test_list) == {'a': 2, 'b': 2}


def test_empty() -> None:
    """Returns the empty dict."""
    test_list: list[str] = []
    assert count(test_list) == {}