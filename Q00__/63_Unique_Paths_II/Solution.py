class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        yLen = len(obstacleGrid)
        xLen = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        elif yLen == 1 and xLen == 1:
            return 1

        matrix = [ [0] * xLen for _ in range(yLen) ]

        for y in range(yLen):
            for x in range(xLen):
                if y == 0 and x == 0:
                    matrix[0][0] = 1
                    continue
                if obstacleGrid[y][x] == 0:
                    # space only
                    if y == 0:
                        matrix[y][x] = matrix[y][x-1]
                    elif x == 0:
                        matrix[y][x] = matrix[y-1][x]
                    else:
                        matrix[y][x] = matrix[y][x-1] + matrix[y-1][x]

        return matrix[yLen-1][xLen-1]