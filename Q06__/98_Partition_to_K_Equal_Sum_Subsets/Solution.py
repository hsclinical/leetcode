from typing import List
from functools import lru_cache

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        numsSum = sum(nums)
        if numsSum % k != 0:
            return False
        else:
            subSum = int(numsSum / k)
            cntSum = 0
            midNums = []
            for i, num in enumerate(nums):
                if num > subSum:
                    return False
                elif num == subSum:
                    cntSum += 1
                else:
                    midNums.append(num)
            if cntSum > k:
                return False
            elif cntSum == k and sum(midNums) == 0:
                return True
            elif cntSum == k-1 and sum(midNums) == subSum:
                return True
            else:
                # process midNums and (k - cntSum)
                sortedNumTuple = tuple( reversed(midNums) )
                return self.findCombination(sortedNumTuple, subSum, k-cntSum, subSum, 0)

    @lru_cache(maxsize = None)
    def findCombination(self, numTuple, subSum, k, numTarget, curK):
        for i, num in enumerate(numTuple):
            if numTuple[i] <= numTarget:
                if numTuple[i] == numTarget:
                    if k - curK <= 2:
                        return True
                    else:
                        outcome = self.findCombination(numTuple[:i] + numTuple[i+1:], subSum, k, subSum, curK+1)
                else:
                    outcome = self.findCombination(numTuple[:i] + numTuple[i+1:], subSum, k, numTarget-numTuple[i], curK)

                if outcome:
                    return True
            else:
                break
        return False
