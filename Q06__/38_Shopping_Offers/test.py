#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = [2,5]
#B = [[3,0,5],[1,2,10]]
#C = [3,2]

A = [2,3,4]
B = [[1,1,0,4],[2,2,1,9]]
C = [1,2,1]

out = obj.shoppingOffers(A, B, C)
print(out)
