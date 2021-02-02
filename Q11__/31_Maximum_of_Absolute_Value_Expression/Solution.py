from typing import List

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        # v1.0.0: O(n**2)
        arrLen = len(arr1)
        maxNum = 0
        for i in range(arrLen-1):
            for j in range(i+1, arrLen):
                curNum = abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j)
                if curNum > maxNum:
                    maxNum = curNum
        return maxNum
        '''

        '''
        # v1.1.0: O(n**2)
        arrLen = len(arr1)
        maxNum = 0
        for i, num in enumerate(arr1[:-1]):
            curMax = max( [ (abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j)) for j in range(i+1, arrLen) ] )
            maxNum = max(curMax, maxNum)
        return maxNum
        '''

        scores = []
        for i, (x, y) in enumerate(zip(arr1, arr2)):
            scores.append( (i+x+y, i+x-y, i-x+y, i-x-y) )
        # zip each column into a list
        medium = [max(score) - min(score) for score in zip(*scores)]
        return max(medium)
