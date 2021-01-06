from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        yDim = len(grid)
        xDim = len(grid[0])
        if yDim < 3 or xDim < 3:
            return 0
        else:
            outCount = 0
            for y in range(yDim-2):
                for x in range(xDim-2):
                    if grid[y+1][x+1] == 5:
                        if self.checkMagic(grid, y, x):
                            outCount += 1
            return outCount
    
    def checkMagic(self, grid, y, x):
        # check all 1-9 present
        isMagic = True
        numSet = set()
        for j in range(3):
            for i in range(3):
                if grid[y+j][x+i] >= 1 and grid[y+j][x+i] <= 9:
                    if grid[y+j][x+i] in numSet:
                        isMagic = False
                        break
                    else:
                        numSet.add(grid[y+j][x+i])
                else:
                    isMagic = False
                    break
            if not isMagic:
                break

        if isMagic:
            if grid[y  ][x  ] + grid[y  ][x+1] + grid[y  ][x+2] == 15 and \
               grid[y+1][x  ] + grid[y+1][x+1] + grid[y+1][x+2] == 15 and \
               grid[y+2][x  ] + grid[y+2][x+1] + grid[y+2][x+2] == 15 and \
               grid[y  ][x  ] + grid[y+1][x  ] + grid[y+2][x  ] == 15 and \
               grid[y  ][x+1] + grid[y+1][x+1] + grid[y+2][x+1] == 15 and \
               grid[y  ][x+2] + grid[y+1][x+2] + grid[y+2][x+2] == 15 and \
               grid[y  ][x  ] + grid[y+1][x+1] + grid[y+2][x+2] == 15 and \
               grid[y+2][x  ] + grid[y+1][x+1] + grid[y  ][x+2] == 15:
                   pass
            else:
                isMagic = False
        return isMagic