#!/usr/bin/python

from Solution import Solution
obj = Solution()

A = ["f","p","a"]
B = 8
C = 7

#A = ["a"]
#B = 10000
#C = 10000

#A = ["a","b","c"]
#B = 3
#C = 1

#A = ["a","bcd"]
#B = 20000
#C = 20000

out = obj.wordsTyping(A, B, C)
print(out)
