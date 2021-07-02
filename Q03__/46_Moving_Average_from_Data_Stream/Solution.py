class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.maxLen = size
        self.curLen = 0
        self.nums = []

    def next(self, val: int) -> float:
        if self.curLen >= self.maxLen:
            self.nums.pop(0)
        else:
            self.curLen += 1
        self.nums.append( val )
        return sum(self.nums) / self.curLen



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)