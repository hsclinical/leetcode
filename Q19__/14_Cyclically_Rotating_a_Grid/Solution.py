from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        yLen = len(grid)
        xLen = len(grid[0])
        layerNum = min( xLen//2, yLen//2 )
        gridOut = [ [0] * xLen for _ in range(yLen) ]
        for i in range(layerNum):
            cellList = []
            for j in range(i, yLen-i):
                if (i, j) not in cellList:
                    cellList.append( (i, j) )
            for j in range(i, xLen-i):
                if (j, yLen-1-i) not in cellList:
                    cellList.append( (j, yLen-1-i) )
            for j in range(yLen-i-1, i-1, -1):
                if (xLen-1-i, j) not in cellList:
                    cellList.append( (xLen-1-i, j) )
            for j in range(xLen-i-1, i-1, -1):
                if (j, i) not in cellList:
                    cellList.append( (j, i) )

            print(layerNum, i, cellList)
            curK = k % len(cellList)
            if curK != 0:
                newList = cellList[-curK:] + cellList[:-curK]
                for j in range(len(cellList)):
                    gridOut[ cellList[j][1] ][ cellList[j][0] ] = grid[ newList[j][1] ][ newList[j][0] ]
            else:
                for j in range(len(cellList)):
                    gridOut[ cellList[j][1] ][ cellList[j][0] ] = grid[ cellList[j][1] ][ cellList[j][0] ]
        return gridOut