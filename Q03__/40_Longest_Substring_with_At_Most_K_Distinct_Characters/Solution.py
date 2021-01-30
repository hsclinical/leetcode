class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        sLen = len(s)
        if sLen <= k:
            return sLen
        else:
            longestLen = 0
            bgnIdx = 0
            distinctChar = 0
            charFreq = {}
            for i, char in enumerate(s):
                if char not in charFreq:
                    charFreq[ char ] = 1
                    distinctChar += 1
                    if distinctChar > k:
                        # remove char from bgnIdx
                        while True:
                            charFreq[ s[bgnIdx] ] -= 1
                            if charFreq[ s[bgnIdx] ] == 0:
                                del charFreq[ s[bgnIdx] ]
                                distinctChar -= 1
                                bgnIdx += 1
                                if distinctChar <= k:
                                    break
                            else:
                                bgnIdx += 1
                else:
                    charFreq[ char ] += 1

                if i - bgnIdx + 1 > longestLen:
                    longestLen = i - bgnIdx + 1

            return longestLen
