
from llist import dllist, dllistnode
class LRU(object):
    """
    this is a class providing the `least recently used' (LRU) cache eviction policy.
    """
    def __init__(self, capacity):
        """
        constructor.

        args:
            capacity: a positive integer, indicating the capacity of the cache
        returns:
            none.
        """
        self.capacity = capacity
        self.size = 0
        self.__hashmap = {}
        self.__cache = dllist()
    def get(self, key):
        """
        get a value by the key: if the cache contains the key, retrieve the value from cache; otherwise, return None.

        args:
            key: the key associated with a value
        returns:
            the value mapped to the key if it's in cache; otherwise, None.
        """
        r = None
        if key in self.__hashmap:
            r = self.__cache.remove(self.__hashmap[key])
            self.__cache.appendleft(r)
        return r.value
    def put(self, key, val):
        """
        associate the value with the key, and put the entry into cache.

        args:
            key: the key associated with val
            val: the value associating with key
        returns:
            None.
        """
        v = dllistnode(val)
        if key in self.__hashmap:
            self.__cache.remove(self.__hashmap[key])
            if self.__hashmap[key] != v: self.__hashmap[key] = v
        elif self.size < self.capacity:
            self.__hashmap[key] = v
            self.size += 1
        else: self.__hashmap.remove(self.__cache.pop())
        self.__cache.appendleft(v)
    def clear(self):
        """
        clear the cache, and reset all parameters.
        """
        self.__hashmap = {}
        self.__cache = dllist()
        self.size = 0
