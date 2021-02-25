from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longestLen = 0
        arrLen = len(arr)
        if arrLen < 3:
            return 0

        for i in range(1, arrLen-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                idxBgn = i - 1
                idxEnd = i + 1
                while True:
                    if idxBgn == 0 or arr[idxBgn-1] >= arr[idxBgn]:
                        break
                    else:
                        idxBgn -= 1
                while True:
                    if idxEnd == arrLen - 1 or arr[idxEnd+1] >= arr[idxEnd]:
                        break
                    else:
                        idxEnd += 1
                if idxEnd - idxBgn + 1 > longestLen:
                    longestLen = idxEnd - idxBgn + 1

        return longestLen