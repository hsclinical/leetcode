class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        yLen = len(grid)
        xLen = yLen

        foundWater = False
        foundLand = False
        visited = set()
        curList = []
        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == 1:
                    visited.add( (y, x) )
                    curList.append( (y, x) )
                    foundLand = True
                else:
                    foundWater = True

        if foundWater and foundLand:
            nextCoords = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
            curStep = 0
            while True:
                nextList = []
                for curCell in curList:
                    for nextCoord in nextCoords:
                        nextCellY = curCell[0] + nextCoord[0]
                        nextCellX = curCell[1] + nextCoord[1]
                        if nextCellY >= 0 and nextCellY < yLen and nextCellX >= 0 and nextCellX < xLen and (nextCellY, nextCellX) not in visited:
                            visited.add( (nextCellY, nextCellX) )
                            nextList.append( (nextCellY, nextCellX) )
                if len(nextList) == 0:
                    break
                else:
                    curList = nextList
                    curStep += 1
            return curStep
        else:
            return -1