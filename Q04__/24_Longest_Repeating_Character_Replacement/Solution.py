from typing import List
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sLen = len(s)
        if sLen <= k+1:
            return sLen

        longestLen = 0

        freq = defaultdict(int)
        totalLen = 0
        idxBgn = 0
        for i in range(sLen):
            freq[ s[i] ] += 1
            totalLen += 1
            if totalLen - max(freq.values()) > k:
                # move idxBgn
                while True:
                    freq[ s[idxBgn] ] -= 1
                    totalLen -= 1
                    idxBgn += 1
                    if totalLen - max(freq.values()) <= k:
                        break
            else:
                if totalLen > longestLen:
                    longestLen = totalLen

        return longestLen