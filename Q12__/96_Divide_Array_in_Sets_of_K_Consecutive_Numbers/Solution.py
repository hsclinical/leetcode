from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0:
            return False
        else:
            numToFreq = {}
            for num in nums:
                if num not in numToFreq:
                    numToFreq[ num ] = 0
                numToFreq[ num ] += 1

            numKey = sorted(numToFreq.keys())

            outcome = True
            for num in numKey:
                if numToFreq[ num ] != 0:
                    for i in range(k):
                        if i == 0:
                            numToRemove = numToFreq[ num ]
                            numToFreq[ num ] = 0
                        else:
                            if num + i in numToFreq and numToFreq[ num + i ] >= numToRemove:
                                numToFreq[ num + i ] -= numToRemove
                            else:
                                outcome = False
                                break
                    if not outcome:
                        break
            if outcome:
                for num in numKey:
                    if numToFreq[ num ] != 0:
                        outcome = False
                        break
                return outcome
            else:
                return outcome
