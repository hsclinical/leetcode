from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        yLen = len(board)
        if yLen <= 2:
            return board

        xLen = len(board[0])
        if xLen <= 2:
            return board

        medium = [ [0] * xLen for _ in range(yLen) ]
        uniqueId = 1
        idToCellList = {} # id -> [ list of cells ]
        idNextToEnd = {}  # id -> True/False

        for y in range(yLen):
            for x in range(xLen):
                if board[y][x] == 'O':
                    if y == 0 and x == 0:
                        medium[y][x] = uniqueId
                        uniqueId += 1
                        idNextToEnd[ medium[y][x] ] = True
                        idToCellList[ medium[y][x] ] = [ (y, x) ]
                    elif y == 0:
                        if medium[y][x-1] != 0:
                            medium[y][x] = medium[y][x-1]
                            idToCellList[ medium[y][x] ].append( (y, x) )
                        else:
                            medium[y][x] = uniqueId
                            uniqueId += 1
                            idNextToEnd[ medium[y][x] ] = True
                            idToCellList[ medium[y][x] ] = [ (y, x) ]
                    elif x == 0:
                        if medium[y-1][x] != 0:
                            medium[y][x] = medium[y-1][x]
                            idToCellList[ medium[y][x] ].append( (y, x) )
                        else:
                            medium[y][x] = uniqueId
                            uniqueId += 1
                            idNextToEnd[ medium[y][x] ] = True
                            idToCellList[ medium[y][x] ] = [ (y, x) ]
                    else:
                        if medium[y-1][x] == 0 and medium[y][x-1] == 0:
                            medium[y][x] = uniqueId
                            uniqueId += 1
                            idNextToEnd[ medium[y][x] ] = False
                            idToCellList[ medium[y][x] ] = [ (y, x) ]
                        elif medium[y-1][x] != 0 and medium[y][x-1] != 0 and medium[y-1][x] != medium[y][x-1]:
                            # merge the larger uniqueId into the smaller one
                            smallerIdx = min(medium[y-1][x], medium[y][x-1])
                            largerIdx = max(medium[y-1][x], medium[y][x-1])
                            idNextToEnd[ smallerIdx ] = idNextToEnd[ smallerIdx ] or idNextToEnd[ largerIdx ]
                            for (j, i) in idToCellList[ largerIdx ]:
                                medium[j][i] = smallerIdx
                            idToCellList[ smallerIdx ] += idToCellList[ largerIdx ]
                            del idNextToEnd[ largerIdx ]
                            del idToCellList[ largerIdx ]

                            medium[y][x] = smallerIdx
                            idToCellList[ medium[y][x] ].append( (y, x) )
                        else:
                            # one is zero, the other is non-zero
                            medium[y][x] = max(medium[y][x-1], medium[y-1][x])
                            idToCellList[ medium[y][x] ].append( (y, x) )

                        if y == yLen-1 or x == xLen-1:
                            idNextToEnd[ medium[y][x] ] = True

        for idx in idNextToEnd:
            if not idNextToEnd[ idx ]:
                for (y, x) in idToCellList[ idx ]:
                    board[y][x] = 'X'

        return board