from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        numsLen = len(nums)
        # contains only 1 or 2 elements
        if numsLen <= 2:
            return max(nums)

        # contains more than 2 elements
        scores = nums[:]
        fromPrev = [ False ] * numsLen
        maxScore = max(nums[:2])
        for i in range(2, numsLen):
            # check i-2
            if nums[i] > nums[i-1]:
                numSkip1 = nums[i] - nums[i-1] + scores[i-2]
            else:
                numSkip1 = scores[i-2]
            if fromPrev[i-2] and nums[i] > nums[i-2]:
                if numSkip1 < nums[i] - nums[i-2] + scores[i-2]:
                    numSkip1 = nums[i] - nums[i-2] + scores[i-2]

            # check i-3
            if i > 2:
                if nums[i] > min(nums[i-1], nums[i-2]):
                    numSkip2 = nums[i] - min(nums[i-1], nums[i-2]) + scores[i-3]
                else:
                    numSkip2 = scores[i-3]
                if fromPrev[i-3] and nums[i] > nums[i-3]:
                    if numSkip2 < nums[i] - nums[i-3] + scores[i-3]:
                        numSkip2 = nums[i] - nums[i-3] + scores[i-3]
            else:
                numSkip2 = 0
            scores[i] = max( scores[i], numSkip1, numSkip2 )
            if scores[i] == numSkip1 or scores[i] == numSkip2:
                fromPrev[i] = True

            if scores[i] > maxScore:
                maxScore = scores[i]
        return maxScore


