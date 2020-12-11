# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathP = []
        pathQ = []
        
        self.getPath(root, pathP, p)
        self.getPath(root, pathQ, q)

        minLen = len(pathP)
        if len(pathQ) < minLen:
            minLen = len(pathQ)
        
        lcAncestor = root
        for i in range(minLen):
            if pathP[i] == pathQ[i]:
                lcAncestor = pathP[i]
            else:
                break
        return lcAncestor


    def getPath(self, root, rarr, x):
        if not root:
            return False

        rarr.append(root)

        if root == x:
            return True

        if self.getPath(root.left, rarr, x) or self.getPath(root.right, rarr, x):
            return True

        rarr.pop()

        return False
