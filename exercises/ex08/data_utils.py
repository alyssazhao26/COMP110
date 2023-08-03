"""Ex08 Data Wrangling."""
__author__ = "730615172"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the data from CSV file and returns a list of dict."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for i in csv_reader:
        result.append(i)
    file_handle.close()
    return result


def column_values(input_list: list[dict[str, str]], key: str) -> list[str]:
    """Returns a list of values in a column that has key as names."""
    result: list[str] = []
    for dict in input_list:
        result.append(dict[key])
    return result


def columnar(input_list: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform table from a list of dict into a dict containing str as keys and list as values."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = input_list[0]
    for keys in first_row: 
        result[keys] = column_values(input_list, keys)
    return result


def head(input_dict: dict[str, list[str]], input_int: int) -> dict[str, list[str]]:
    """Returns a new column_based table with only first N rows of data."""
    result_dict: dict[str, list[str]] = {}
    if input_int >= len(input_dict): 
        result_dict = input_dict
        return result_dict
    for keys in input_dict:
        new_list: list[str] = []
        for i in range(0, input_int, 1):
            values = input_dict[keys]
            new_list.append(values[i])
        result_dict[keys] = new_list
    return result_dict


def select(input_dict: dict[str, list[str]], input_list: list[str]) -> dict[str, list[str]]:
    """Returns a column_based table with a subset of original columns."""
    result: dict[str, list[str]] = {}
    for element in input_list:
        result[element] = input_dict[element]
    return result


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a combined version of the two given dictionaries."""
    result: dict[str, list[str]] = {}
    for keys in dict_1:
        result[keys] = dict_1[keys]
    for key in dict_2:
        if key in result:
            result[key] += dict_2[key]
        else:
            result[key] = dict_2[key]
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Returns the count of each of the items in the input ilst."""
    result: dict[str, int] = {}
    for element in input_list:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result