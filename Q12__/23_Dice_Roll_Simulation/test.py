#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = 2
#B = [1,1,1,1,1,1]
#B = [1,1,2,2,2,3]

#A = 5
#B = [1,1,1,2,2,3]
#A = 4
#B = [2,1,1,3,3,2]

A = 20
B = [8,5,10,8,7,2]

out = obj.dieSimulator(A, B)
print(out)
