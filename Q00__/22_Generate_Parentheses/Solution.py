from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return [ '()' ]
        else:
            # the first must be '('
            # the last  must be ')'
            return self.listCombination(n)


    def listCombination(self, depth):
        if depth == 1:
            return [ '()' ]
        else:
            listIn = self.listCombination(depth-1)
            listOut = set()

            inLen = (depth-1)*2
            for curString in listIn:
                for i in range(inLen+1):
                    for j in range(i, inLen+1):
                        if i == j:
                            newString = curString[:i] + '()' + curString[i:]
                        else:
                            newString = curString[:i] + '(' + curString[i:j] + ')' + curString[j:]
                        listOut.add(newString)
            return list(listOut)

