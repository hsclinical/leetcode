from typing import List

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        # (horizontal, vertical, diagonal or anti-diagonal)
        self.iMax = len(M) - 1
        if self.iMax == -1:
            return 0

        self.jMax = len(M[0]) - 1
        self.S = []
        longestLen = 0
        for i in range(len(M)):
            row = []
            self.S.append(row)
            for j in range(len(M[0])):
                if M[i][j] == 0:
                    row.append( (0, 0, 0, 0) )
                else:
                    num1 = self.checkCell(M, i, j-1, 0) # horizontal
                    num2 = self.checkCell(M, i-1, j, 1) # vertical
                    num3 = self.checkCell(M, i-1, j-1, 2) # diagonal
                    num4 = self.checkCell(M, i-1, j+1, 3) # anti-diagonal

                    cellVal = (num1, num2, num3, num4)
                    row.append( cellVal )
                    if longestLen < max(cellVal):
                        longestLen = max(cellVal)
        return longestLen


    def checkCell(self, M, x, y, idx):
        if (x >= 0 and x <= self.iMax) and (y >= 0 and y <= self.jMax):
            return self.S[x][y][idx] + 1
        else:
            return 1

