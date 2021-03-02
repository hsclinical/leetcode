class MyCircularQueue:

    def __init__(self, k: int):
        self.queueList = [ 0 ] * k
        self.bgnIdx = -1
        self.endIdx = -1
        self.cnt = 0
        self.queueLen = k

    def enQueue(self, value: int) -> bool:
        if self.cnt == self.queueLen:
            return False
        else:
            if self.cnt == 0:
                self.queueList[ 0 ] = value
                self.bgnIdx = 0
                self.endIdx = 0
            else:
                self.endIdx = (self.endIdx + 1) % self.queueLen
                self.queueList[ self.endIdx ] = value
            self.cnt += 1
            return True

    def deQueue(self) -> bool:
        if self.cnt == 0:
            return False
        else:
            self.bgnIdx = (self.bgnIdx + 1) % self.queueLen
            self.cnt -= 1
            return True

    def Front(self) -> int:
        if self.cnt == 0:
            return -1
        else:
            return self.queueList[ self.bgnIdx ]

    def Rear(self) -> int:
        if self.cnt == 0:
            return -1
        else:
            return self.queueList[ self.endIdx ]

    def isEmpty(self) -> bool:
        if self.cnt == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.cnt == self.queueLen:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()