from typing import List
import bisect

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        numLen = len(nums)
        numSum = sum(nums)
        if numSum <= threshold:
            return 1
        elif numLen == threshold:
            return max(nums)
        else:
            # numLen < threshold
            sortedNums = sorted(nums)
            numBgn = 1
            numEnd = sortedNums[-1]
            numToThreshold = {}
            while True:
                if numEnd - numBgn == 1:
                    tmpList = []
                    if numBgn not in numToThreshold:
                        tmpList.append(numBgn)
                    elif numEnd not in numToThreshold:
                        tmpList.append(numEnd)
                    for curDivisor in tmpList:
                        idxBgnToSearch = bisect.bisect_right(sortedNums, curDivisor)
                        curSum = idxBgnToSearch
                        for i in range(idxBgnToSearch, numLen):
                            if sortedNums[i] % curDivisor == 0:
                                curSum += sortedNums[i] / curDivisor
                            else:
                                curSum += (sortedNums[i] // curDivisor) + 1

                        numToThreshold[curDivisor] = curSum
                    break
                else:
                    curDivisor = (numBgn + numEnd) // 2
                    idxBgnToSearch = bisect.bisect_right(sortedNums, curDivisor)
                    curSum = idxBgnToSearch
                    for i in range(idxBgnToSearch, numLen):
                        if sortedNums[i] % curDivisor == 0:
                            curSum += int(sortedNums[i] / curDivisor)
                        else:
                            curSum += (sortedNums[i] // curDivisor) + 1

                    numToThreshold[curDivisor] = curSum
                    if curSum <= threshold:
                        numEnd = curDivisor
                    else:
                        numBgn = curDivisor
            #print(numToThreshold)

            return min( [ x for x in numToThreshold if numToThreshold[x] <= threshold ] )