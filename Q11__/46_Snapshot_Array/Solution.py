class SnapshotArray:
    '''
    # v1.0.0: easy to read, but need more memory and not efficient
    def __init__(self, length: int):
        initArray = [0] * length
        self.array = []
        self.array.append(initArray)
        self.maxId = 0

    def set(self, index: int, val: int) -> None:
        self.array[self.maxId][index] = val

    def snap(self) -> int:
        newArray = self.array[self.maxId][:]
        self.array.append(newArray)
        self.maxId += 1
        return self.maxId - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.array[snap_id][index]
    '''

    def __init__(self, length: int):
        self.currentSnapId = 0
        self.dataArray = [0] * length
        self.snapLog = {}

    def set(self, index: int, val: int) -> None:
        # update self.snapLog
        if index not in self.snapLog:
            self.snapLog[ index ] = {}
        self.snapLog[ index ][ self.currentSnapId ] = val

        # set current value
        self.dataArray[ index ] = val

    def snap(self) -> int:
        previousSnapId = self.currentSnapId
        self.currentSnapId += 1
        return previousSnapId

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snapLog:
            sortedSnapId = sorted(self.snapLog[ index ].keys())
            if snap_id < sortedSnapId[0]:
                return 0
            elif snap_id >= sortedSnapId[-1]:
                return self.snapLog[ index ][ sortedSnapId[-1] ]
            else:
                #lastOne = sortedSnapId[0]
                #for snapVersion in sortedSnapId:
                #    if snap_id < snapVersion:
                #        break
                #    else:
                #        lastOne = snapVersion
                #        continue
                snapVersion = self.findIndex(snap_id, sortedSnapId, 0, len(sortedSnapId)-1)
                return self.snapLog[ index ][ snapVersion ]
        else:
            return 0

    def findIndex(self, num, sortedSnapId, bgn, end):
        if bgn + 1 == end:
            return sortedSnapId[bgn]
        else:
            mid = (bgn + end)//2
            if num >= sortedSnapId[mid]:
                return self.findIndex(num, sortedSnapId, mid, end)
            else:
                return self.findIndex(num, sortedSnapId, bgn, mid)



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)