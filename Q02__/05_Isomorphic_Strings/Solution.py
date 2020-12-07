class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            output = True
            sToT = {}
            tToS = {}
            for i in range(len(s)):
                if s[i] in sToT:
                    if t[i] != sToT[ s[i] ]:
                        output = False
                        break
                else:
                    sToT[ s[i] ] = t[i]

                if t[i] in tToS:
                    if s[i] != tToS[ t[i] ]:
                        output = False
                        break
                else:
                    tToS[ t[i] ] = s[i]
            return output