from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numLen = len(nums)
        for i in range(numLen):
            while True:
                if nums[i] == i + 1:
                    break
                else:
                    if nums[ nums[i] - 1 ] == nums[i]:
                        return nums[i]
                    else:
                        tmp = nums[ nums[i] - 1 ]
                        nums[ nums[i] - 1 ] = nums[i]
                        nums[i] = tmp
