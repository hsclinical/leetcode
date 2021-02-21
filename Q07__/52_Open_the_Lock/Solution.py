from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        elif '0000' in deadends:
            return -1

        deadendN = set()
        for deadend in deadends:
            deadendN.add( (int(deadend[0]), int(deadend[1]), int(deadend[2]), int(deadend[3])) )

        targetN = (int(target[0]), int(target[1]), int(target[2]), int(target[3]))

        cnt = 0
        currentN = [ (0, 0, 0, 0) ]
        visitedN = set()
        neighbours = [ (1, 0, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0), (0, -1, 0, 0), (0, 0, 1, 0), (0, 0, -1, 0), (0, 0, 0, 1), (0, 0, 0, -1) ]
        found = False
        while True:
            nextN = []
            for cell in currentN:
                for neighbour in neighbours:
                    u = (cell[0] + neighbour[0]) % 10
                    v = (cell[1] + neighbour[1]) % 10
                    w = (cell[2] + neighbour[2]) % 10
                    x = (cell[3] + neighbour[3]) % 10
                    nextCell = (u, v, w, x)
                    if nextCell not in deadendN and nextCell not in visitedN:
                        nextN.append( nextCell )
                        visitedN.add( nextCell )
                        if nextCell == targetN:
                            found = True
                            break
            if len(nextN) == 0:
                break
            elif found:
                cnt += 1
                break
            else:
                cnt += 1
                currentN = nextN
        if found:
            return cnt
        else:
            return -1
