#!/usr/bin/env python3
"""LIFO CACHING"""
from collections import deque
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class parent"""

    def __init__(self):
        super().__init__()
        self.key_queue = []

    def put(self, key, item):
        """Add an item to cache"""
        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_item = self.key_queue.pop()
                del self.cache_data[last_item]
                print(f"DISCARD: {last_item}")
        self.cache_data[key] = item
        self.key_queue.append(key)

    def get(self, key):
        """get from cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
