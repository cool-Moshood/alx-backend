#!/usr/bin/env python3

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)

        self.cache[key] = value

    def get(self, key):
        return self.cache.get(key)


# Example usage:
cache = LRUCache(3)

cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")

# Output: "A" (Item 1 is accessed and becomes the most recently used)
print(cache.get(1))
# Output: "B" (Item 2 is accessed and becomes the most recently used)
print(cache.get(2))
print(cache.get(3))  # Output: None (Item 4 is not in the cache)

cache.put(4, "D")
# Output: None (Item 3 was the least recently used and got evicted)
print(cache.get(1))
