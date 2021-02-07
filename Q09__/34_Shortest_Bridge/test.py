#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
A = [[0,1,0],[0,0,0],[0,0,1]]
out = obj.shortestBridge(A)
print(out)
