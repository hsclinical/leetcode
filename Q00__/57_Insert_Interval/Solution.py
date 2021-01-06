from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [ newInterval ]
        else:
            intervalLeft = []
            intervalRight = []
            for interval in intervals:
                if interval[1] < newInterval[0]:
                    intervalLeft.append(interval)
                elif interval[0] > newInterval[1]:
                    intervalRight.append(interval)
                else:
                    newInterval[0] = min(newInterval[0], interval[0])
                    newInterval[1] = max(newInterval[1], interval[1])
            return intervalLeft + [ newInterval ] + intervalRight
