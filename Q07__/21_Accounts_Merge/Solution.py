from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        idxConvert = {} # curIdx -> the smallest idx
        emailToMinIdx = {} # email -> minIdx

        yLen = len(accounts)
        for y in range(yLen):
            xLen = len(accounts[y])
            uniq = set()
            for x in range(1, xLen):
                # to avoid duplicate email within the single list
                if accounts[y][x] in uniq:
                    continue
                else:
                    uniq.add(accounts[y][x])

                if accounts[y][x] not in emailToMinIdx:
                    # it's the first time that the email shows up
                    if y in idxConvert:
                        # previous another email builds the connection between y and a previous row
                        emailToMinIdx[ accounts[y][x] ] = idxConvert[ y ]
                    else:
                        emailToMinIdx[ accounts[y][x] ] = y
                else:
                    minEmailIdx = emailToMinIdx[ accounts[y][x] ]
                    minEmailIdx = self.findMinIdx(idxConvert, minEmailIdx)

                    if y in idxConvert:
                        minIdx = min(idxConvert[ y ], minEmailIdx)
                        maxIdx = max(idxConvert[ y ], minEmailIdx)
                        if minIdx != maxIdx:
                            idxConvert[ maxIdx ] = minIdx
                            for idx in idxConvert:
                                if idxConvert[ idx ] == maxIdx:
                                    idxConvert[ idx ] = minIdx
                    else:
                        if y != minEmailIdx:
                            idxConvert[ y ] = minEmailIdx

        outList = []
        for y in range(yLen):
            if y in idxConvert:
                accounts[ idxConvert[y] ] += accounts[y][1:]
            else:
                outList.append( accounts[y] )

        return [ sorted(set(i)) for i in outList ]

    def findMinIdx(self, idxConvert, curIdx):
        while True:
            if curIdx in idxConvert:
                curIdx = idxConvert[ curIdx ]
            else:
                break
        return curIdx