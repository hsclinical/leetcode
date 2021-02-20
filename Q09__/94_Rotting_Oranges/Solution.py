from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        yLen = len(grid)
        xLen = len(grid[0])

        fresh = set()
        rotten = set()
        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == 1:
                    fresh.add( (y, x) )
                elif grid[y][x] == 2:
                    rotten.add( (y, x) )

        if len(fresh) == 0:
            return 0
        elif len(rotten) == 0:
            return -1

        neighbours = [ (1, 0), (0, 1), (-1, 0), (0, -1) ]
        curRotten = list(rotten)
        cnt = 0
        while True:
            nextRotten = []
            for cell in curRotten:
                for neighbour in neighbours:
                    y = cell[0] + neighbour[0]
                    x = cell[1] + neighbour[1]
                    if y >= 0 and y < yLen and x >= 0 and x < xLen:
                        if grid[y][x] == 1:
                            grid[y][x] = 2
                            nextRotten.append( (y, x) )
                            fresh.remove( (y, x) )

            if len(nextRotten) == 0:
                break
            else:
                cnt += 1
                curRotten = nextRotten

        if len(fresh) == 0:
            return cnt
        else:
            return -1
