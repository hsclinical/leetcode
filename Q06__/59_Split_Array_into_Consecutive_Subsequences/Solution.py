from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        numOrdered = []
        curLen = 0

        for num in nums:
            inserted = False
            for i in range(curLen-1, -1, -1):
                if num - numOrdered[i][-1] == 0:
                    pass
                elif num - numOrdered[i][-1] == 1:
                    numOrdered[i].append( num )
                    inserted = True
                    break
                else:
                    break

            if not inserted:
                numOrdered.append( [ num ] )
                curLen += 1

        success = True
        for singleOrder in numOrdered:
            if len(singleOrder) < 3:
                success = False
                break

        return success