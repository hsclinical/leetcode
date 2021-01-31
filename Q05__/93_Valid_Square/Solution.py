from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        points = sorted(points, key=lambda element: (element[0], element[1]))
        return self.isSquare(points)

    def isSquare(self, points):
        sum14X = points[0][0] + points[3][0]
        sum23X = points[1][0] + points[2][0]
        sum14Y = points[0][1] + points[3][1]
        sum23Y = points[1][1] + points[2][1]
        if sum14X == sum23X and sum14Y == sum23Y:
            cpointsX = (sum14X + sum23X)/4
            cpointsY = (sum14Y + sum23Y)/4
            dist1 = (points[0][0] - cpointsX) ** 2 + (points[0][1] - cpointsY) ** 2
            dist2 = (points[1][0] - cpointsX) ** 2 + (points[1][1] - cpointsY) ** 2
            dist3 = (points[2][0] - cpointsX) ** 2 + (points[2][1] - cpointsY) ** 2
            dist4 = (points[3][0] - cpointsX) ** 2 + (points[3][1] - cpointsY) ** 2
            if dist1 != 0 and dist1 == dist2 and dist1 == dist3 and dist1 == dist4:
                if (points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2 == \
                   (points[0][0] - points[2][0]) ** 2 + (points[0][1] - points[2][1]) ** 2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

