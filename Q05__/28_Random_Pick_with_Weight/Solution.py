from typing import List
from random import randrange

class Solution:
    accumulate = []
    countAll = 0
    sumAll = 0

    def __init__(self, w: List[int]):
        self.accumulate = [0]
        total = 0
        for num in w:
            total += num
            self.accumulate.append(total)
        self.countAll = len(self.accumulate)
        self.sumAll = total

    def pickIndex(self) -> int:
        pickedNum = randrange(self.sumAll)
        # Solution v1.0.0 O(n)
        # This solution is not optimal. The complexity is O(n)
        # Since the list is sorted, the better solution should be O(logn)
        # Time Test with (100K pick): 90 sec
        #
        #for i in range(len(self.accumulate)-1):
        #    if pickedNum >= self.accumulate[i] and pickedNum < self.accumulate[i+1]:
        #        return i

        # Solution v1.1.0
        # Use list comprehension, which is slightly better than for loop
        #
        #output = min(i for i in range(self.countAll) if self.accumulate[i] > pickedNum)
        #return output - 1

        # Solution v2.0.0 O(logn)
        # Time Test with (100K pick): 1 sec
        #
        return self.findIndex(pickedNum, 0, self.countAll)

    def findIndex(self, pickedNum, idxBgn, idxEnd):
        if idxBgn + 1 == idxEnd:
            return idxBgn
        else:
            idxMed = (idxBgn + idxEnd)//2
            if pickedNum >= self.accumulate[idxMed]:
                return self.findIndex(pickedNum, idxMed, idxEnd)
            else:
                return self.findIndex(pickedNum, idxBgn, idxMed)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()