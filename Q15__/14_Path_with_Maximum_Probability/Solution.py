from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        edgeToProbs = {}
        nodeEdges = {}
        for i, edge in enumerate(edges):
            sortedEdge = tuple(sorted(edge))
            edgeToProbs[ sortedEdge ] = succProb[ i ]

            if edge[0] not in nodeEdges:
                nodeEdges[ edge[0] ] = []
            if edge[1] not in nodeEdges:
                nodeEdges[ edge[1] ] = []
            nodeEdges[ edge[0] ].append( edge[1] )
            nodeEdges[ edge[1] ].append( edge[0] )

        if start not in nodeEdges or end not in nodeEdges:
            return 0
        else:
            nodeVisited = {}
            nodeToCheck = {}
            nodeToCheck[ start ] = 1
            foundPath = False
            while True:
                # Two cases to break:
                #   1. reach the end
                #   2. never reach the end
                maxNode = max(nodeToCheck, key=nodeToCheck.get)
                nodeVisited[ maxNode ] = nodeToCheck[ maxNode ]
                for nextNode in nodeEdges[ maxNode ]:
                    if nextNode not in nodeVisited:
                        if maxNode > nextNode:
                            curEdge = (nextNode, maxNode)
                        else:
                            curEdge = (maxNode, nextNode)
                        curProb = edgeToProbs[ curEdge ] * nodeVisited[ maxNode ]
                        if nextNode not in nodeToCheck or nodeToCheck[ nextNode ] < curProb:
                            nodeToCheck[ nextNode ] = curProb
                del nodeToCheck[ maxNode ]
                if end in nodeVisited:
                    foundPath = True
                    break
                elif len(nodeToCheck) == 0:
                    break

            if foundPath:
                return nodeVisited[ end ]
            else:
                return 0