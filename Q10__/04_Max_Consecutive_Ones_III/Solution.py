from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        aLen = len(A)
        if aLen <= K:
            return aLen

        longestLen = 0
        idxBgn = 0
        zeroCnt = 0
        for i in range(aLen):
            if A[i] == 0:
                zeroCnt += 1

            if zeroCnt > K:
                if i - idxBgn > longestLen:
                    longestLen = i - idxBgn
                while True:
                    if A[idxBgn] == 0:
                        zeroCnt -= 1
                    idxBgn += 1
                    if zeroCnt <= K:
                        break

        if aLen - idxBgn > longestLen:
            longestLen = aLen - idxBgn

        return longestLen