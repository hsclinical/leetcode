from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        else:
            if s[1] == '0':
                if int(s[:2]) <= 26:
                    if len(s) == 2:
                        num = 1
                    else:
                        num = self.numDecodings(s[2:])
                else:
                    num = 0
            else:
                num = self.numDecodings(s[1:])
                if int(s[:2]) <= 26:
                    if len(s) == 2:
                        num += 1
                    else:
                        num += self.numDecodings(s[2:])
            return num
