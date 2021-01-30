class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        sLen = len(S)
        if sLen == 0:
            return 0
        elif sLen == 1:
            # throw out error message
            pass
            return 0
        else:
            sList = []
            bgnIdx = 0
            num = 0
            while True:
                if bgnIdx > sLen-1:
                    if num != 0:
                        sList.append(num)
                    break
                elif bgnIdx == sLen-1:
                    if num != 0:
                        sList.append(num)
                    sList.append(S[bgnIdx])
                    break
                else:
                    if S[bgnIdx:(bgnIdx+2)] == '()':
                        num += 1
                        bgnIdx += 2
                    else:
                        if num != 0:
                            sList.append(num)
                            num = 0
                        sList.append(S[bgnIdx])
                        bgnIdx += 1

            stack = []
            for elem in sList:
                if elem == '(':
                    stack.append('(')
                elif elem == ')':
                    num = 0
                    while True:
                        if stack[-1] == '(':
                            num = num * 2
                            stack.pop()
                            stack.append(num)
                            break
                        else:
                            num += stack.pop()
                else:
                    stack.append(elem)
            return sum(stack)