from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k <= 0:
            return 0
        else:
            numOfCards = len(cardPoints)
            totalPart1 = sum(cardPoints) * (k//numOfCards)
            k = k%numOfCards

            totalPart2 = sum(cardPoints[:k])
            currValue = totalPart2
            for i in range(k):
                currValue = currValue - cardPoints[k-i-1] + cardPoints[-(i+1)]
                if totalPart2 < currValue:
                    totalPart2 = currValue
            total = totalPart1 + totalPart2

            return total