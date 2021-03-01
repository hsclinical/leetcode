from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        numsLen = len(nums)
        outList = self.getAllCombination(nums, numsLen, 0)
        return outList

    def getAllCombination(self, nums, numsLen, idx):
        if idx == numsLen - 1:
            return [ [], [ nums[idx] ] ]
        else:
            outList = []
            curList = [ [], [ nums[idx] ] ]
            prevList = self.getAllCombination(nums, numsLen, idx + 1)
            for curElem in curList:
                for prevElem in prevList:
                    outList.append( curElem + prevElem )
            return outList
