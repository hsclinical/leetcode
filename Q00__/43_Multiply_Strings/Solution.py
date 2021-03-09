class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1Len = len(num1)
        num2Len = len(num2)
        numDict = {}
        for i, letter1 in enumerate(num1):
            for j, letter2 in enumerate(num2):
                tenCnt = (num1Len - 1 - i) + (num2Len - 1 - j)
                if tenCnt not in numDict:
                    numDict[ tenCnt ] = []
                numDict[ tenCnt ].append( int(letter1) * int(letter2) )

        sumVal = 0
        for tenCnt in numDict:
            sumVal += (10**tenCnt) * sum( numDict[tenCnt] )
        return str(sumVal)
