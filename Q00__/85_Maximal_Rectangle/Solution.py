from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        yLen = len(matrix)
        if yLen == 0:
            return 0
        xLen = len(matrix[0])
        if xLen == 0:
            return 0

        mediumX = [ [0] * xLen for _ in range(yLen) ]
        mediumY = [ [0] * xLen for _ in range(yLen) ]
        for y in range(yLen):
            for x in range(xLen):
                if y == '0':
                    mediumY[y][x] = int(matrix[y][x])
                else:
                    if matrix[y][x] == '1':
                        mediumY[y][x] = mediumY[y-1][x] + 1

                if x == '0':
                    mediumX[y][x] = int(matrix[y][x])
                else:
                    if matrix[y][x] == '1':
                        mediumX[y][x] = mediumX[y][x-1] + 1

        maxArea = 0
        for y in range(yLen):
            for x in range(xLen):
                if mediumY[y][x] != 0:
                    for i in range(mediumX[y][x]):
                        area = min(mediumY[y][x-i:(x+1)])*(i+1)
                        if area > maxArea:
                            maxArea = area

        return maxArea