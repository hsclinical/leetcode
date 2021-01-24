from typing import List
from functools import lru_cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.output = []
        self.processString(s, [])
        return self.output

    #@lru_cache(maxsize=None)
    def processString(self, s, partPath):
        sLen = len(s)
        if sLen == 1:
            partPath.append(s)
            self.output.append(partPath)
        else:
            for i in range(sLen):
                if self.isPalindrome(s[0:(i+1)]):
                    if i+1 == sLen:
                        partPath.append(s)
                        self.output.append(partPath)
                    else:
                        newPath = partPath[:] + [ s[0:(i+1)] ]
                        self.processString(s[(i+1):], newPath)

    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        else:
            sLen = len(s)
            midLen = sLen//2
            outcome = True
            for i in range(midLen):
                if s[i] != s[sLen-1-i]:
                    outcome = False
                    break
            return outcome
