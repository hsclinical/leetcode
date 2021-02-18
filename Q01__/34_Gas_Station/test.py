#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = [1,2,3,4,5]
#B = [3,4,5,1,2]

#A = [2,3,4]
#B = [3,2,3]

#A = [5,1,2,3,4]
#B = [4,4,1,5,1]

A = [3,1,1]
B = [1,2,2]
out = obj.canCompleteCircuit(A, B)
print(out)
