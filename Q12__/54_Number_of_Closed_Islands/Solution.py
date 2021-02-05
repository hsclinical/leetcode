from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        yLen = len(grid)
        xLen = len(grid[0])
        uniqueId = 1
        uniqueIdValid = {}
        uniqueIdCell  = {}
        matrix = [ [0] * xLen for _ in range(yLen) ]

        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == 0:
                    if y == 0 and x == 0:
                        matrix[y][x] = uniqueId
                        uniqueIdValid[ matrix[y][x] ] = False
                        uniqueIdCell[ matrix[y][x] ] = [ (y, x) ]
                        uniqueId += 1
                    elif y == 0:
                        if matrix[y][x-1] != 0:
                            matrix[y][x] = matrix[y][x-1]
                            uniqueIdCell[ matrix[y][x] ].append( (y, x) )
                        else:
                            matrix[y][x] = uniqueId
                            uniqueIdValid[ matrix[y][x] ] = False
                            uniqueIdCell[ matrix[y][x] ] = [ (y, x) ]
                            uniqueId += 1
                    elif x == 0:
                        if matrix[y-1][x] != 0:
                            matrix[y][x] = matrix[y-1][x]
                            uniqueIdCell[ matrix[y][x] ].append( (y, x) )
                        else:
                            matrix[y][x] = uniqueId
                            uniqueIdValid[ matrix[y][x] ] = False
                            uniqueIdCell[ matrix[y][x] ] = [ (y, x) ]
                            uniqueId += 1
                    else:
                        if matrix[y][x-1] == 0 and matrix[y-1][x] == 0:
                            matrix[y][x] = uniqueId
                            uniqueIdValid[ matrix[y][x] ] = True
                            uniqueIdCell[ matrix[y][x] ] = [ (y, x) ]
                            uniqueId += 1
                        elif matrix[y][x-1] == 0:
                            matrix[y][x] = matrix[y-1][x]
                            uniqueIdCell[ matrix[y][x] ].append( (y, x) )
                        elif matrix[y-1][x] == 0:
                            matrix[y][x] = matrix[y][x-1]
                            uniqueIdCell[ matrix[y][x] ].append( (y, x) )
                        else:
                            if matrix[y][x-1] == matrix[y-1][x]:
                                matrix[y][x] = matrix[y][x-1]
                                uniqueIdCell[ matrix[y][x] ].append( (y, x) )
                            else:
                                self.mergeUniqueId(min(matrix[y][x-1], matrix[y-1][x]), max(matrix[y][x-1], matrix[y-1][x]), matrix, uniqueIdValid, uniqueIdCell)
                                matrix[y][x] = min(matrix[y][x-1], matrix[y-1][x])
                                uniqueIdCell[ matrix[y][x] ].append( (y, x) )
                        if x == xLen - 1 or y == yLen - 1:
                            uniqueIdValid[ matrix[y][x] ] = False
        return len( [ i for i in uniqueIdValid if uniqueIdValid[i] ] )

    def mergeUniqueId(self, minId, maxId, matrix, uniqueIdValid, uniqueIdCell):
        uniqueIdValid[ minId ] = uniqueIdValid[ minId ] and uniqueIdValid[ maxId ]
        uniqueIdCell[ minId ] += uniqueIdCell[ maxId ][:]
        for (y, x) in uniqueIdCell[ maxId ]:
            matrix[y][x] = minId
        del uniqueIdValid[ maxId ]
        del uniqueIdCell[ maxId ]