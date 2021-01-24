#!/usr/bin/python

from Solution import Solution
obj = Solution()

A = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

out = obj.maximalSquare(A)
print(out)
