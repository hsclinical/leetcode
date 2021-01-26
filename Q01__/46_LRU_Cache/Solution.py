class LRUCache:
    def __init__(self, capacity: int):
        self.dataDict = {}
        self.dataList = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dataList:
            index = self.dataList.index(key)
            if index != len(self.dataList) - 1:
                self.dataList.pop(index)
                self.dataList.append(key)
            return self.dataDict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dataList:
            self.dataList.remove(key)
            self.dataList.append(key)
            self.dataDict[ key ] = value
        else:
            if len(self.dataList) < self.capacity:
                self.dataList.append(key)
                self.dataDict[ key ] = value
            else:
                elem = self.dataList.pop(0)
                del self.dataDict[ elem ]
                self.dataList.append(key)
                self.dataDict[ key ] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)