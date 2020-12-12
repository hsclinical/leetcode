from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        if len(intervals) == 0:
            return output
        startToEnd = {}
        for interval in intervals:
            if interval[0] in startToEnd:
                if interval[1] > startToEnd[ interval[0] ]:
                    startToEnd[ interval[0] ] = interval[1]
            else:
                startToEnd[ interval[0] ] = interval[1]

        sortedStart = sorted(startToEnd.keys())

        for i in range(len(sortedStart)):
            if i == 0:
                previousStart = sortedStart[0]
                previousEnd   = startToEnd[ sortedStart[0] ]
            else:
                if sortedStart[i] > previousEnd:
                    output.append([previousStart, previousEnd])
                    previousStart = sortedStart[i]
                    previousEnd   = startToEnd[ sortedStart[i] ]
                else:
                    if startToEnd[ sortedStart[i] ] > previousEnd:
                        previousEnd = startToEnd[ sortedStart[i] ]
        output.append([previousStart, previousEnd])
        return output