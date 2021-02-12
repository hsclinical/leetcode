#!/usr/bin/python

import os
from Solution import Solution

obj = Solution()

#A = 6
#B = [[0,1],[1,3],[2,3],[4,0],[4,5]]

A = 5
B = [[1,0],[1,2],[3,2],[3,4]]
print(obj.minReorder(A, B))
