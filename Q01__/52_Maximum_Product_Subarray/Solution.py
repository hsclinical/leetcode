from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        finalProd = nums[0]
        # here we record max and min in case there is a negative number to flip
        maxProd = nums[0]
        minProd = nums[0]
        for i, num in enumerate(nums):
            if i != 0:
                if num > 0:
                    # to-do
                    maxProd = max(maxProd * num, num)
                    finalProd = max(finalProd, maxProd)

                    minProd = min(minProd * num, num)
                else:
                    tmp1 = max(minProd * num, num)
                    tmp2 = min(maxProd * num, num)
                    finalProd = max(finalProd, tmp1)
                    maxProd = tmp1
                    minProd = tmp2
        return finalProd