from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        sortedCosts = sorted([ x + [ abs(x[0] - x[1]) ] for x in costs ], key=lambda x: -x[2])

        costSum = 0
        curACnt = 0
        curBCnt = 0

        for sortedCost in sortedCosts:
            if curACnt == n:
                costSum += sortedCost[1]
                curBCnt += 1
            elif curBCnt == n:
                costSum += sortedCost[0]
                curACnt += 1
            else:
                if sortedCost[0] > sortedCost[1]:
                    costSum += sortedCost[1]
                    curBCnt += 1
                else:
                    costSum += sortedCost[0]
                    curACnt += 1

        return costSum