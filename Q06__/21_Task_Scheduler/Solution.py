from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        wordFreq = {}
        maxValue = 0
        for task in tasks:
            if task in wordFreq:
                wordFreq[ task ] += 1
            else:
                wordFreq[ task ] = 1

            if wordFreq[ task ] > maxValue:
                maxValue = wordFreq[ task ]

        taskLen = len(tasks)
        if n == 0:
            return taskLen
        else:
            valList = list( wordFreq.values() )
            maxCount = len([x for x in valList if x >= maxValue])
            tmpValue = (maxValue - 1) * (n + 1) + maxCount

            return max(taskLen, tmpValue)
