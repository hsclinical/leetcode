from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        yLen = len(accounts)
        xLen = len(accounts[0])
        emailToIdx = {}
        idxConvert = {}
        for y in range(yLen):
            for x in range(1,xLen):
                if accounts[y][x] not in emailToIdx:
                    emailToIdx[ accounts[y][x] ] = [ y ]
                else: