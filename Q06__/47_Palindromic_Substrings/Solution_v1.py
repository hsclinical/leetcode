from functools import lru_cache

class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            return self.cntPalindromic(s)


    def cntPalindromic(self, s):
        if len(s) == 1:
            return 1
        else:
            cnt = 1
            for i in range(1, len(s)):
                if self.isPalindromic(s[:(i+1)]):
                    cnt += 1
            cnt += self.cntPalindromic(s[1:])
            return cnt


    @lru_cache(maxsize=None)
    def isPalindromic(self, s):
        if len(s) == 1:
            return True
        else:
            nums = len(s) // 2
            for i in range(nums):
                if s[i] != s[-1-i]:
                    return False
            return True
