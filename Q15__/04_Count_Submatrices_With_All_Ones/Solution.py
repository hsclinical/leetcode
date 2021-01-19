from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rowLen = len(mat)
        colLen = len(mat[0])

        medium = [ [0] * colLen for _ in range(rowLen) ]
        #stack to bottom
        for j in range(colLen):
            for i in range(rowLen):
                if mat[i][j] == 1:
                    if i == 0 or mat[i-1][j] == 0:
                        medium[i][j] = 1
                    else:
                        medium[i][j] = medium[i-1][j] + 1

        #print(medium)
        result = [ [0] * colLen for _ in range(rowLen) ]
        total = 0
        for i in range(rowLen):
            for j in range(colLen):
                if mat[i][j] == 1:
                    cellTotal = medium[i][j]
                    # backward column
                    minStack = cellTotal
                    for k in range(j-1, -1, -1):
                        if mat[i][k] == 0:
                            break
                        else:
                            minStack = min(minStack, medium[i][k])
                            cellTotal += minStack
                    total += cellTotal
                    result[i][j] = cellTotal
        #print(result)
        return total