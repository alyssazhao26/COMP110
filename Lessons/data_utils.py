from csv import DictReader 

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    ## DictReader returns each row in the file. 
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Return Values in a table under a certain header."""
    result: list[str] = []
    # step through table
    for row in table:
        result.append(row[header])
    return result
    # save every value under key 'header'


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats original data."""
    result: dict[str, list[str]] = {}
    # Loop thorugh keys of one row of table
    first_row: dict[str, str] = table[0]
    # for each key, make a dictionary entry will all column values
    for key in first_row:
        result[key] = column_vals(table, key)
    return result