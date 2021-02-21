from typing import List
import bisect

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heightsLen = len(heights)
        heightsDiff = [ 0 ]
        for i in range(heightsLen-1):
            diff = max(heights[i+1] - heights[i], 0)
            heightsDiff.append( diff )

        goThrough = True
        sumBricks = 0
        heightsAdded = [ ]
        for i, diff in enumerate(heightsDiff):
            if i >= ladders:
                if ladders == 0:
                    sumBricks += diff
                else:
                    bisect.insort(heightsAdded, diff)
                    minHeight = heightsAdded.pop(0)
                    sumBricks += minHeight
                if sumBricks > bricks:
                    goThrough = False
                    break
            else:
                bisect.insort(heightsAdded, diff)
            maxStep = i

        if goThrough:
            maxStep = heightsLen - 1

        return maxStep
