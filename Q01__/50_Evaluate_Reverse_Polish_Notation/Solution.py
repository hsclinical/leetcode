from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNum = []
        for singleToken in tokens:
            if singleToken == '+' or singleToken == '-' or singleToken == '*' or singleToken == '/':
                num2 = stackNum.pop()
                num1 = stackNum.pop()
                if singleToken == '+':
                    stackNum.append( num1 + num2 )
                elif singleToken == '-':
                    stackNum.append( num1 - num2 )
                elif singleToken == '*':
                    stackNum.append( num1 * num2 )
                else:
                    if num1 * num2 > 0:
                        numRes = num1 // num2
                    else: 
                        numRes = -1 * ( ( -1 * num1) // num2 )
                    stackNum.append( numRes )
            else:
                stackNum.append( int(singleToken) )
        return stackNum[0]