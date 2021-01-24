#!/usr/bin/python

from Solution import NumMatrix
obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])

print(obj.sumRegion(2,1,4,3))
print(obj.sumRegion(1,1,2,2))
print(obj.sumRegion(1,2,2,4))
