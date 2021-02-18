from typing import List
from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        valuesLen = len(values)
        sortedZipValue = sorted( [(values[i], labels[i]) for i in range(valuesLen)], key=lambda x: -x[0] )

        valueSum = 0
        valueUsed = 0
        labelUsed = defaultdict(int)
        for i in range(valuesLen):
            if labelUsed[ sortedZipValue[i][1] ] < use_limit:
                valueSum += sortedZipValue[i][0]
                labelUsed[ sortedZipValue[i][1] ] += 1
                valueUsed += 1

            if valueUsed >= num_wanted:
                break

        return valueSum
