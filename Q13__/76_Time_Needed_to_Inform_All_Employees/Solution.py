from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
        # v1.0.0: recursive method, works but slow

        maxChildMinute = 0
        for i in range(len(manager)):
            if manager[i] == headID:
                singleMinute = self.numOfMinutes(n, i, manager, informTime)
                if singleMinute > maxChildMinute:
                    maxChildMinute = singleMinute
        totalMinute = maxChildMinute + informTime[headID]
        return totalMinute
        '''

        memberIdxDict = {}
        for idx, employee in enumerate(manager):
            if employee in memberIdxDict:
                memberIdxDict[employee].append(idx)
            else:
                memberIdxDict[employee] = [ idx ]
        return self.countMinutes(headID, memberIdxDict, informTime)

    def countMinutes(self, headID, memberIdxDict, informTime):
        maxChildMinute = 0
        if headID in memberIdxDict:
            members = memberIdxDict[ headID ]
            for member in members:
                singleMinute = self.countMinutes(member, memberIdxDict, informTime)
                if singleMinute > maxChildMinute:
                    maxChildMinute = singleMinute
        totalMinute = maxChildMinute + informTime[headID]
        return totalMinute

