# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.currentId = 0
        self.uniqueIdToNode = {} # root.uniqueId -> [node]
        self.tupleToUniqueId = {} # (root.val, left.uniqueId, right.uniqueId) -> root.uniqueId

        self.dfsTree(root)
        return [ self.uniqueIdToNode[i][0] for i in self.uniqueIdToNode if len(self.uniqueIdToNode[i]) > 1]

    def dfsTree(self, root):
        if root.left == None and root.right == None:
            leftUniqueId = None
            rightUniqueId = None
        elif root.right == None:
            leftUniqueId = self.dfsTree(root.left)
            rightUniqueId = None
        elif root.left == None:
            leftUniqueId = None
            rightUniqueId = self.dfsTree(root.right)
        else:
            leftUniqueId = self.dfsTree(root.left)
            rightUniqueId = self.dfsTree(root.right)

        key = (root.val, leftUniqueId, rightUniqueId)
        if key in self.tupleToUniqueId:
            uniqueId = self.tupleToUniqueId[ key ]
            self.uniqueIdToNode[ uniqueId ].append( root )
        else:
            self.tupleToUniqueId[ key ] = self.currentId
            self.uniqueIdToNode[ self.currentId ] = [ root ]
            self.currentId += 1
        return self.tupleToUniqueId[ key ]
