from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort position from the largest to the smallest (large one close to target)
        # if there are multiple cars starting at the same position, sort them based on speed
        # fastest first

        positionSpeed = list(zip(position, speed))
        positionSpeed = sorted(positionSpeed, key=lambda x: (x[0], x[1]), reverse=True)

        lastTime = 0
        fleetCount = 0
        for i in range(len(positionSpeed)):
            if i == 0:
                lastTime = (target-positionSpeed[i][0])/positionSpeed[i][1]
                fleetCount += 1
            else:
                curTime = (target-positionSpeed[i][0])/positionSpeed[i][1]
                if curTime <= lastTime:
                    pass
                else:
                    lastTime = curTime
                    fleetCount += 1
        return fleetCount
