from typing import List
from math import sqrt

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        pointsLen = len(points)
        if pointsLen < 4:
            return 0
        else:
            minArea = 0
            points = sorted(points, key=lambda element: (element[0], element[1]))
            for i in range(pointsLen-3):
                for j in range(i+1, pointsLen-2):
                    for k in range(j+1, pointsLen-1):
                        for l in range(k+1, pointsLen):
                            curArea = self.isRect(points[i], points[j], points[k], points[l])
                            if curArea != 0:
                                if minArea == 0:
                                    minArea = curArea
                                else:
                                    if curArea < minArea:
                                        minArea = curArea
            return minArea

    def isRect(self, point1, point2, point3, point4):
        sum14X = point1[0] + point4[0]
        sum23X = point2[0] + point3[0]
        sum14Y = point1[1] + point4[1]
        sum23Y = point2[1] + point3[1]
        if sum14X == sum23X and sum14Y == sum23Y:
            cPointX = (sum14X + sum23X)/4
            cPointY = (sum14Y + sum23Y)/4
            dist1 = (point1[0] - cPointX) ** 2 + (point1[1] - cPointY) ** 2
            dist2 = (point2[0] - cPointX) ** 2 + (point2[1] - cPointY) ** 2
            dist3 = (point3[0] - cPointX) ** 2 + (point3[1] - cPointY) ** 2
            dist4 = (point4[0] - cPointX) ** 2 + (point4[1] - cPointY) ** 2
            if dist1 == dist2 and dist1 == dist3 and dist1 == dist4:
                area = sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) * \
                    sqrt((point1[0] - point3[0]) ** 2 + (point1[1] - point3[1]) ** 2)
                return area
            else:
                return 0
        else:
            return 0

