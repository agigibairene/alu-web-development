#!/usr/bin/python3
"""0. Basic dictionary"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class. Inherits from BaseCaching"""

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
