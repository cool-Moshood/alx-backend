#!/usr/bin/env python3
"""FIFO CACHING"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO CACHING"""

    def __init__(self):
        """class with parent"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ADD TO CACHE"""
        if key is not None and item is not None:
            lens = len(self.cache_data)
            if lens >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                first_item = self.order.pop(0)
                print(f"DISCARD: {first_item}")
                del self.cache_data[first_item]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
