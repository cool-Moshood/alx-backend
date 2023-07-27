#!/usr/bin/env python3
"""Basic cache that inherit base caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache class"""

    def put(self, key, item):
        """adding caching"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get the cache"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
