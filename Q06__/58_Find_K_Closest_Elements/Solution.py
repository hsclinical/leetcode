from typing import List
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        else:
            count = 0
            arrLen = len(arr)
            outList = []

            if x in arr:
                idxTmp = bisect.bisect_left(arr, x)
                idxLeft = idxTmp
                idxRight = idxTmp + 1
            else:
                idxTmp = bisect.bisect_left(arr, x)
                idxLeft = idxTmp - 1
                idxRight = idxTmp

            while True:
                if count == k:
                    break
                else:
                    if idxLeft < 0:
                        outList.append( arr[idxRight] )
                        idxRight += 1
                        count += 1
                    elif idxRight >= arrLen:
                        outList.insert( 0, arr[idxLeft] )
                        idxLeft -= 1
                        count += 1
                    else:
                        if x - arr[idxLeft] <= arr[idxRight] - x:
                            outList.insert( 0, arr[idxLeft] )
                            idxLeft -= 1
                            count += 1
                        else:
                            outList.append( arr[idxRight] )
                            idxRight += 1
                            count += 1
            return outList

