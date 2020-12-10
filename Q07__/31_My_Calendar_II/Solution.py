class MyCalendarTwo:
    intervalList = []
    maxLayer = 3

    def __init__(self):
        self.intervalList = []

    def book(self, start: int, end: int) -> bool:
        countIntervalCoverInput = 0
        subsetIntervalList = []
        posStartList = []
        posEndList = []
        # find overlap interval
        for iStart, iEnd in zip(self.intervalList[0::2], self.intervalList[1::2]):
            if (iStart <= start) and (iEnd >= end):
                # interval cover input
                countIntervalCoverInput += 1
                if (countIntervalCoverInput >= self.maxLayer - 1):
                    return False
            elif (iStart >= start) and (iEnd <= end):
                # input cover interval
                subsetIntervalList.append(iStart)
                subsetIntervalList.append(iEnd)
                posStartList.append(iStart)
                posEndList.append(iEnd)
            elif (iEnd > start) and (iEnd <= end):
                subsetIntervalList.append(iStart)
                subsetIntervalList.append(iEnd)
                posEndList.append(iEnd)
            elif (iStart >= start) and (iStart < end):
                subsetIntervalList.append(iStart)
                subsetIntervalList.append(iEnd)
                posStartList.append(iStart)


        for candStart in posStartList:
            countPartial = 0
            for iStart, iEnd in zip(subsetIntervalList[0::2], subsetIntervalList[1::2]):
                if (candStart >= iStart) and (candStart < iEnd):
                    countPartial += 1
                    if (countPartial + countIntervalCoverInput >= self.maxLayer - 1):
                        return False

        for candEnd in posEndList:
            countPartial = 0
            for iStart, iEnd in zip(subsetIntervalList[0::2], subsetIntervalList[1::2]):
                if (candEnd > iStart) and (candEnd <= iEnd):
                    countPartial += 1
                    if (countPartial + countIntervalCoverInput >= self.maxLayer - 1):
                        return False

        self.intervalList.append(start)
        self.intervalList.append(end)
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)