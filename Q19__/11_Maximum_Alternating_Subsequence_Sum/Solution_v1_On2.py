from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        numsLen = len(nums)
        scores = nums[:]
        maxScore = max(nums)
        for i in range(numsLen):
            if i > 1:
                minInRange = nums[i-1]
                for j in range(i-1, 0, -1):
                    if nums[j] < minInRange:
                        minInRange = nums[j]
                    maxDiff = nums[i] - minInRange
                    if maxDiff + scores[j-1] > scores[i]:
                        scores[i] = maxDiff + scores[j-1]
                    if scores[i] > maxScore:
                        maxScore = scores[i]
        return maxScore
