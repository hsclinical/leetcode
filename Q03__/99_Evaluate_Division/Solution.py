from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodeExist = set()
        nodeDistance = {}
        for i in range(len(values)):
            # equations[i][0]， equations[i][1]， values[i]
            nodeExist.add(equations[i][0])
            nodeExist.add(equations[i][1])

            if equations[i][0] not in nodeDistance:
                nodeDistance[ equations[i][0] ] = {}
            if equations[i][1] not in nodeDistance:
                nodeDistance[ equations[i][1] ] = {}

            if equations[i][1] not in nodeDistance[ equations[i][0] ]:
                nodeDistance[ equations[i][0] ][ equations[i][1] ] = values[i]
            if equations[i][0] not in nodeDistance[ equations[i][1] ]:
                nodeDistance[ equations[i][1] ][ equations[i][0] ] = 1/values[i]
        #print(nodeDistance)

        # check queries
        output = []
        for i in range(len(queries)):
            if queries[i][0] not in nodeExist or queries[i][1] not in nodeExist:
                output.append(-1.0)
            elif queries[i][0] == queries[i][1]:
                output.append(1.0)
            else:
                nodeToStartDist = {}
                nodeToStartDist[ queries[i][0] ] = 1.0

                currList = [ queries[i][0] ]
                while True:
                    nextList = []
                    foundInLoop = False
                    for cNode in currList:
                        for nNode in nodeDistance[cNode]:
                            if nNode not in nodeToStartDist:
                                nodeToStartDist[ nNode ] = nodeToStartDist[ cNode ] * nodeDistance[ cNode ][ nNode ]
                                nextList.append(nNode)

                                if nNode == queries[i][1]:
                                    output.append( nodeToStartDist[ nNode ] )
                                    foundInLoop = True
                                    break
                        if foundInLoop:
                            break
                    if foundInLoop:
                        break
                    else:
                        if len(nextList) == 0:
                            output.append(-1.0)
                            break
                        else:
                            currList = nextList
        return output