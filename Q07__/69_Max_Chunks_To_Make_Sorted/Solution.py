class Solution:
    def maxChunksToSorted(self, arr):
        intervals = {}
        for i in range(len(arr)):
            if i < arr[i]:
                minVal, maxVal = i, arr[i]
            else:
                minVal, maxVal = arr[i], i
            if minVal in intervals:
                if maxVal > intervals[ minVal ]:
                    intervals[ minVal ] = maxVal
            else:
                intervals[ minVal ] = maxVal

        sortedKeys = sorted(intervals.keys())
        if len(sortedKeys) == 1:
            return 1
        else:
            bgnNum = sortedKeys[0]
            endNum = intervals[ sortedKeys[0] ]

            outCount = 0
            for i in range(1, len(sortedKeys)):
                if endNum < sortedKeys[i]:
                    endNum = intervals[ sortedKeys[i] ]
                    outCount += 1
                else:
                    endNum = max(endNum, intervals[ sortedKeys[i] ])
            outCount += 1
            return outCount
