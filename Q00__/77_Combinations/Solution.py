from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.getAllCombination( n, k )

    def getAllCombination(self, n, kLeft):
        if kLeft == 1:
            return [ [x] for x in range(1, n+1) ]
        else:
            outList = []
            curList = [ x for x in range(1, n+1) ]
            prevList = self.getAllCombination(n, kLeft-1)
            for curNum in curList:
                for prevNum in prevList:
                    if curNum < prevNum[0]:
                        outList.append( [curNum] + prevNum )
            return outList