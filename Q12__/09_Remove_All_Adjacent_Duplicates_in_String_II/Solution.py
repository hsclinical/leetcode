from typing import List

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s

        stackTyp = []
        stackCnt = []
        for char in s:
            if len(stackTyp) == 0:
                stackTyp.append( char )
                stackCnt.append( 1 )
            else:
                if char != stackTyp[-1]:
                    stackTyp.append( char )
                    stackCnt.append( 1 )
                else:
                    stackCnt[-1] += 1
                    if stackCnt[-1] == k:
                        stackTyp.pop()
                        stackCnt.pop()

        typLen = len(stackTyp)
        if typLen == 0:
            return ""
        else:
            return ''.join([ stackTyp[i] * stackCnt[i] for i in range(typLen)])
