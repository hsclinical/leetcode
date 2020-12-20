#!/usr/bin/python

'''
["SnapshotArray","snap","snap","get","set","snap","set"]
[[4],[],[],[3,1],[2,4],[],[1,4]]
'''

from Solution import SnapshotArray
'''
obj = SnapshotArray(4)
obj.snap()
obj.snap()
print(obj.get(3, 1))
obj.set(2, 4)
obj.snap()
obj.set(1, 4)
#
obj = SnapshotArray(2)
obj.snap()
print(obj.get(1, 0))
print(obj.get(0, 0))
obj.set(1, 8)
print(obj.get(1, 0))
obj.set(0, 20)
print(obj.get(0, 0))
obj.set(0, 7)
'''
'''
obj = SnapshotArray(3)
obj.set(0, 5)
obj.snap()
obj.set(0, 6)
print(obj.get(0, 0))
'''
'''
obj = SnapshotArray(1)
obj.set(0, 4)
obj.set(0, 16)
obj.set(0, 13)
obj.snap()
print(obj.get(0, 0))
obj.snap()
'''
#["SnapshotArray","snap","get","get","set","snap","set","get","set","snap","get","set","set"]
#[[1],[],[0,0],[0,0],[0,2],[],[0,14],[0,1],[0,12],[],[0,0],[0,17],[0,16]]

obj = SnapshotArray(1)
obj.snap()
print(obj.get(0, 0))
print(obj.get(0, 0))
obj.set(0, 2)
obj.snap()
obj.set(0, 14)
print(obj.get(0, 1))
obj.set(0, 12)
obj.snap()
print(obj.get(0, 0))
obj.set(0, 17)
obj.set(0, 16)

