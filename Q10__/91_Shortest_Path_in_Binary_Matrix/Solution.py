from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        elif n == 1:
            return 1

        matrix = [ [-1] * n for _ in range(n) ]
        neighbours = [ (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1) ]
        curCellList = [ (0, 0) ]
        matrix[0][0] = 1

        found = False
        stepCnt = 1
        while True:
            nextCellList = []
            for cell in curCellList:
                for neighbour in neighbours:
                    y = cell[0] + neighbour[0]
                    x = cell[1] + neighbour[1]
                    if y >= 0 and y <= n-1 and x >= 0 and x <= n -1:
                        if grid[y][x] == 0 and matrix[y][x] == -1:
                            nextCellList.append( (y, x) )
                            matrix[y][x] = matrix[ cell[0] ][ cell[1] ] + 1
                        if y == n-1 and x == n-1:
                            # reach the end
                            found = True
                            stepCnt = matrix[y][x]
                if found:
                    break
            if len(nextCellList) == 0:
                # unreachable
                break
            elif found:
                break
            else:
                curCellList = nextCellList

        if found:
            return stepCnt
        else:
            return -1



