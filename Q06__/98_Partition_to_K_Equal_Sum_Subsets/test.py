#!/usr/bin/python

from Solution import Solution
obj = Solution()
#A = [4, 3, 2, 3, 5, 2, 1]
#B = 4

#A = [10,10,10,7,7,7,7,7,7,6,6,6]
#B = 3

#A = [4,5,3,2,5,5,5,1,5,5,5,5,5,5,5,5]
#B = 14

#A = [7,2,2,2,2,2,2,2,3]
#B = 3

#A = [7,6,2,2,2,2,3]
#B = 3


A = [780,935,2439,444,513,1603,504,2162,432,110,1856,575,172,367,288,316]
B = 4

out = obj.canPartitionKSubsets(A, B)
print(out)
