from typing import Dict, Any


def enumarate_task3(value: dict):
    """
    Function return indexed dict.
    Args:
        value:

    Returns:

    """
    result: dict[Any, Any] = dict(enumerate(value))
    return result


print(enumarate_task3(['a', 'b', 'c', 'd', 'e']))

