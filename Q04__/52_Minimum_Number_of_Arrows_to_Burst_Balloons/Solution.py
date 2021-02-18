class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pointsLen = len(points)
        if pointsLen <= 1:
            return pointsLen
        else:
            sortedPoints = sorted(points, key=lambda x: (x[0], x[1]))

            outList = []
            curBgn = sortedPoints[0][0]
            curEnd = sortedPoints[0][1]
            for i in range(1, pointsLen):
                if sortedPoints[i][0] <= curEnd:
                    curBgn = sortedPoints[i][0]
                    curEnd = min(sortedPoints[i][1], curEnd)
                else:
                    outList.append( (curBgn, curEnd) )
                    curBgn = sortedPoints[i][0]
                    curEnd = sortedPoints[i][1]
            outList.append( (curBgn, curEnd) )

            return len(outList)
