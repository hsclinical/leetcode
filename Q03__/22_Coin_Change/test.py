#!/usr/bin/python

from Solution import Solution

obj = Solution()

inputA = [1,2,5]
inputB = 100

#inputA = [1,3,4,5]
#inputB = 7

#inputA = [2]
#inputB = 3

out = obj.coinChange(coins=inputA, amount=inputB)
print(out)
