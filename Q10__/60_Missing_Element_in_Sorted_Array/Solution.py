from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # the most straight forward way is to start with [0], add 1 each time, if in list, skip
        # the complexity is O(n). Not efficient
        # It's sorted array, should be O(logn)
        # to find index i that nums[i] + 1 = ? and nums[i+1] > ? (? is the missing number)

        spaceInRange = nums[-1] - nums[0] - len(nums) + 1
        if spaceInRange < k:
            return (k - spaceInRange) + nums[-1]
        else:
            return self.findIndex(nums, k, 0, len(nums)-1)

    def findIndex(self, nums, k, indexBgn, indexEnd):
        indexMed = (indexBgn + indexEnd)//2
        spaceInRange = nums[indexMed] - nums[0] - indexMed
        if spaceInRange < k:
            out = (k - spaceInRange) + nums[indexMed]
            if out > nums[indexMed + 1]:
                return self.findIndex(nums, k, indexMed, indexEnd)
            else:
                return out
        else:
            return self.findIndex(nums, k, indexBgn, indexMed)
