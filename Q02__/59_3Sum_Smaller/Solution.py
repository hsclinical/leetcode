from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        numLen = len(nums)
        if numLen < 3:
            return 0
        elif numLen == 3:
            if sum(nums) < target:
                return 1
            else:
                return 0
        else:
            sortedNums = sorted(nums)
            totalCnt = 0
            for i in range(numLen-2):
                totalCnt += self.twoSumSmaller(sortedNums, i+1, target-sortedNums[i])
            return totalCnt

    def twoSumSmaller(self, nums, idxBgn, target):
        totalCnt = 0
        curBgn = idxBgn
        curEnd = len(nums) - 1
        while True:
            if curBgn == curEnd:
                break
            if nums[curBgn] + nums[curEnd] >= target:
                curEnd -= 1
            else:
                totalCnt += (curEnd - curBgn)
                curBgn += 1

        return totalCnt