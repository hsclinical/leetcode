from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sLen = len(s)
        if sLen <= 10:
            return []
        else:
            freq = defaultdict(int)
            for i in range(sLen-10+1):
                freq[ s[i:i+10] ] += 1

            outList = [ x for x in freq if freq[x] > 1 ]
            return outList