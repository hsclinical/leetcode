"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        elif len(node.neighbors) == 0:
            nodeCopy = Node(node.val)
            return nodeCopy
        else:
            copied = {}
            nodeCopy = Node(node.val)
            copied[ node.val ] = nodeCopy
            self.copyNode( copied, node, nodeCopy )
            return nodeCopy

    def copyNode( self, copied, nodeOrig, nodeCopy ):
        if nodeOrig.neighbors == None:
            pass
        else:
            neighbors = []
            listToRecursive = []
            for curNodeOrig in nodeOrig.neighbors:
                if curNodeOrig.val in copied:
                    neighbors.append( copied[ curNodeOrig.val ] )
                else:
                    curNodeCopy = Node(curNodeOrig.val)
                    copied[ curNodeOrig.val ] = curNodeCopy
                    neighbors.append( copied[ curNodeOrig.val ] )
                    listToRecursive.append( curNodeOrig )
            nodeCopy.neighbors = neighbors

            for node in listToRecursive:
                self.copyNode( copied, node, copied[node.val] )

