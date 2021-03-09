from itertools import chain
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sortedMatrix = list(chain.from_iterable(matrix))
        heapq.heapify(sortedMatrix)
        return heapq.nsmallest(k, sortedMatrix)[-1]