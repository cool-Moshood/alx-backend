#!/usr/bin/env python3
""" a function named index_range that takes
two integer arguments page and page_size"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for the given pagination parameters.

    Args:
        page (int): The current page number (1-based index).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index
        (inclusive) and end index (exclusive).
    """

    if page < 1 or page_size < 1:
        return ValueError("the parameter must be positive integer")

    else:
        start_index = ((page - 1) * page_size)
        end_index = start_index + page_size

    return start_index, end_index
