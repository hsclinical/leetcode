# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.valList = []
        self.scanTree(root, k)
        return self.valList[k-1]

    def scanTree(self, root, k):
        if len(self.valList) < k:
            if root.left != None:
                self.scanTree(root.left, k)
        if len(self.valList) < k:
            self.valList.append(root.val)
        if len(self.valList) < k:
            if root.right != None:
                self.scanTree(root.right, k)

