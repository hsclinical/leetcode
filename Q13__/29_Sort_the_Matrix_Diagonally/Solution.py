from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        yLen = len(mat)
        xLen = len(mat[0])
        if yLen == 1 or xLen == 1:
            return mat
        else:
            bgnCellList = [ (0, x) for x in range(xLen) ] + [ (y, 0) for y in range(1, yLen) ]
            matList = {}
            for bgnCell in bgnCellList:
                matList[ bgnCell ] = []
                y = bgnCell[0]
                x = bgnCell[1]
                while True:
                    if y <= yLen - 1 and x <= xLen - 1:
                        matList[ bgnCell ].append( mat[y][x] )
                        y = y + 1
                        x = x + 1
                    else:
                        break

            for bgnCell in bgnCellList:
                sortedList = sorted(matList[ bgnCell ])
                y = bgnCell[0]
                x = bgnCell[1]
                cnt = 0
                while True:
                    if y <= yLen - 1 and x <= xLen - 1:
                        mat[y][x] = sortedList[ cnt ]
                        y = y + 1
                        x = x + 1
                        cnt += 1
                    else:
                        break

            return mat
