from typing import List

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        yLen = len(A)
        xLen = len(A[0])

        if yLen == 1:
            return min(A[0])
        elif xLen == 1:
            return min([ i[0] for i in A ])
        else:
            confirmed = {}
            visited = {}

            neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            confirmed[ (0, 0) ] = A[0][0]
            visited[ (0, 1) ] = min( A[0][0], A[0][1] )
            visited[ (1, 0) ] = min( A[0][0], A[1][0] )
            while True:
                maxVisitedVal = max(visited.values())
                maxCellList = [ i for i in visited if visited[i] == maxVisitedVal ]
                for maxCell in maxCellList:
                    confirmed[ maxCell ] = visited[ maxCell ]
                    del visited[ maxCell ]
                    self.scanNeighbour(A, yLen, xLen, confirmed, visited, neighbours, maxCell, maxVisitedVal)

                if (yLen-1, xLen-1) in confirmed:
                    return confirmed[ (yLen-1, xLen-1) ]

    def scanNeighbour(self, A, yLen, xLen, confirmed, visited, neighbours, curCell, curValue):
        for neighbour in neighbours:
            y = curCell[0] + neighbour[0]
            x = curCell[1] + neighbour[1]
            if y >= 0 and y < yLen and x >= 0 and x < xLen and (y, x) not in confirmed:
                if A[y][x] >= curValue:
                    confirmed[ (y, x) ] = curValue
                    self.scanNeighbour(A, yLen, xLen, confirmed, visited, neighbours, (y, x), curValue)
                else:
                    if (y, x) not in visited or visited[ (y, x) ] < A[y][x]:
                        visited[ (y, x) ] = A[y][x]


