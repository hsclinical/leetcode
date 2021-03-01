from typing import List

class Solution:
    def expand(self, s: str) -> List[str]:
        subListG = False
        twoDList = []
        for char in s:
            if char == '{':
                subListG = True
                subListC = []
            elif char == '}':
                subListG = False
                twoDList.append( subListC )
            else:
                if char == ',':
                    continue
                else:
                    if subListG:
                        subListC.append( char )
                    else:
                        twoDList.append( [ char ] )

        outputList = self.listAllCombination(twoDList, len(twoDList), 0)
        return outputList


    def listAllCombination(self, inputList, inputLen, curIdx):
        if curIdx == inputLen - 1:
            return sorted(inputList[ curIdx ])
        else:
            outputList = []
            previousList = self.listAllCombination(inputList, inputLen, curIdx+1)
            currentList = sorted(inputList[ curIdx ])
            for curChar in currentList:
                for prevString in previousList:
                    outputList.append( curChar + prevString )
            return outputList