from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0:
            return False
        else:
            return self.findConsecutiveNumber(nums, k)

    def findConsecutiveNumber(self, nums, k):
        indexListAsc = []
        indexListDesc = []
        foundAllAsc  = True
        foundAllDesc = True
        for i in range(k):
            if i == 0:
                startNum = nums[0]
                lastIdxAsc = 0
                lastIdxDesc = 0
                indexListAsc.append(0)
                indexListDesc.append(0)
            else:
                if foundAllAsc:
                    idx = nums.index(startNum+i, lastIdxAsc+1) if (startNum+i) in nums[lastIdxAsc+1:] else -1
                    if idx == -1:
                        foundAllAsc = False
                    else:
                        lastIdxAsc = idx
                        indexListAsc.append(idx)
                if foundAllDesc:
                    idx = nums.index(startNum-i, lastIdxDesc+1) if (startNum-i) in nums[lastIdxDesc+1:] else -1
                    if idx == -1:
                        foundAllDesc = False
                    else:
                        lastIdxDesc = idx
                        indexListDesc.append(idx)
                if (not foundAllAsc) and (not foundAllDesc):
                    break

        if foundAllAsc and foundAllDesc:
            indexListAsc = list(reversed(indexListAsc))
            newNumsAsc = nums[:]
            for i in range(len(indexListAsc)):
                newNumsAsc.pop(indexListAsc[i])

            indexListDesc = list(reversed(indexListDesc))
            newNumsDesc = nums[:]
            for i in range(len(indexListDesc)):
                newNumsDesc.pop(indexListDesc[i])

            if len(newNumsAsc) == 0 or len(newNumsDesc):
                return True
            else:
                return self.findConsecutiveNumber(newNumsAsc,k) or self.findConsecutiveNumber(newNumsDesc,k)
        elif foundAllAsc:
            indexListAsc = list(reversed(indexListAsc))
            newNums = nums[:]
            for i in range(len(indexListAsc)):
                newNums.pop(indexListAsc[i])
            if len(newNums) == 0:
                return True
            else:
                return self.findConsecutiveNumber(newNums,k)
        elif foundAllDesc:
            indexListDesc = list(reversed(indexListDesc))
            newNums = nums[:]
            for i in range(len(indexListDesc)):
                newNums.pop(indexListDesc[i])
            if len(newNums) == 0:
                return True
            else:
                return self.findConsecutiveNumber(newNums,k)
        else:
            return False