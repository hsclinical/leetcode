from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        yLen = len(board)
        if yLen == 0 or click[0] >= yLen:
            print("Error in input yLen (" + yLen + "), click[0] ( " + click[0] + ")")
            sys.exit(1)
        xLen = len(board[0])
        if xLen == 0 or click[1] >= xLen:
            print("Error in input xLen (" + xLen + "), click[1] ( " + click[1] + ")")
            sys.exit(1)

        if board[ click[0] ][ click[1] ] == 'M':
            board[ click[0] ][ click[1] ] = 'X'
            return board
        else:
            cells= ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
            self.searchBoard(board, yLen, xLen, cells, click)
            return board

    def searchBoard(self, board, yLen, xLen, cells, click):
        count = 0
        for cell in cells:
            yIdx = cell[0] + click[0]
            xIdx = cell[1] + click[1]
            if yIdx >= 0 and yIdx < yLen and xIdx >= 0 and xIdx < xLen and (board[yIdx][xIdx] == 'M' or board[yIdx][xIdx] == 'X'):
                count += 1
        if count != 0:
            board[ click[0] ][ click[1] ] = str(count)
        else:
            board[ click[0] ][ click[1] ] = 'B'
            for cell in cells:
                yIdx = cell[0] + click[0]
                xIdx = cell[1] + click[1]
                if yIdx >= 0 and yIdx < yLen and xIdx >= 0 and xIdx < xLen and board[yIdx][xIdx] == 'E':
                    self.searchBoard(board, yLen, xLen, cells, [yIdx, xIdx])

