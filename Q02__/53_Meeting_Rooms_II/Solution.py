from typing import List
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timePoint = {}
        for interval in intervals:
            if interval[0] not in timePoint:
                timePoint[ interval[0] ] = defaultdict(int)
            if interval[1] not in timePoint:
                timePoint[ interval[1] ] = defaultdict(int)
            timePoint[ interval[0] ][ 1 ] += 1
            timePoint[ interval[1] ][ 2 ] += 1

        maxRoom = 1
        curRoom = 0
        for curTime in sorted(timePoint):
            curRoom -= timePoint[ curTime ][ 2 ]
            curRoom += timePoint[ curTime ][ 1 ]
            if curRoom > maxRoom:
                maxRoom = curRoom

        return maxRoom
