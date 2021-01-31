from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0:
            return []
        else:
            outList = self.listCombination(n)
            if n != 1:
                outList = [i for i in outList if not i.startswith('0')]
            return outList

    def listCombination(self, n):
        if n == 1:
            return ["0", "1", "8"]
        elif n == 2:
            return ["00", "11","69","88","96"]
        else:
            prevList = self.listCombination(n-2)
            nextList = []
            list1 = ["0", "1", "8", "6", "9"]
            list2 = ["0", "1", "8", "9", "6"]
            for i, s in enumerate(prevList):
                for j in range(len(list1)):
                    nextList.append( list1[j] + s + list2[j] )
            return nextList
