# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            self.overall = 1
            longest, val = self.findLongest(root)
            return self.overall

    def findLongest(self, root):
        if root.left == None and root.right == None:
            return 1, root.val
        elif root.right == None:
            (lLen, lVal) = self.findLongest(root.left)
            if lVal - root.val == 1:
                if lLen+1 > self.overall:
                    self.overall = lLen+1
                return (lLen+1), root.val
            else:
                return 1, root.val
        elif root.left == None:
            (rLen, rVal) = self.findLongest(root.right)
            if rVal - root.val == 1:
                if rLen+1 > self.overall:
                    self.overall = rLen+1
                return (rLen+1), root.val
            else:
                return 1, root.val
        else:
            (lLen, lVal) = self.findLongest(root.left)
            (rLen, rVal) = self.findLongest(root.right)
            longest = 1
            if lVal - root.val == 1 and lLen + 1 > longest:
                longest = lLen + 1
            if rVal - root.val == 1 and rLen + 1 > longest:
                longest = rLen + 1
            if longest > self.overall:
                self.overall = longest
            return longest, root.val
