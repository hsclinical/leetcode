from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        yLen = len(rooms)
        xLen = len(rooms[0])

        currentCell = []
        for y in range(yLen):
            for x in range(xLen):
                if rooms[y][x] == 0:
                    currentCell.append( (y, x) )

        if len(currentCell) == 0:
            return rooms

        cnt = 0
        neighbours = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
        while True:
            nextCell = []
            cnt += 1
            for cell in currentCell:
                for neighbour in neighbours:
                    ny = cell[0] + neighbour[0]
                    nx = cell[1] + neighbour[1]
                    if ny >= 0 and ny < yLen and nx >= 0 and nx < xLen and rooms[ny][nx] == 2147483647:
                        nextCell.append( (ny, nx) )
                        rooms[ny][nx] = cnt
            if len(nextCell) == 0:
                break
            else:
                currentCell = nextCell
        print(rooms)