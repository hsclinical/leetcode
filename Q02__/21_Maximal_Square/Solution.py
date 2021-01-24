from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)    # row
        n = len(matrix[0]) # col

        found = False
        medium = [ [0] * n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    found = True
                    if i == 0:
                        medium[i][j] = 1
                    else:
                        medium[i][j] = medium[i-1][j] + 1

        if found:
            maxLen = 1
            for i in range(m):
                for j in range(n):
                    if medium[i][j] > maxLen and j >= maxLen:
                        bgnIdx = j - medium[i][j]
                        if bgnIdx < -1:
                            bgnIdx = -1
                        curMin = medium[i][j]
                        curLen = 1
                        for k in range(j-1, bgnIdx, -1):
                            curMin = min(curMin, medium[i][k])
                            if curMin <= maxLen:
                                break
                            else:
                                curLen = min(curMin, j-k+1)
                                if curLen > maxLen:
                                    maxLen = curLen
            return maxLen * maxLen
        else:
            return 0