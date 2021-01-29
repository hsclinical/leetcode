from typing import List

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        sLen = len(a)
        if sLen == 0:
            return False
        elif sLen == 1:
            return True
        else:
            if self.isPalindrome(a) or self.isPalindrome(b):
                return True
            else:
                checkLen = sLen // 2
                a_P_b_S_check = True
                b_P_a_S_check = True
                a_P_b_S_index = 0
                b_P_a_S_index = 0

                for i in range(checkLen):
                    if a_P_b_S_check:
                        if a[i] != b[sLen-1-i]:
                            a_P_b_S_check = False
                            a_P_b_S_index = i
                    if b_P_a_S_check:
                        if b[i] != a[sLen-1-i]:
                            b_P_a_S_check = False
                            b_P_a_S_index = i
                    if not a_P_b_S_check and not b_P_a_S_check:
                        break;

                if a_P_b_S_check or b_P_a_S_check:
                    return True
                else:
                    if self.isPalindrome(a[a_P_b_S_index:(sLen-a_P_b_S_index)]) or \
                       self.isPalindrome(b[a_P_b_S_index:(sLen-a_P_b_S_index)]) or \
                       self.isPalindrome(a[b_P_a_S_index:(sLen-b_P_a_S_index)]) or \
                       self.isPalindrome(b[b_P_a_S_index:(sLen-b_P_a_S_index)]):
                        return True
                    else:
                         return False

    def isPalindrome(self, s):
        sLen = len(s)
        if sLen == 1:
            return True
        else:
            checkLen = sLen // 2
            for i in range(checkLen):
                if s[i] != s[sLen-1-i]:
                    return False
            return True