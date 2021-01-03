from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totLen = len(nums)

        leftNum = 1
        rightNum = 1
        leftToRight = [ 1 ]
        rightToLeft = [ 1 ]
        for i in range(totLen-1):
            leftNum *= nums[i]
            rightNum *= nums[(-1)*i-1]
            leftToRight.append(leftNum)
            rightToLeft.append(rightNum)

        outList = []
        for i in range(totLen):
            outList.append( leftToRight[i] * rightToLeft[totLen-1-i])
        return outList

