from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstLen = len(firstList)
        secondLen = len(secondList)
        if firstLen == 0 or secondLen == 0:
            return []
        else:
            firstIdx = 0
            secondIdx = 0
            intersectionList = []
            while True:
                if firstIdx == firstLen or secondIdx == secondLen:
                    break
                # compare firstList[ firstIdx ] with secondList[ secondIdx ]
                # 6 cases
                if firstList[ firstIdx ][ 0 ] > secondList[ secondIdx ][ 1 ]:
                    secondIdx += 1
                elif firstList[ firstIdx ][ 1 ] < secondList[ secondIdx ][ 0 ]:
                    firstIdx += 1
                elif firstList[ firstIdx ][ 0 ] <= secondList[ secondIdx ][ 0 ] and firstList[ firstIdx ][ 1 ] >= secondList[ secondIdx ][ 1 ]:
                    intersectionList.append( secondList[ secondIdx ] )
                    secondIdx += 1
                elif firstList[ firstIdx ][ 0 ] >= secondList[ secondIdx ][ 0 ] and firstList[ firstIdx ][ 1 ] <= secondList[ secondIdx ][ 1 ]:
                    intersectionList.append( firstList[ firstIdx ] )
                    firstIdx += 1
                elif firstList[ firstIdx ][ 0 ] <= secondList[ secondIdx ][ 1 ] and firstList[ firstIdx ][ 1 ] >= secondList[ secondIdx ][ 1 ]:
                    intersectionList.append( [ firstList[ firstIdx ][ 0 ], secondList[ secondIdx ][ 1 ] ] )
                    secondIdx += 1
                else:
                    intersectionList.append( [ secondList[ secondIdx ][ 0 ], firstList[ firstIdx ][ 1 ] ] )
                    firstIdx += 1
            return intersectionList

