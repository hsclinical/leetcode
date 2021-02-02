from typing import List

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        outList = []
        minXY = 1
        maxXY = 1000
        for x in range(minXY, (maxXY+1)):
            if customfunction.f(x, minXY) > z:
                break
            elif customfunction.f(x, maxXY) < z:
                continue
            else:
                found, y = self.findSolutionInRange(customfunction, z, x, minXY, maxXY)
                if found:
                    outList.append( [x, y] )
        return outList


    def findSolutionInRange(self, customfunction, z, x, yBgn, yEnd):
        if yEnd == yBgn:
            tmpZ = customfunction.f(x, yBgn)
            if tmpZ == z:
                return True, yBgn
            else:
                return False, 0
        elif yEnd - yBgn == 1:
            tmpZ1 = customfunction.f(x, yBgn)
            tmpZ2 = customfunction.f(x, yEnd)
            if tmpZ1 == z:
                return True, yBgn
            elif tmpZ2 == z:
                return True, yEnd
            else:
                return False, 0
        else:
            yAvg = (yBgn + yEnd) // 2
            tmpZ = customfunction.f(x, yAvg)
            if tmpZ == z:
                return True, yAvg
            elif tmpZ > z:
                return self.findSolutionInRange(customfunction, z, x, yBgn, yAvg-1)
            else:
                return self.findSolutionInRange(customfunction, z, x, yAvg+1, yEnd)
