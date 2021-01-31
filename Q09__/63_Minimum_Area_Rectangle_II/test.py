#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = [[1,2],[2,1],[1,0],[0,1]]
#A = [[0,1],[2,1],[1,1],[1,0],[2,0]]
A = [[0,3],[1,2],[3,1],[1,3],[2,1]]
out = obj.minAreaFreeRect(A)
print(out)
