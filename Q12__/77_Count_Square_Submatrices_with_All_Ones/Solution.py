from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        yDim = len(matrix)
        xDim = len(matrix[0])
        self.visitedSquare = set() # y, x, len
        for y in range(yDim):
            for x in range(xDim):
                if matrix[y][x] == 1:
                    self.visitedSquare.add( (y, x, 1) )
                    self.checkSquare(matrix, y, x, yDim, xDim)

        return len(self.visitedSquare)

    def checkSquare(self, matrix, y, x, yDim, xDim):
        curLen = 2
        while True:
            if (y, x, curLen) in self.visitedSquare:
                curLen += 1
                continue
            else:
                successAddOne = True
                if y+curLen > yDim or x+curLen > xDim:
                    successAddOne = False
                    break
                if successAddOne:
                    for i in range(curLen):
                        if matrix[y+(curLen-1)][x+i] == 1:
                            self.visitedSquare.add( (y+(curLen-1), x+i, 1) )
                        else:
                            successAddOne = False
                            break
                if successAddOne:
                    for i in range(curLen-1):
                        if matrix[y+i][x+(curLen-1)] == 1:
                            self.visitedSquare.add( (y+i, x+(curLen-1), 1) )
                        else:
                            successAddOne = False
                            break
                if successAddOne:
                    self.addNewSquareToSet(y, x, curLen)
                    curLen += 1
                else:
                    break

    def addNewSquareToSet(self, y, x, curLen):
        for i in range(curLen-1):
            if i == 0:
                self.visitedSquare.add( (y, x, curLen) )
            else:
                self.visitedSquare.add( (y+i, x+i, curLen-i) )
                for j in range(i):
                    self.visitedSquare.add( (y+j, x+i, curLen-i) )
                    self.visitedSquare.add( (y+i, x+j, curLen-i) )
