class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        else:
            sLen = len(s)
            cnt = sLen
            for i in range(sLen-1):
                # check i, i+1
                maxIdx = min(i, sLen-i-2)
                for idx in range(maxIdx+1):
                    if s[i-idx] == s[i+1+idx]:
                        cnt += 1
                    else:
                        break

                # check i-1, i, i+1
                if i >= 1:
                    maxIdx = min(i-1, sLen-i-2)
                    for idx in range(maxIdx+1):
                        if s[i-1-idx] == s[i+1+idx]:
                            cnt += 1
                        else:
                            break

            return cnt