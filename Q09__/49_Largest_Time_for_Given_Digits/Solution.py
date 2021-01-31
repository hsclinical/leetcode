from typing import List
from functools import lru_cache

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arrLen = len(arr)
        arr = sorted(arr, reverse=True)
        hPrefixIdx = []
        for i in range(arrLen):
            if arr[i] <= 2:
                hPrefixIdx.append(i)

        if len(hPrefixIdx) == 0:
            return ""
        else:
            outcome = ""
            found = False
            lastHHInt = 0
            lastMMInt = 0
            # nums are sorted from the largest to the smallest
            for i in hPrefixIdx:
                for j in range(arrLen):
                    if i != j:
                        num1Int = arr[i] * 10 + arr[j]
                        num1Str = str(arr[i]) + str(arr[j])
                        num2Int = arr[j] * 10 + arr[i]
                        num2Str = str(arr[j]) + str(arr[i])

                        if num1Int <= 23:
                            isValid, minInt, minStr = self.checkMin(tuple(arr), arrLen, i, j)
                            if isValid:
                                if num1Int >= lastHHInt and minInt >= lastMMInt:
                                    outcome = num1Str + ':' + minStr
                                    found = True
                                    break

                        if num2Int <= 23:
                            isValid, minInt, minStr = self.checkMin(tuple(arr), arrLen, i, j)
                            if isValid:
                                if num2Int >= lastHHInt and minInt >= lastMMInt:
                                    lastHHInt = num2Int
                                    lastMMInt = minInt
                                    outcome = num2Str + ':' + minStr
                if found == True:
                    break
            return outcome

    @lru_cache(maxsize=None)
    def checkMin(self, arr, arrLen, num1, num2):
        outList = []
        for i in range(arrLen):
            if i != num1 and i != num2:
                outList.append(arr[i])
        
        left1Int = outList[0] * 10 + outList[1]
        left1Str = str(outList[0]) + str(outList[1])
        left2Int = outList[1] * 10 + outList[0]
        left2Str = str(outList[1]) + str(outList[0])
        if left1Int <= 59:
            return True, left1Int, left1Str
        elif left2Int <= 59:
            return True, left2Int, left2Str
        else:
            return False, 0, ""

