from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        else:
            monoIncrease = True
            lastNum = nums[-1]
            numsLen = len(nums)
            swiftIdx = 0
            for i in range(numsLen-2, -1, -1):
                if nums[i] < lastNum:
                    swiftIdx = i
                    monoIncrease = False
                    break
                lastNum = nums[i]
            if not monoIncrease:
                for i in range(numsLen-1, -1, -1):
                    if nums[i] > nums[swiftIdx]:
                        tmp = nums[swiftIdx]
                        nums[swiftIdx] = nums[i]
                        nums[i] = tmp
                        break
                swiftIdx += 1
            # v1.0.0: sort List
            #self.sortList(nums, numsLen, swiftIdx)
            
            # v2.0.0: the List is in decreasing order. Just reverse the List
            centerIdx = (swiftIdx + numsLen - 1 + 1) // 2
            for i in range(swiftIdx, centerIdx):
                tmp = nums[i]
                nums[i] = nums[numsLen - 1 - (i - swiftIdx)]
                nums[numsLen - 1 - (i - swiftIdx)] = tmp

            return nums

    '''
    def sortList(self, nums, numsLen, bgnIdx):
        for i in range(bgnIdx, numsLen-1):
            for j in range(i+1, numsLen):
                if nums[i] > nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
    '''
