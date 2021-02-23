from typing import List

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        maxLen = 0
        maxList = []
        for singleD in d:
            if self.isSubSequence(s, singleD):
                singleDLen = len(singleD)
                if singleDLen > maxLen:
                    maxLen = singleDLen
                    maxList = [ singleD ]
                elif singleDLen == maxLen:
                    maxList.append( singleD )
        if len(maxList) == 0:
            return ""
        else:
            maxList.sort()
            return maxList[0]

    def isSubSequence(self, longStr, shortStr):
        shortStrLen = len(shortStr)
        shortStrIdx = 0
        found = False
        for s in longStr:
            if s == shortStr[shortStrIdx]:
                shortStrIdx += 1
            if shortStrIdx >= shortStrLen:
                found = True
                break
        return found