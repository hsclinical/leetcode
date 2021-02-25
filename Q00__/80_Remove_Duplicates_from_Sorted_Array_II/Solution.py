from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numLen = len(nums)
        if numLen <= 2:
            return numLen

        dupicateCnt = 0
        lastNumType = None
        lastNumCount = 0
        for i in range(numLen):
            if i > numLen - 1 - dupicateCnt:
                break

            if lastNumType == None:
                lastNumType = nums[i]
                lastNumCount = 1
            else:
                if nums[i] == lastNumType:
                    lastNumCount += 1
                    if lastNumCount == 2:
                        offset = 0
                        curDupicateCnt = dupicateCnt
                        for j in range(i+1, numLen-curDupicateCnt):
                            if nums[j] == nums[i]:
                                offset += 1
                                dupicateCnt += 1
                            else:
                                if offset == 0:
                                    break
                                else:
                                    nums[j-offset] = nums[j]
                else:
                    lastNumType = nums[i]
                    lastNumCount = 1

        return numLen - dupicateCnt