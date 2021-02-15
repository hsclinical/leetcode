class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stoneLen = len(stones)

        grpIdx = 0
        xNumToGrpIdx = {}
        yNumToGrpIdx = {}

        for stone in stones:
            if stone[0] in xNumToGrpIdx and stone[1] in yNumToGrpIdx:
                if xNumToGrpIdx[ stone[0] ] == yNumToGrpIdx[ stone[1] ]:
                    pass
                else:
                    # merge one group index to the smaller one
                    if xNumToGrpIdx[ stone[0] ] > yNumToGrpIdx[ stone[1] ]:
                        minGrpIdx = yNumToGrpIdx[ stone[1] ]
                        maxGrpIdx = xNumToGrpIdx[ stone[0] ]
                    else:
                        minGrpIdx = xNumToGrpIdx[ stone[0] ]
                        maxGrpIdx = yNumToGrpIdx[ stone[1] ]
                    for i in xNumToGrpIdx:
                        if xNumToGrpIdx[ i ] == maxGrpIdx:
                            xNumToGrpIdx[ i ] = minGrpIdx
                    for i in yNumToGrpIdx:
                        if yNumToGrpIdx[ i ] == maxGrpIdx:
                            yNumToGrpIdx[ i ] = minGrpIdx
            elif stone[0] in xNumToGrpIdx:
                yNumToGrpIdx[ stone[1] ] = xNumToGrpIdx[ stone[0] ]
            elif stone[1] in yNumToGrpIdx:
                xNumToGrpIdx[ stone[0] ] = yNumToGrpIdx[ stone[1] ]
            else:
                xNumToGrpIdx[ stone[0] ] = grpIdx
                yNumToGrpIdx[ stone[1] ] = grpIdx
                grpIdx += 1

        grpLen = len(set(xNumToGrpIdx.values()))
        return stoneLen - grpLen