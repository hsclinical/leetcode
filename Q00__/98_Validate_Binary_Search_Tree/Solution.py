# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.scanTree(root, None, None)

    def scanTree(self, root, minEnd, maxEnd):
        outcome = True
        if root.left != None:
            if root.left.val >= root.val:
                outcome = False
            if minEnd != None and root.left.val <= minEnd:
                outcome = False
            if maxEnd != None and root.left.val >= maxEnd:
                outcome = False
            if not self.scanTree(root.left, minEnd, root.val):
                outcome = False
        if outcome == True and root.right != None:
            if root.right.val <= root.val:
                outcome = False
            if minEnd != None and root.right.val <= minEnd:
                outcome = False
            if maxEnd != None and root.right.val >= maxEnd:
                outcome = False
            if not self.scanTree(root.right, root.val, maxEnd):
                outcome = False
        return outcome

