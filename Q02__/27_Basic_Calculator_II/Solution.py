class Solution:
    def calculate(self, s: str) -> int:
        curList = []
        lastIdx = 0
        for i, char in enumerate(s):
            if char == '+' or char == '-' or char == '*' or char == '/':
                curList.append( int(s[lastIdx:i]) )
                curList.append( char )
                lastIdx = i + 1
        curList.append( int(s[lastIdx:]) )

        # calcualte * and / first
        nextList = []
        curLen = len(curList)
        curIdx = 0
        while True:
            if curList[ curIdx ] != '*' and curList[ curIdx ] != '/':
                nextList.append( curList[ curIdx ] )
                curIdx += 1
            else:
                num1 = nextList.pop()
                num2 = curList[ curIdx + 1 ]
                if curList[ curIdx ] == '*':
                    nextList.append( num1 * num2 )
                else:
                    nextList.append( num1 // num2 )
                curIdx += 2

            if curIdx >= curLen:
                break

        # calcualte + and - first
        curList = nextList
        nextList = []
        curLen = len(curList)
        curIdx = 0
        while True:
            if curList[ curIdx ] != '+' and curList[ curIdx ] != '-':
                nextList.append( curList[ curIdx ] )
                curIdx += 1
            else:
                num1 = nextList.pop()
                num2 = curList[ curIdx + 1 ]
                if curList[ curIdx ] == '+':
                    nextList.append( num1 + num2 )
                else:
                    nextList.append( num1 - num2 )
                curIdx += 2

            if curIdx >= curLen:
                break

        return nextList[0]