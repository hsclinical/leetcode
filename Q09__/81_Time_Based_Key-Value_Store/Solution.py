import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictTimeDict = {}
        self.dictTimeList = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictTimeDict:
            self.dictTimeDict[ key ] = {}
            self.dictTimeList[ key ] = []
        if timestamp not in self.dictTimeDict[ key ]:
            bisect.insort(self.dictTimeList[ key ], timestamp)
        self.dictTimeDict[ key ][ timestamp ] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictTimeDict:
            return ""
        else:
            idx = bisect.bisect_right(self.dictTimeList[ key ], timestamp)
            if idx == 0:
                return ""
            else:
                return self.dictTimeDict[ key ][ self.dictTimeList[ key ][ idx -1 ] ]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)