"""Generic functions to be used anywhere. All functions only have stdlib dependencies."""
from re import sub


def is_key_value_in_list(
    key: any, value: any, search_list: list, return_item: bool = False
) -> bool:
    """Iterate through a list of dicts to check if a specific key/value pair exists."""
    if isinstance(search_list, list):
        for item in search_list:
            if item.__contains__(key) and item[key] == value:
                if return_item:
                    return item
                return True
    return False


def remove_duplicates_from_list(duplicate_list: list) -> list:
    """Returns a list that contains no duplicate values"""
    return list(dict.fromkeys(duplicate_list))


def clean_string(string: str) -> str:
    """Removes non-alphanumerics from a string"""
    return sub(r"\W+", "", string).lower()


def str_to_bool(string: str, default_value: bool = True) -> bool:
    """Converts a string into a boolean."""
    if isinstance(string, str):
        if string.lower() == "true" or string == "1":
            return True
        if string.lower() == "false" or string == "0":
            return False
    return default_value


def str_to_int(value: str, default_value: int = 0) -> int:
    """Converts a string into a integer."""
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return default_value
