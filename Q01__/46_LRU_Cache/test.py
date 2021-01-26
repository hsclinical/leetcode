#!/usr/bin/python

from Solution import LRUCache
obj = LRUCache(2)

print(obj.put(2, 1))
print(obj.put(2, 2))
print(obj.get(2))
print(obj.put(1, 1))
print(obj.put(4, 1))
print(obj.get(2))
