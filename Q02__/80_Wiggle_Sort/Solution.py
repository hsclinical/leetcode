from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        if numsLen == 2:
            if nums[0] > nums[1]:
                tmp = nums[0]
                nums[0] = nums[1]
                nums[1] = tmp
        elif numsLen >= 3:
            sortedNums = sorted(nums)
            if numsLen % 2 == 0:
                mediumNum = (sortedNums[ (numsLen // 2) - 1 ] + sortedNums[ (numsLen // 2) ])/2
            else:
                mediumNum = sortedNums[ (numsLen // 2) ]

            smallIdx = [ i for i in range(numsLen) if (i % 2 == 0) and (nums[i] >= mediumNum) ]
            largeIdx = [ i for i in range(numsLen) if (i % 2 == 1) and (nums[i] <= mediumNum) ]

            smallIdxLen = len(smallIdx)
            largeIdxLen = len(largeIdx)
            if smallIdxLen < largeIdxLen:
                removeIdx = []
                for idx in largeIdx:
                    if nums[idx] == mediumNum:
                        removeIdx.append( idx )
                cntToRemove = largeIdxLen - smallIdxLen
                for i in range(cntToRemove):
                    largeIdx.remove( removeIdx[ i ] )
            elif smallIdxLen > largeIdxLen:
                removeIdx = []
                for idx in smallIdx:
                    if nums[idx] == mediumNum:
                        removeIdx.append( idx )
                cntToRemove = smallIdxLen - largeIdxLen
                for i in range(cntToRemove):
                    smallIdx.remove( removeIdx[ i ] )

            for i in range( len(smallIdx) ):
                tmp = nums[ smallIdx[i] ]
                nums[ smallIdx[i] ] = nums[ largeIdx[i] ]
                nums[ largeIdx[i] ] = tmp
