class Solution:
    def calculate(self, s: str) -> int:
        # step 1: use stack to calculate the data in bracket
        stackList = []
        for char in s:
            if char == ' ':
                pass
            elif char == ')':
                curString = ''
                while True:
                    curChar = stackList.pop()
                    if curChar == '(':
                        break
                    else:
                        curString = curChar + curString
                sumString = self.simpleCalculate( curString )
                stackList.append( sumString )
            else:
                stackList.append( char )
        finalString = ''.join(stackList)
        finalSum = self.simpleCalculate( finalString )
        return int(finalSum)

    def simpleCalculate(self, s):
        stackList = [ '+' ]
        lastNum = ''
        for char in s:
            if char == ' ':
                pass
            elif char == '+':
                if lastNum == '':
                    if stackList[-1] == '+' or stackList[-1] == '-':
                        pass
                    else:
                        stackList.append( '+' )
                else:
                    stackList.append(lastNum)
                    stackList.append( '+' )
                    lastNum = ''
            elif char == '-':
                if lastNum == '':
                    if stackList[-1] == '+':
                        stackList[-1] = '-'
                    elif stackList[-1] == '-':
                        stackList[-1] = '+'
                    else:
                        stackList.append( '-' )
                else:
                    stackList.append(lastNum)
                    stackList.append( '-' )
                    lastNum = ''
            else:
                lastNum += char
        stackList.append( lastNum )
        score = 0
        for i, j in zip(stackList[0::2], stackList[1::2]):
            score += int( i + j )
        return str(score)
