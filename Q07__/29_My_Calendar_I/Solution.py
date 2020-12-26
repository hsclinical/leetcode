class MyCalendar:

    def __init__(self):
        self.startToEnd = {}
        self.sortedStart = []

    def book(self, start: int, end: int) -> bool:
        if len(self.sortedStart) == 0:
            self.sortedStart.append(start)
            self.startToEnd[ start ] = end
            return True

        if start in self.startToEnd:
            return False
        else:
            if start < self.sortedStart[0]:
                if end <= self.sortedStart[0]:
                    self.sortedStart.insert(0, start)
                    self.startToEnd[ start ] = end
                    return True
                else:
                    return False
            elif start > self.sortedStart[-1]:
                if start >= self.startToEnd[ self.sortedStart[-1] ]:
                    self.sortedStart.append(start)
                    self.startToEnd[ start ] = end
                    return True
                else:
                    return False
            else:
                insIndex = self.findIndex(start, 0, len(self.sortedStart)-1)
                if self.startToEnd[ self.sortedStart[ insIndex ] ] > start or self.sortedStart[ insIndex+1 ] < end:
                    return False
                else:
                    self.sortedStart.insert(insIndex+1, start)
                    self.startToEnd[ start ] = end
                    return True

    def findIndex(self, start, bgnIdx, endIdx):
        if bgnIdx + 1 == endIdx:
            return bgnIdx
        else:
            midIdx = (bgnIdx + endIdx)//2
            if start > self.sortedStart[midIdx]:
                return self.findIndex(start, midIdx, endIdx)
            else:
                return self.findIndex(start, bgnIdx, midIdx)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)