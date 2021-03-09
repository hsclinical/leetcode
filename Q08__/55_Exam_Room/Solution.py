import bisect

class ExamRoom:

    def __init__(self, N: int):
        self.occupied = []
        self.totalNum = N
        self.cnt = 0

    def seat(self) -> int:
        if self.cnt == 0:
            self.occupied.append(0)
            self.cnt += 1
            return 0
        else:
            seatId = 0
            maxDist = self.occupied[0]
            for i in range(self.cnt-1):
                curDist = (self.occupied[i+1] - self.occupied[i]) // 2
                if curDist > maxDist:
                    maxDist = curDist
                    seatId = self.occupied[i] + curDist
            if self.totalNum - 1 - self.occupied[-1] > maxDist:
                maxDist = self.totalNum - 1 - self.occupied[-1]
                seatId = self.totalNum - 1
            bisect.insort_left(self.occupied, seatId) 
            self.cnt += 1
            return seatId

    def leave(self, p: int) -> None:
        self.occupied.remove(p)
        self.cnt -= 1


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)