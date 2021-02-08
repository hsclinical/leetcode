from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 1:
            return n

        nInEdge = dict([(i, False) for i in range(n) ])
        sToE = {}
        for edge in edges:
            nInEdge[ edge[0] ] = True
            nInEdge[ edge[1] ] = True
            if edge[0] not in sToE:
                sToE[ edge[0] ] = []
            if edge[1] not in sToE:
                sToE[ edge[1] ] = []
            sToE[ edge[0] ].append( edge[1] )
            sToE[ edge[1] ].append( edge[0] )

        outList = []
        visited = set()
        for i in range(n):
            if nInEdge[ i ]:
                if i not in visited:
                    outList.append( i )
                    visited.add( i )
                    curList = sToE[ i ]
                    while True:
                        nextList = []
                        for j in curList:
                            visited.add( j )
                            for k in sToE[ j ]:
                                if k not in visited:
                                    nextList.append( k )

                        if len(nextList) == 0:
                            break
                        else:
                            curList = nextList
            else:
                # never shows up in edge list
                outList.append( i )

        return len(outList)
