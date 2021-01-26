from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        yDim = len(grid)
        xDim = len(grid[0])
        score = [ [0] * xDim for _ in range(yDim) ]
        for y in range(yDim):
            for x in range(xDim):
                if y == 0:
                    if x == 0:
                        score[y][x] = grid[y][x]
                    else:
                        score[y][x] = score[y][x-1] + grid[y][x]
                else:
                    if x == 0:
                        score[y][x] = score[y-1][x] + grid[y][x]
                    else:
                        score[y][x] = min(score[y][x-1], score[y-1][x]) + grid[y][x]
        return score[yDim-1][xDim-1]

