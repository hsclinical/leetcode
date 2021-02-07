from typing import List

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        yLen = len(A)
        xLen = len(A[0])

        yCur, xCur = self.findCell(A, yLen, xLen, 1)
        self.changeValue(A, yLen, xLen, yCur, xCur, 1, -1)

        curVal = 1
        curList = self.findCellList(A, yLen, xLen, curVal)
        found = False
        while True:
            nextList = []
            for (yCur, xCur) in curList:
                cells = [(yCur - 1, xCur), (yCur, xCur - 1), (yCur + 1, xCur), (yCur, xCur + 1)]
                for cell in cells:
                    if cell[0] >= 0 and cell[0] <= yLen - 1 and cell[1] >= 0 and cell[1] <= xLen - 1:
                        if A[ cell[0] ][ cell[1] ] == -1:
                            # break
                            found = True
                            break
                        elif A[ cell[0] ][ cell[1] ] == 0:
                            # update
                            A[ cell[0] ][ cell[1] ] = curVal + 1
                            nextList.append( (cell[0], cell[1]) )
                        else:
                            pass
                if found:
                    break
            if found:
                break
            else:
                curList = nextList
                curVal += 1

        return curVal - 1


    def findCell(self, A, yLen, xLen, valToFind):
        found = False
        for y in range(yLen):
            for x in range(xLen):
                if A[y][x] == valToFind:
                    cell = (y, x)
                    found = True
                    break
            if found:
                break
        return cell[0], cell[1]


    def findCellList(self, A, yLen, xLen, valToFind):
        cellList = []
        for y in range(yLen):
            for x in range(xLen):
                if A[y][x] == valToFind:
                    cellList.append( (y, x) )
                    cell = (y, x)
        return cellList

    def changeValue(self, A, yLen, xLen, yCur, xCur, curVal, nextVal):
        A[yCur][xCur] = nextVal
        cells = [(yCur - 1, xCur), (yCur, xCur - 1), (yCur + 1, xCur), (yCur, xCur + 1)]
        for cell in cells:
            if cell[0] >= 0 and cell[0] <= yLen - 1 and cell[1] >= 0 and cell[1] <= xLen - 1 and A[ cell[0] ][ cell[1] ] == curVal:
                self.changeValue(A, yLen, xLen, cell[0], cell[1], curVal, nextVal)
