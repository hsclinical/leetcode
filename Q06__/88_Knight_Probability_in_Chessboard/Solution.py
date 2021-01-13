class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        preData = [ [0] * N for x in range(N) ]
        preData[r][c] = 1
        for enumK in range(K):
            curData = [ [0] * N for x in range(N) ]
            for rIdx, row in enumerate(preData):
                for cIdx, col in enumerate(row):
                    if preData[rIdx][cIdx] != 0:
                        for dr, dc in [ (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2) ]:
                            if rIdx+dr >= 0 and rIdx+dr < N and cIdx+dc >= 0 and cIdx+dc < N:
                                curData[rIdx+dr][cIdx+dc] += preData[rIdx][cIdx]/8
            preData = curData
        return sum([sum(i) for i in preData])

