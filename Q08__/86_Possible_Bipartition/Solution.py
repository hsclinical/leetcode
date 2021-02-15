from typing import List

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) <= 1:
            return True
        else:
            catId = 0
            numToCatId = {}
            catIdToPair = {}
            for dislike in dislikes:
                if dislike[0] not in numToCatId and dislike[1] not in numToCatId:
                    numToCatId[ dislike[0] ] = catId
                    numToCatId[ dislike[1] ] = catId
                    catIdToPair[ catId ] = [ dislike ]
                    catId += 1
                elif dislike[0] not in numToCatId:
                    numToCatId[ dislike[0] ] = numToCatId[ dislike[1] ]
                    catIdToPair[ numToCatId[ dislike[1] ] ].append( dislike )
                elif dislike[1] not in numToCatId:
                    numToCatId[ dislike[1] ] = numToCatId[ dislike[0] ]
                    catIdToPair[ numToCatId[ dislike[0] ] ].append( dislike )
                else:
                    if numToCatId[ dislike[0] ] == numToCatId[ dislike[1] ]:
                        catIdToPair[ numToCatId[ dislike[0] ] ].append( dislike )
                    else:
                        # merge to the smaller one
                        if numToCatId[ dislike[0] ] > numToCatId[ dislike[1] ]:
                            minCatId = numToCatId[ dislike[1] ]
                            maxCatId = numToCatId[ dislike[0] ]
                        else:
                            minCatId = numToCatId[ dislike[0] ]
                            maxCatId = numToCatId[ dislike[1] ]
                        for num in numToCatId:
                            if numToCatId[ num ] == maxCatId:
                                numToCatId[ num ] = minCatId
                        catIdToPair[ minCatId ] += catIdToPair[ maxCatId ]
                        catIdToPair[ minCatId ].append( dislike )
                        del catIdToPair[ maxCatId ]

            print(catIdToPair)
            # for all groups pass, the final result pass. Otherwise, it fail
            finalOutcome = True
            for catId in catIdToPair:
                tmpList = catIdToPair[ catId ]
                if len(tmpList) >= 2:
                    numToGrpId = {}
                    numToGrpId[ tmpList[0][0] ] = 0
                    numToGrpId[ tmpList[0][1] ] = 1
                    outcome = self.addPair(numToGrpId, tmpList, len(tmpList), 1)
                    if not outcome:
                        finalOutcome = False
            return outcome


    def addPair(self, numToGrpId, dislikes, dislikesLen, curIdx):
        dislike = dislikes[curIdx]
        if dislike[0] not in numToGrpId and dislike[1] not in numToGrpId:
            if curIdx == dislikesLen - 1:
                return True
            else:
                numToGrpIdCopy = dict(numToGrpId)
                numToGrpIdCopy[ dislike[0] ] = 1
                numToGrpIdCopy[ dislike[1] ] = 0
                outcome1 = self.addPair(numToGrpIdCopy, dislikes, dislikesLen, curIdx+1)
                if outcome1:
                    return True
                numToGrpId[ dislike[0] ] = 0
                numToGrpId[ dislike[1] ] = 1
                outcome2 = self.addPair(numToGrpId, dislikes, dislikesLen, curIdx+1)
                if outcome2:
                    return True
        elif dislike[0] not in numToGrpId:
            if curIdx == dislikesLen - 1:
                return True
            else:
                switchGrpId = (numToGrpId[ dislike[1] ] + 1) % 2
                numToGrpId[ dislike[0] ] = switchGrpId
                outcome = self.addPair(numToGrpId, dislikes, dislikesLen, curIdx+1)
                if outcome:
                    return True
        elif dislike[1] not in numToGrpId:
            if curIdx == dislikesLen - 1:
                return True
            else:
                switchGrpId = (numToGrpId[ dislike[0] ] + 1) % 2
                numToGrpId[ dislike[1] ] = switchGrpId
                outcome = self.addPair(numToGrpId, dislikes, dislikesLen, curIdx+1)
                if outcome:
                    return True
        else:
            if curIdx == dislikesLen - 1:
                if numToGrpId[ dislike[0] ] != numToGrpId[ dislike[1] ]:
                    return True
            else:
                if numToGrpId[ dislike[0] ] != numToGrpId[ dislike[1] ]:
                    outcome = self.addPair(numToGrpId, dislikes, dislikesLen, curIdx+1)
                    if outcome:
                        return True
        return False
