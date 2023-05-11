from itertools import chain
from bisect import bisect_left

class BPlusTree:
    def __init__(self, order):
        self._order = order
        self._root = BPlusTreeNode(order, is_leaf=True)

    def __getitem__(self, key):
        return self._root.get(key)

    def __setitem__(self, key, value):
        self._root.insert(key, value)

    def __delitem__(self, key):
        self._root.delete(key)

    def items(self):
        return self._root.items()

    def keys(self):
        return self._root.keys()

    def values(self):
        return self._root.values()

class BPlusTreeNode:
    def __init__(self, order, is_leaf=False):
        self._order = order
        self._is_leaf = is_leaf
        self._keys = []
        self._values = []
        self._pointers = []

    def get(self, key):
        if self._is_leaf:
            index = bisect_left(self._keys, key)
            if index < len(self._keys) and self._keys[index] == key:
                return self._values[index]
            else:
                return None
        else:
            index = bisect_left(self._keys, key)
            return self._pointers[index].get(key)

    def insert(self, key, value):
        if self._is_leaf:
            index = bisect_left(self._keys, key)
            self._keys.insert(index, key)
            self._values.insert(index, value)
            if len(self._keys) > 2 * self._order:
                self._split()
        else:
            index = bisect_left(self._keys, key)
            child = self._pointers[index]
            if len(child._keys) == 2 * self._order:
                child._split()
                if key > self._keys[-1]:
                    index += 1
            self._pointers[index].insert(key, value)

    def delete(self, key):
        if self._is_leaf:
            index = bisect_left(self._keys, key)
            if index < len(self._keys) and self._keys[index] == key:
                self._keys.pop(index)
                self._values.pop(index)
            if len(self._keys) < self._order and self._pointers:
                self._rebalance()
        else:
            index = bisect_left(self._keys, key)
            self._pointers[index].delete(key)
            if len(self._pointers[index]._keys) < self._order and index > 0:
                self._pointers[index - 1]._merge(self._pointers[index])
                self._pointers.pop(index)
                self._keys.pop(index - 1)
            elif len(self._pointers[index]._keys) < self._order and index < len(self._pointers) - 1:
                self._pointers[index]._merge(self._pointers[index + 1])
                self._pointers.pop(index + 1)
                self._keys.pop(index)

    def items(self):
        if self._is_leaf:
            return zip(self._keys, self._values)
        else:
            return chain.from_iterable(ptr.items() for ptr in self._pointers)

    def keys(self):
        if self._is_leaf:
            return self._keys
        else:
            return chain
