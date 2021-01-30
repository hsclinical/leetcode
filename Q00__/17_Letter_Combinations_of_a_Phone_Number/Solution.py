from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        else:
            self.numToChar = {}
            self.numToChar['2'] = ['a', 'b', 'c']
            self.numToChar['3'] = ['d', 'e', 'f']
            self.numToChar['4'] = ['g', 'h', 'i']
            self.numToChar['5'] = ['j', 'k', 'l']
            self.numToChar['6'] = ['m', 'n', 'o']
            self.numToChar['7'] = ['p', 'q', 'r', 's']
            self.numToChar['8'] = ['t', 'u', 'v']
            self.numToChar['9'] = ['w', 'x', 'y', 'z']

            return self.listCombination(digits)

    def listCombination(self, digits):
        if len(digits) == 1:
            return self.numToChar[ digits ]
        else:
            outList = []
            listA = self.numToChar[ digits[0] ]
            listB = self.listCombination( digits[1:] )
            for i, a in enumerate(listA):
                for j, b in enumerate(listB):
                    outList.append( a + b )
            return outList
