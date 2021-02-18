from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        numLen = len(nums)
        numSum = sum(nums)
        if numSum < target:
            return 0
        elif numSum == target:
            return numLen
        else:
            curSum = 0
            idxBgn = 0
            idxEnd = -1
            for i in range(numLen):
                curSum += nums[i]
                if curSum >= target:
                    idxEnd = i
                    break

            minLen = idxEnd - idxBgn + 1
            while True:
                if curSum >= target:
                    if idxEnd - idxBgn + 1 < minLen:
                        minLen = idxEnd - idxBgn + 1
                    curSum -= nums[idxBgn]
                    idxBgn += 1
                else:
                    idxEnd += 1
                    if idxEnd >= numLen:
                        break
                    curSum += nums[idxEnd]

            return minLen