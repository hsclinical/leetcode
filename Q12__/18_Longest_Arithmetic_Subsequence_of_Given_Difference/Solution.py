from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if len(arr) == 0:
            return 0
        longestLen = 0
        maxScore = {}
        for i, num in enumerate(arr):
            newScore = 1
            if num - difference in maxScore:
                newScore = maxScore[ num - difference ] + 1

            if num in maxScore:
                if newScore > maxScore[ num ]:
                    maxScore[ num ] = newScore
            else:
                maxScore[ num ] = newScore

            if newScore > longestLen:
                longestLen = newScore
        return longestLen
