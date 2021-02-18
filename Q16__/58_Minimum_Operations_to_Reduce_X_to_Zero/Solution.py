from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        numSum = sum(nums)
        if numSum < x:
            return -1
        elif numSum == x:
            return len(nums)
        else:
            numSum = 0
            idxLeft = 0
            for i, num in enumerate(nums):
                numSum += num
                if numSum >= x:
                    idxLeft = i
                    break
            idxRight = 0

            minLen = -1
            searchComplete = False
            while True:
                if numSum == x:
                    curLen = (idxLeft + 1) + (0 - idxRight)
                    if minLen == -1 or minLen > curLen:
                        minLen = curLen
                    idxRight -= 1
                    numSum += nums[ idxRight ]
                elif numSum > x:
                    if idxLeft == -1:
                        searchComplete = True
                        break
                    else:
                        numSum -= nums[ idxLeft ]
                        idxLeft -= 1
                else:
                    idxRight -= 1
                    numSum += nums[ idxRight ]

                if searchComplete:
                    break

            return minLen