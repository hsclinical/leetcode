from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles
        numDiff = self.findMinmax(0, len(piles)-1, 1, 'A')
        numA = int((sum(piles) + numDiff)/2)
        return numA

    @lru_cache(maxsize=None)
    def findMinmax(self, bgnIdx, endIdx, M, person):
        if endIdx - bgnIdx + 1 <= 2 * M:
            num = sum(self.piles[bgnIdx:(endIdx+1)])
            if person == 'A':
                return num
            else:
                return (-1) * num
        else:
            results = []
            tmpNum = -1
            nextPerson = 'A'
            if person == 'A':
                tmpNum = 1
                nextPerson = 'B'
            for i in range(1, (2 * M + 1)):
                nextM = max(i, M)
                results.append( tmpNum * sum(self.piles[bgnIdx:(bgnIdx+i)]) + self.findMinmax(bgnIdx+i, endIdx, nextM, nextPerson) )

            if person == 'A':
                return max(results)
            else:
                return min(results)

