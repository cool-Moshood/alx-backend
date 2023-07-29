#!/usr/bin/env python3
"""pagination of csv datafile"""


import csv
import math
from typing import Tuple, List, Dict


def index_range(page=int, page_size=int) -> tuple:
    """a function that return page and page_size"""

    start_index = ((page - 1) * page_size)
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """getting the rquire pages"""

        assert type(page) is int and page > 0
        assert type(page_size) is int and page > 0

        dataset = self.dataset()
        lenght = len(dataset)

        index = index_range(page, page_size)

        if page_size >= lenght:
            return []
        else:
            return dataset[index[0]: index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """fxn that page of dataset"""
        get_p = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + 1

        hyper = {
            "page_size": page_size if page_size <= len(get_p) else len(get_p),
            "page": page,
            "data": get_p,
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages":  total_pages
        }

        return hyper
