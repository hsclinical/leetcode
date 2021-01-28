from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        else:
            total = costs[0]
            if n == 1:
                return min(total)
            else:
                for i in range(1, n):
                    nextTotal = [0] * 3
                    nextTotal[0] = min(total[1], total[2]) + costs[i][0]
                    nextTotal[1] = min(total[0], total[2]) + costs[i][1]
                    nextTotal[2] = min(total[0], total[1]) + costs[i][2]
                    total = nextTotal
                return min(total)
