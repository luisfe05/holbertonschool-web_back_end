#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a page of the indexed dataset resilient to deletions."""
        data = self.indexed_dataset()
        assert index is None or (
            isinstance(index, int) and 0 <= index <= max(data.keys())
        )

        if index is None:
            index = 0

        data_page = []
        current_index = index
        max_index = max(data.keys())

        while len(data_page) < page_size and current_index <= max_index:
            if current_index in data:
                data_page.append(data[current_index])
            current_index += 1

        return {
            'index': index,
            'next_index': current_index,
            'page_size': len(data_page),
            'data': data_page,
        }
