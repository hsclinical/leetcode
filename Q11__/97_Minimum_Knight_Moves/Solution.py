from typing import List

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0

        currentP = []
        visitedP = set()
        neighbours = [ (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1) ]
        currentP.append( (0, 0) )

        found = False
        cnt = 0
        while True:
            nextP = []
            for cell in currentP:
                for neighbour in neighbours:
                    ny = cell[0] + neighbour[0]
                    nx = cell[1] + neighbour[1]
                    if (ny, nx) not in visitedP:
                        visitedP.add( (ny, nx) )
                        nextP.append( (ny, nx) )
                    if y == ny and x == nx:
                        found = True
                        break
                if found:
                    break
            cnt += 1
            if found:
                break
            else:
                currentP = nextP
        return cnt
