from typing import List

class RLEIterator:

    def __init__(self, A: List[int]):
        self.data = A

    def next(self, n: int) -> int:
        outNum = -1
        while True:
            if len(self.data) == 0:
                break
            if n <= self.data[0]:
                self.data[0] -= n
                outNum = self.data[1]
                break
            else:
                n -= self.data[0]
                self.data.pop(0)
                self.data.pop(0)

        return outNum


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)