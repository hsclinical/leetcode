from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        outList = []

        xBgn = 0
        xEnd = len(matrix[0])-1
        yBgn = 0
        yEnd = len(matrix)-1
        xCur = 0
        yCur = 0
        ori = "xi" # xi -> yi -> xd -> yd

        visited = set()
        while True:
            if (yCur, xCur) in visited:
                break
            else:
                visited.add( (yCur, xCur) )

            outList.append(matrix[yCur][xCur])

            if ori == "xi":
                if xCur == xEnd:
                    ori = 'yi'
                    yBgn += 1
                    if yBgn > yEnd:
                        break
                    yCur += 1
                else:
                    xCur += 1
            elif ori == "yi":
                if yCur == yEnd:
                    ori = 'xd'
                    xEnd -= 1
                    if xEnd < xBgn:
                        break
                    xCur -= 1
                else:
                    yCur += 1
            elif ori == "xd":
                if xCur == xBgn:
                    ori = 'yd'
                    yEnd -= 1
                    if yEnd < yBgn:
                        break
                    yCur -= 1
                else:
                    xCur -= 1
            elif ori == "yd":
                if yCur == yBgn:
                    ori = 'xi'
                    xBgn += 1
                    if xBgn > xEnd:
                        break
                    xCur += 1
                else:
                    yCur -= 1

        return outList
