from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        yLen = len(board)
        xLen = len(board[0])
        wordLen = len(word)
        directions = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

        found = False
        for y in range(yLen):
            for x in range(xLen):
                if board[y][x] == word[0]:
                    curSearch = self.searchWord(directions, board, yLen, xLen, word, wordLen, (y, x), 0, [ (y, x) ])
                    if curSearch:
                        found = True
                        break
        return found


    def searchWord(self, directions, board, yLen, xLen, word, wordLen, curCell, curIdx, curPath):
        if curIdx == wordLen-1:
            return True

        found = False
        for direction in directions:
            nextY = curCell[0] + direction[0]
            nextX = curCell[1] + direction[1]
            if nextY >= 0 and nextY < yLen and nextX >= 0 and nextX < xLen and (nextY, nextX) not in curPath and board[nextY][nextX] == word[curIdx+1]:
                nextPath = curPath[:] + [ (nextY, nextX) ]
                if self.searchWord(directions, board, yLen, xLen, word, wordLen, (nextY, nextX), curIdx+1, nextPath):
                    found = True
                    break

        return found
