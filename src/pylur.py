
from llist import dllist, dllistnode
class LRU(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.__hashmap = {}
        self.__cache = dllist()
    def get(self, key):
        r = None
        if key in self.__hashmap:
            r = self.__cache.remove(self.__hashmap[key])
            self.__cache.appendleft(r)
        return r.value
    def put(self, key, val):
        v = dllistnode(val)
        if key in self.__hashmap:
            self.__cache.remove(self.__hashmap[key])
            if self.__hashmap[key] != v: self.__hashmap[key] = v
        elif self.size < self.capacity:
            self.__hashmap[key] = v
            self.size += 1
        else: self.__hashmap.remove(self.__cache.pop())
        self.__cache.appendleft(v)
