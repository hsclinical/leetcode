from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        yLen = len(matrix)
        if yLen == 0:
            return []
        elif yLen == 1:
            return [ [0, i] for i in range( len(matrix[0]) ) ]

        xLen = len(matrix[0])
        if xLen == 0:
            return []
        elif xLen == 1:
            return [ [i, 0] for i in range( yLen ) ]

        pStartList = [ (0, i) for i in range( xLen ) ] + [ (i, 0) for i in range( 1, yLen ) ]
        pVisited = set(pStartList)
        for pCurCell in pStartList:
            self.findCell(matrix, yLen, xLen, pVisited, pCurCell)

        aStartList = [ (yLen-1, i) for i in range( xLen ) ] + [ (i, xLen-1) for i in range( yLen - 1 ) ]
        aVisited = set(aStartList)
        for aCurCell in aStartList:
            self.findCell(matrix, yLen, xLen, aVisited, aCurCell)

        print(pVisited)
        print(aVisited)
        bothVisited = pVisited.intersection(aVisited)
        return [ list(i) for i in bothVisited ]

    def findCell(self, matrix, yLen, xLen, visited, curCell):
        flankCells = [ (curCell[0]-1, curCell[1]), (curCell[0], curCell[1]-1), (curCell[0]+1, curCell[1]), (curCell[0], curCell[1]+1) ]
        for flankCell in flankCells:
            if flankCell[0] >= 0 and flankCell[0] <= yLen - 1 and flankCell[1] >= 0 and flankCell[1] <= xLen - 1:
                if flankCell not in visited and matrix[ flankCell[0] ][ flankCell[1] ] >= matrix[ curCell[0] ][ curCell[1] ]:
                    visited.add(flankCell)
                    self.findCell(matrix, yLen, xLen, visited, flankCell)
