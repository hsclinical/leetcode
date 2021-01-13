from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        outcome = [ [0] * 6 for i in range(n) ]
        colSum = [0] * n

        for i in range(n):
            if i == 0:
                for j in range(6):
                    outcome[i][j] = 1
                    colSum[i] = sum(outcome[i])
            else:
                for j in range(6):
                    if i >= rollMax[j]:
                        outcome[i][j] = 0
                        for k in range(rollMax[j]):
                            outcome[i][j] += (colSum[i-1-k] - outcome[i-1-k][j])
                    else:
                        outcome[i][j] = colSum[i-1]
                colSum[i] = sum(outcome[i])

        #print(outcome)
        return sum(outcome[n-1])%(10**9+7)
