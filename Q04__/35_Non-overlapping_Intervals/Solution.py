from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        else:
            endToStart = {}
            numToRemove = 0
            for interval in intervals:
                if interval[1] in endToStart:
                    numToRemove += 1
                    if interval[0] > endToStart[ interval[1] ]:
                        endToStart[ interval[1] ] = interval[0]
                else:
                    endToStart[ interval[1] ] = interval[0]

            reversedEndList = sorted(endToStart.keys(), reverse=True)

            for i in range(len(reversedEndList)):
                if i == 0:
                    previousEnd = reversedEndList[i]
                    previousStart = endToStart[ reversedEndList[i] ]
                else:
                    if reversedEndList[i] <= previousStart:
                        previousEnd = reversedEndList[i]
                        previousStart = endToStart[ reversedEndList[i] ]
                    else:
                        numToRemove += 1
                        if endToStart[ reversedEndList[i] ] > previousStart:
                            previousEnd = reversedEndList[i]
                            previousStart = endToStart[ reversedEndList[i] ]
            return numToRemove