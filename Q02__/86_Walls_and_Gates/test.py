#!/usr/bin/python

from Solution import Solution
obj = Solution()

A = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
print(A)
out = obj.wallsAndGates(A)
print(out)
