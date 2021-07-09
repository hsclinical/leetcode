import heapq

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        timeToReachList = []
        heapq.heapify( timeToReachList )
        distLen = len( dist )
        for i in range(distLen):
            timeToReach = dist[i] / speed[i]
            heapq.heappush( timeToReachList, timeToReach )

        outcome = 0
        count = 0
        while True:
            count += 1
            if count > distLen:
                break
            curTime = heapq.heappop(timeToReachList)
            if outcome < curTime:
                outcome += 1
            else:
                break
        return outcome

