from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        self.numToIdx = {}
        for i in range(len(nums)):
            if nums[i] not in self.numToIdx:
                self.numToIdx[ nums[i] ] = []
            self.numToIdx[ nums[i] ].append(i)
        sortedNums = sorted(set(nums))

        numList = [ ]
        longestLen = 0
        for i in range(len(sortedNums)):
            if i == 0:
                numList.append( sortedNums[0] )
            else:
                if sortedNums[i] - numList[0] <= limit:
                    numList.append( sortedNums[i] )
                else:
                    currentLen = self.checkLength(numList)
                    if currentLen > longestLen:
                        longestLen = currentLen
                    numList.append( sortedNums[i] )
                    while True:
                        numList.pop(0)
                        if sortedNums[i] - numList[0] <= limit:
                            break

        currentLen = self.checkLength(numList)
        if currentLen > longestLen:
            longestLen = currentLen

        return longestLen

    def checkLength(self, numList):
        print("A", numList)
        idxList = []
        for num in numList:
            idxList += self.numToIdx[ num ]
        idxList.sort()
        print("B", idxList)
        longestLen = 0
        for i in range(len(idxList)):
            if i == 0:
                lastVal = idxList[0]
                curLen = 1
            else:
                if idxList[i] == lastVal + 1:
                    lastVal += 1
                    curLen += 1
                else:
                    if curLen > longestLen:
                        longestLen = curLen
                    lastVal = idxList[i]
                    curLen = 1

        if curLen > longestLen:
            longestLen = curLen
        return longestLen
