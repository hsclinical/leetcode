#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = [[0,0],[2,1]]
#B = [[1,2],[3,3]]

#A = [[0,0],[1,1],[2,0]]
#B = [[1,0],[2,2],[2,1]]

A = [[0,0],[1,0],[2,0],[3,0],[4,0]]
B = [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999]]
out = obj.assignBikes(A, B)
print(out)
