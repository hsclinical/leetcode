#from bisect import bisect

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hitList = []


    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hitList.append( timestamp )
        if timestamp > 300:
            self.cleanList(timestamp)


    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp > 300:
            self.cleanList(timestamp)
        return len(self.hitList)


    def cleanList(self, timestamp):
        bgn = timestamp-300
        #idx = bisect.bisect_right( self.hitList, bgn )
        #self.hitList = self.hitList[idx:]
        self.hitList = [ x for x in self.hitList if x > bgn ]


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)