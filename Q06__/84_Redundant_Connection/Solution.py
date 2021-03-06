from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        grpId = 1
        numToGrpId = {}
        for edge in edges:
            if edge[0] not in numToGrpId and edge[1] not in numToGrpId:
                numToGrpId[ edge[0] ] = grpId
                numToGrpId[ edge[1] ] = grpId
                grpId += 1
            elif edge[0] not in numToGrpId:
                numToGrpId[ edge[0] ] = numToGrpId[ edge[1] ]
            elif edge[1] not in numToGrpId:
                numToGrpId[ edge[1] ] = numToGrpId[ edge[0] ]
            else:
                if numToGrpId[ edge[0] ] != numToGrpId[ edge[1] ]:
                    toGrpId   = numToGrpId[ edge[0] ]
                    fromGrpId = numToGrpId[ edge[1] ]
                    for num in numToGrpId:
                        if numToGrpId[ num ] == fromGrpId:
                            numToGrpId[ num ] = toGrpId
                else:
                    return edge
            print(edge, numToGrpId)
        return None
