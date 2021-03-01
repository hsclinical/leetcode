from typing import List

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        numStringLen = len(num)
        if numStringLen < 3:
            return False

        numTmp = (numStringLen+1) // 2
        if num[0] == '0' and num[1] == '0':
            if len( set(num) ) == 1:
                return True
            else:
                return False
        elif num[0] == '0':
            found = False
            for j in range(1, numTmp):
                if j != numStringLen - 1: 
                    if self.isAdditiveChecker(num, numStringLen, (0, 0), (1, j)):
                        found = True
                        break
            return found
        else:
            found = False
            for i in range(numTmp - 1):
                for j in range(i + 1, i + numTmp):
                    if j != numStringLen - 1: 
                        if self.isAdditiveChecker(num, numStringLen, (0, i), (i + 1, j)):
                            found = True
                            break
            return found


    def isAdditiveChecker(self, numString, numStringLen, num1Tuple, num2Tuple):
        # num1 (bgn1, end1) example: (0, 0)
        # num2 (bgn2, end2) example: (1, 2)
        if num2Tuple[1] == numStringLen - 1:
            return True

        str1 = numString[ num1Tuple[0]:(num1Tuple[1]+1) ]
        str2 = numString[ num2Tuple[0]:(num2Tuple[1]+1) ]
        if (str1[0] == '0' and len(str1) == 1) or str1[0] != '0':
            num1 = int(str1)
        else:
            return False
        if (str2[0] == '0' and len(str2) == 1) or str2[0] != '0':
            num2 = int(str2)
        else:
            return False
        numSum = str(num1 + num2)
        if numString[ (num2Tuple[1]+1):(num2Tuple[1]+1+len(numSum)) ] == numSum:
            return self.isAdditiveChecker(numString, numStringLen, num2Tuple, (num2Tuple[1]+1, num2Tuple[1]+len(numSum)) )
        else:
            return False
