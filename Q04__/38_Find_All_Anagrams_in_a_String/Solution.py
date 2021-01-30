from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        outList = []
        sLen = len(s)
        pLen = len(p)
        if sLen < pLen:
            return outList

        # process string p
        pFreq = {}
        pSet = set()
        for char in p:
            if char not in pFreq:
                pFreq[ char ] = 0
                pSet.add( char )
            pFreq[ char ] += 1

        # process string s by sliding a window with pLen
        sFreq = {}
        sSet  = set()
        for i in range(sLen-pLen+1):
            if i == 0:
                for j in range(pLen):
                    if s[j] not in sFreq:
                        sFreq[ s[j] ] = 0
                        sSet.add( s[j] )
                    sFreq[ s[j] ] += 1
            else:
                if s[i+pLen-1] not in sFreq:
                    sFreq[ s[i+pLen-1] ] = 0
                    sSet.add( s[i+pLen-1] )
                sFreq[ s[i+pLen-1] ] += 1

                sFreq[ s[i-1] ] -= 1
                if sFreq[ s[i-1] ] == 0:
                    del sFreq[ s[i-1] ]
                    sSet.remove( s[i-1] )

            if sSet == pSet:
                outcome = True
                for char in sSet:
                    if sFreq[ char ] != pFreq[ char ]:
                        outcome = False
                        break
                if outcome:
                    outList.append(i)

        return outList