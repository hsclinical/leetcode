from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        outList = []
        for num in nums:
            if len(outList) == 0:
                outList.append( [ num ] )
            else:
                for i, candidate in enumerate(outList):
                    if outList[i][-1] >= num:
                        outList[i][-1] = num
                        break
                    else:
                        if i == len(outList) - 1:
                            tmpList = outList[i][:] + [ num ]
                            outList.append( tmpList )
                            break
                        else:
                            if num < outList[i+1][-1]:
                                outList[i+1] = outList[i][:] + [ num ]
        #print(outList)

        return len(outList[-1])
