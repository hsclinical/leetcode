#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = [ ["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]
A = [ ["0","0","0","0","0"], ["0","0","0","0","0"]]
out = obj.numIslands(A)
print(out)
