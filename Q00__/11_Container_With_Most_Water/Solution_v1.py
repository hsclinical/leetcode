from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        heightLen = len(height)
        if heightLen <= 1:
            return 0
        else:
            outNum = 0
            candidateLeft = []
            candidateRight = []
            curMaxLeft = 0
            curMaxRight = 0

            for i in range(heightLen-1):
                if height[i] > curMaxLeft:
                    curMaxLeft = height[i]
                    candidateLeft.append(i)
                if height[len(height)-i-1] > curMaxRight:
                    curMaxRight = height[len(height)-i-1]
                    candidateRight.append(len(height)-i-1)
            candidateRight.reverse()

            for i in candidateLeft:
                for j in [x for x in candidateRight if x > i]:
                    curNum = (j-i) * min(height[j], height[i])
                    if curNum > outNum:
                        outNum = curNum
            return outNum
