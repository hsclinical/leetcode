from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        yLen = len(grid)
        xLen = len(grid[0])

        medium = [ [0] * xLen for _ in range(yLen) ]
        uniqueId = 1
        idToCellList = {} # id -> [ list of cells ]

        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == '1':
                    if y == 0 and x == 0:
                        medium[y][x] = uniqueId
                        uniqueId += 1
                        idToCellList[ medium[y][x] ] = [ (y, x) ]
                    elif y == 0:
                        if medium[y][x-1] != 0:
                            medium[y][x] = medium[y][x-1]
                            idToCellList[ medium[y][x] ].append( (y, x) )
                        else:
                            medium[y][x] = uniqueId
                            uniqueId += 1
                            idToCellList[ medium[y][x] ] = [ (y, x) ]
                    elif x == 0:
                        if medium[y-1][x] != 0:
                            medium[y][x] = medium[y-1][x]
                            idToCellList[ medium[y][x] ].append( (y, x) )
                        else:
                            medium[y][x] = uniqueId
                            uniqueId += 1
                            idToCellList[ medium[y][x] ] = [ (y, x) ]
                    else:
                        if medium[y-1][x] == 0 and medium[y][x-1] == 0:
                            medium[y][x] = uniqueId
                            uniqueId += 1
                            idToCellList[ medium[y][x] ] = [ (y, x) ]
                        elif medium[y-1][x] != 0 and medium[y][x-1] != 0 and medium[y-1][x] != medium[y][x-1]:
                            # merge the larger uniqueId into the smaller one
                            smallerIdx = min(medium[y-1][x], medium[y][x-1])
                            largerIdx = max(medium[y-1][x], medium[y][x-1])
                            for (j, i) in idToCellList[ largerIdx ]:
                                medium[j][i] = smallerIdx
                            idToCellList[ smallerIdx ] += idToCellList[ largerIdx ]
                            del idToCellList[ largerIdx ]

                            medium[y][x] = smallerIdx
                            idToCellList[ medium[y][x] ].append( (y, x) )
                        else:
                            # one is zero, the other is non-zero
                            medium[y][x] = max(medium[y][x-1], medium[y-1][x])
                            idToCellList[ medium[y][x] ].append( (y, x) )

        return len( idToCellList.keys() )

