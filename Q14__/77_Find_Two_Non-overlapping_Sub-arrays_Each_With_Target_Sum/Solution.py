from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        targetCount = arr.count(target)
        if targetCount >= 2:
            return 2
        else:
            intervals = []
            newBgn = True
            for i in range(len(arr)):
                if arr[i] >= target:
                    newBgn = True
                else:
                    if newBgn:
                        newBgn = False
                        idxBgn = i
                        idxEnd = i
                        total = arr[i]
                    else:
                        idxEnd = i
                        total += arr[i]
                        if total < target:
                            pass
                        elif total == target:
                            intervals.append([idxBgn, idxEnd])
                        else:
                            for j in range(idxBgn, idxEnd):
                                total -= arr[j]
                                idxBgn = j+1
                                if total > target:
                                    pass
                                elif total == target:
                                    intervals.append([idxBgn, idxEnd])
                                    break
                                else:
                                    break

            if targetCount == 1:
                if len(intervals) >= 1:
                    minVal = min([interval[1]-interval[0]+1 for interval in intervals])
                    return minVal + 1
                else:
                    return -1
            else:
                if len(intervals) < 2:
                    return -1
                else:
                    intervals.sort(key=lambda x: x[1]-x[0])
                    found = False
                    output = -1
                    for i in range(len(intervals)-1):
                        for j in range(i+1, len(intervals)):
                            tmp = (intervals[i][1] - intervals[i][0] + 1) + (intervals[j][1] - intervals[j][0] + 1)
                            if found and tmp >= output:
                                break
                            else:
                                if intervals[i][1] < intervals[j][0] or intervals[j][1] < intervals[i][0]:
                                    if not found:
                                        output = tmp
                                        found = True
                                    else:
                                        if output > tmp:
                                            output = tmp
                                    break
                    if found:
                        return output
                    else:
                        return -1