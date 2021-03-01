from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        minSum = sum(range(1,1+k))
        maxSum = sum(range(10-k,10))
        if n > maxSum or n < minSum:
            return []
        elif n == maxSum:
            return [ list(range(10-k,10)) ]
        elif n == minSum:
            return [ list(range(1,1+k)) ]
        else:
            rawList = self.checkAllCombination(n, k)
            outList = [ x for x in rawList if sum(x) == n ]
            return outList

    def checkAllCombination(self, n, kLeft):
        if kLeft == 1:
            return [ [x] for x in range(1, 10) if x <= n ]
        else:
            outList = []
            curList = [ x for x in range(1, 10) if x <= n ]
            prevList = self.checkAllCombination(n, kLeft - 1)
            for curNum in curList:
                for prevNum in prevList:
                    if curNum not in prevNum and curNum < prevNum[0]:
                        newList = [ curNum ] + prevNum
                        if sum(newList) <= n:
                            outList.append(newList)
        return outList

