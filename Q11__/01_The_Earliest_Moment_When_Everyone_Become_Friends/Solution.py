from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        found = False
        timestamp = None
        grpId = 0
        personToGrpId = {}
        grpIdToSet = {}
        for singleLog in sorted(logs):
            finalGrpId = None
            if singleLog[1] not in personToGrpId and singleLog[2] not in personToGrpId:
                personToGrpId[ singleLog[1] ] = grpId
                personToGrpId[ singleLog[2] ] = grpId
                grpIdToSet[ grpId ] = set()
                grpIdToSet[ grpId ].add( singleLog[1] )
                grpIdToSet[ grpId ].add( singleLog[2] )
                finalGrpId = grpId
                grpId += 1
            elif singleLog[1] not in personToGrpId:
                curGrpId = personToGrpId[ singleLog[2] ]
                personToGrpId[ singleLog[1] ] = curGrpId
                grpIdToSet[ curGrpId ].add( singleLog[1] )
                finalGrpId = curGrpId
            elif singleLog[2] not in personToGrpId:
                curGrpId = personToGrpId[ singleLog[1] ]
                personToGrpId[ singleLog[2] ] = curGrpId
                grpIdToSet[ curGrpId ].add( singleLog[2] )
                finalGrpId = curGrpId
            else:
                if personToGrpId[ singleLog[1] ] == personToGrpId[ singleLog[2] ]:
                    finalGrpId = personToGrpId[ singleLog[1] ]
                else:
                    curGrpId1 = personToGrpId[ singleLog[1] ]
                    curGrpId2 = personToGrpId[ singleLog[2] ]
                    grpIdToSet[ curGrpId1 ] = grpIdToSet[ curGrpId1 ].union( grpIdToSet[ curGrpId2 ] )
                    for person in personToGrpId:
                        if personToGrpId[ person ] == curGrpId2:
                            personToGrpId[ person ] = curGrpId1
                    finalGrpId = personToGrpId[ singleLog[1] ]

            if len( grpIdToSet[ finalGrpId ] ) == N:
                found = True
                timestamp = singleLog[0]
                break

        if found:
            return timestamp
        else:
            return -1
