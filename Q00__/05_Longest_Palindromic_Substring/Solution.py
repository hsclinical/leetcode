class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        if sLen <= 1:
            return s
        else:
            longestLen = 1
            longestStr = s[0]
            for i, char in enumerate(s):
                if i+1<=sLen-1 and s[i] == s[i+1]:
                    curString, curLen = self.expandPalindrome(s, sLen, i, i+1)
                    if curLen > longestLen:
                        longestLen = curLen
                        longestStr = curString
                if i+2<=sLen-1 and s[i] == s[i+2]:
                    curString, curLen = self.expandPalindrome(s, sLen, i, i+2)
                    if curLen > longestLen:
                        longestLen = curLen
                        longestStr = curString
            return longestStr

    def expandPalindrome(self, s, sLen, bgnIdx, endIdx):
        outString = s[bgnIdx:(endIdx+1)]
        while True:
            bgnIdx -= 1
            endIdx += 1
            if bgnIdx >= 0 and endIdx <= sLen - 1:
                if s[bgnIdx] == s[endIdx]:
                    outString = s[bgnIdx:(endIdx+1)]
                else:
                    break
            else:
                break
        return outString, len(outString)
