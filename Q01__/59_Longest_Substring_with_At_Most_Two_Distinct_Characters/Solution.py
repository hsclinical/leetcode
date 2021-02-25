from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        sLen = len(s)
        if sLen <= 2:
            return sLen

        longestLen = 0
        idxBgn = 0
        maxDictChar = 2
        charFreq = defaultdict(int)
        for i in range(sLen):
            charFreq[ s[i] ] += 1
            if len(charFreq) > maxDictChar:
                if i - idxBgn > longestLen:
                    longestLen = i - idxBgn
                # move idxBgn until maxDictChar < maxDictChar
                while True:
                    charFreq[ s[idxBgn] ] -= 1
                    if charFreq[ s[idxBgn] ] == 0:
                        del charFreq[ s[idxBgn] ]
                    idxBgn += 1
                    if len(charFreq) <= maxDictChar:
                        break

        if sLen - idxBgn > longestLen:
            longestLen = sLen - idxBgn
        return longestLen