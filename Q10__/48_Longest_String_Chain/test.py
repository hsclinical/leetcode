#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = ["a","b","ba","bca","bda","bdca"]
#A = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
A = ["a","b","ab","bac"]

out = obj.longestStrChain(A)
print(out)
