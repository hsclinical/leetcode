from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        outCount = 0

        sumVal = 0
        sumDict = {}
        for num in nums:
            sumVal += num
            if sumVal == k:
                outCount += 1
            if sumVal - k in sumDict:
                outCount += sumDict[ sumVal - k ]

            if sumVal in sumDict:
                sumDict[ sumVal ] += 1
            else:
                sumDict[ sumVal ] = 1

        return outCount