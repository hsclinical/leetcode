from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        yLen = len(grid)
        xLen = len(grid[0])

        maximumGold = 0
        nextDirections = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] != 0:
                    maximumGoldStartWithCell = self.getMaximumGoldStartWithCell( grid, nextDirections, yLen, xLen, (y, x), [ (y, x) ] )
                    if maximumGold < maximumGoldStartWithCell:
                        maximumGold = maximumGoldStartWithCell
        return maximumGold

    def getMaximumGoldStartWithCell(self, grid, nextDirections, yLen, xLen, cell, curPath):
        maximumGold = 0
        for nextDirection in nextDirections:
            nextY = cell[0] + nextDirection[0]
            nextX = cell[1] + nextDirection[1]
            if nextY >= 0 and nextY < yLen and nextX >= 0 and nextX < xLen and grid[nextY][nextX] != 0 and (nextY, nextX) not in curPath:
                nextPath = curPath[:] + [ (nextY, nextX) ]
                curMaximumGold = self.getMaximumGoldStartWithCell(grid, nextDirections, yLen, xLen, (nextY, nextX), nextPath)
                if curMaximumGold > maximumGold:
                    maximumGold = curMaximumGold
        return maximumGold + grid[ cell[0] ][ cell[1] ]
