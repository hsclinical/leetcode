# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            self.total = 0
            self.travelTree(root)
            return self.total

    def travelTree(self, root):
        if root.left == None and root.right == None:
            self.total += 1
            return True, root.val
        else:
            cCheck = True
            if root.left != None:
                lCheck, lVal = self.travelTree(root.left)
                if lCheck and lVal == root.val:
                    pass
                else:
                    cCheck = False

            if root.right != None:
                rCheck, rVal = self.travelTree(root.right)
                if rCheck and rVal == root.val:
                    pass
                else:
                    cCheck = False

            if cCheck:
                self.total += 1
            return cCheck, root.val

