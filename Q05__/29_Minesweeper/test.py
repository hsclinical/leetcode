#!/usr/bin/python

from Solution import Solution
obj = Solution()

A = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
B = [3,0]
out = obj.updateBoard(A, B)
print(out)
