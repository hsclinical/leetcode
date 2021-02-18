from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasLen = len(gas)
        absGas = [ gas[i] - cost[i] for i in range(gasLen) ]

        sumGas = sum(absGas)

        if sumGas < 0:
            return -1
        else:
            for i, num in enumerate(absGas):
                if i == 0:
                    numSum = num
                    minSum = num
                    minIdx = 0
                else:
                    numSum += num
                    if numSum < minSum:
                        minSum = numSum
                        minIdx = i
            return (minIdx + 1) % gasLen