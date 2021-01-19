from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        medium = [ [0] * n for i in range(m) ]
        for i, row in enumerate(mat):
            for j, cell in enumerate(mat[i]):
                bgnIdx = max(0, j - K)
                endIdx = min(n-1, j + K)
                medium[i][j] = sum(mat[i][bgnIdx:(endIdx+1)])

        #print(medium)
        outList = [ [0] * n for i in range(m) ]
        for j in range(n):
            for i in range(m):
                bgnIdx = max(0, i - K)
                endIdx = min(m-1, i + K)
                #print(i, j, bgnIdx, endIdx, [medium[x][j] for x in range(bgnIdx,endIdx)])
                outList[i][j] = sum([medium[x][j] for x in range(bgnIdx,(endIdx+1))])

        return outList