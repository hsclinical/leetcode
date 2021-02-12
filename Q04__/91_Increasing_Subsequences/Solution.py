class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return []

        medList = []
        for num in nums:
            medListLen = len(medList)
            for i in range(medListLen):
                if num >= medList[i][-1]:
                    single = medList[i][:] + [ num ]
                    if single not in medList:
                        medList.append( single )
            if [ num ] not in medList:
                medList.append( [ num ] )

        finalList = [ i for i in medList if len(i) > 1 ]
        return finalList