from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        heightLen = len(height)
        if heightLen <= 1:
            return 0
        else:
            idxBgn = 0
            idxEnd = heightLen - 1
            lowHeight = min(height[idxBgn], height[idxEnd])
            outNum = (idxEnd - idxBgn) * lowHeight
            if height[idxBgn] < height[idxEnd]:
                ori = "toR"
            else:
                ori = "toL"

            while True:
                if idxBgn >= idxEnd:
                    break
                if ori == "toR":
                    idxBgn += 1
                    if height[idxBgn] > lowHeight:
                        if height[idxBgn] > height[idxEnd]:
                            lowHeight = height[idxEnd]
                            ori = "toL"
                        else:
                            lowHeight = height[idxBgn]

                        curNum = (idxEnd - idxBgn) * lowHeight
                        if curNum > outNum:
                            outNum = curNum
                else:
                    idxEnd -= 1
                    if height[idxEnd] > lowHeight:
                        if height[idxBgn] > height[idxEnd]:
                            lowHeight = height[idxEnd]
                        else:
                            lowHeight = height[idxBgn]
                            ori = "toR"

                        curNum = (idxEnd - idxBgn) * lowHeight
                        if curNum > outNum:
                            outNum = curNum
            return outNum
