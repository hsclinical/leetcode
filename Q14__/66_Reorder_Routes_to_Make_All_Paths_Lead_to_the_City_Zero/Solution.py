from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        posCon = {}
        negCon = {}
        for singleCon in connections:
            if singleCon[0] not in posCon:
                posCon[ singleCon[0] ] = []
            posCon[ singleCon[0] ].append( singleCon[1] )
            if singleCon[1] not in negCon:
                negCon[ singleCon[1] ] = []
            negCon[ singleCon[1] ].append( singleCon[0] )

        visited = set()
        return self.travelAround(posCon, negCon, visited, 0)

    def travelAround(self, posCon, negCon, visited, curNode):
        total = 0
        visited.add(curNode)

        if curNode in negCon:
            negConList = negCon[ curNode ]
            for nextNode in negConList:
                if nextNode not in visited:
                    total += self.travelAround(posCon, negCon, visited, nextNode)

        if curNode in posCon:
            posConList = posCon[ curNode ]
            for nextNode in posConList:
                if nextNode not in visited:
                    total += 1
                    total += self.travelAround(posCon, negCon, visited, nextNode)

        return total
