from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        countToVal = {}
        firstNum = True
        for i in reversed(range(len(nums))):
            if firstNum:
                countToVal[1] = nums[i]
                firstNum = False
            else:
                if nums[i] < countToVal[1]:
                    if 2 in countToVal:
                        if nums[i] < countToVal[2]:
                            return True
                        else:
                            countToVal[2] = nums[i]
                    else:
                        countToVal[2] = nums[i]
                else:
                    countToVal[1] = nums[i]
        return False